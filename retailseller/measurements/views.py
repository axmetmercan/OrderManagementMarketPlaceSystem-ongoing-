from datetime import date
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from customer.models import CustomerInfo
from measurements.forms import MeasurementForm
from .models import MeasuementName, Measurement
from .forms import MeasurementWindow
# Create your views here.


@login_required
def add_measurement(request, customer_id):
    customer = get_object_or_404(CustomerInfo, id = customer_id)
    data =  {'customer_id' : customer_id}

    if customer.user == request.user:
        form = MeasurementForm(request.POST or None, initial = data)
        measurements = MeasuementName.objects.filter(customer_id = customer_id).order_by('-date')
            
        context = {
            'customer':customer,
            'form':form,
            'measurements':measurements,
        }


        if form.is_valid():
            measurement = form.save()
            return render(request, 'addmeasurement.html',context)
    else:
        return redirect('customer:customer')
   

    return render(request, 'addmeasurement.html',context)



@login_required
def add_measure_to_customer(request, customer_id, measurement_id):
    customer = get_object_or_404(CustomerInfo, id = customer_id)

    if request.user == customer.user:
        measurements = Measurement.objects.filter(customer_id = customer_id, measurement_id = measurement_id)
        customer = CustomerInfo.objects.filter(id = customer_id)
        print(customer[0].user)

        data = {'measurement_id': measurement_id, 'customer_id':customer_id}
        room_form = MeasurementWindow(request.POST or None, request.FILES or None,  initial=data)
        room_form.fields['measurement_id'].disabled=True
        room_form.fields['customer_id'].disabled=True
        measurement_date = get_object_or_404(MeasuementName, id = measurement_id)
        context = {
        'form':room_form,
        'measurements': measurements,
        'customer':customer[0],
        'measurement_name':MeasuementName.objects.get(id =measurement_id),
        'measure_date':measurement_date.date
        }

        if request.method =='POST':
            if room_form.is_valid():
                room_form.save()
                print('form kaydedildi')    

        return render(request, 'measurements.html',context)
    return redirect('customer:customer')


### There is a bug in this method it need to be refreshed the current page i solved by redirecting it for now.
@login_required
def delete_a_measurement(request, customer_id, measurement_id, measurement_detail_id):
    customer = get_object_or_404(CustomerInfo, id = customer_id)

    if request.user == customer.user:
        measurements = Measurement.objects.filter(customer_id = customer_id, measurement_id = measurement_id)
        customer = CustomerInfo.objects.filter(id = customer_id)

        measurement = get_object_or_404(Measurement, id=measurement_detail_id)
        measurement.delete()

        data = {'measurement_id': measurement_id, 'customer_id':customer_id}
        room_form = MeasurementWindow(request.POST or None, request.FILES or None, initial=data)
        room_form.fields['measurement_id'].disabled=True
        room_form.fields['customer_id'].disabled=True
        context = {
        'form':room_form,
        'measurements': measurements,
        'customer':customer[0],
        'measurement_name':MeasuementName.objects.get(id =measurement_id)
        }

        return redirect('customer:customer')
    return redirect('customer:customer')
