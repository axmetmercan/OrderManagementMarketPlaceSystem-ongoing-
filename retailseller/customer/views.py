from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomerForm
from .models import CustomerInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
@login_required
def customer(request):
    current_user = request.user
    customers = CustomerInfo.objects.filter(user = current_user)
    page = request.GET.get('page',1)
    paginator = Paginator(customers, 10)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)


    context = {
        'customers':customers,
    }

    return render(request, 'customers.html', context)

@login_required
def adding_customer(request):
    form = CustomerForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        print(form.errors)
 
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('users:dashboard')
    

    return render(request, 'addcustomer.html', context)

@login_required
def edit_customer(request, customer_id):

    customer = get_object_or_404(CustomerInfo, id = customer_id)

    form = CustomerForm(request.POST or None, instance = customer)
    
    if form.is_valid():
        customer = form.save(commit=False)
        customer.user = request.user
        customer.save()
        return redirect('customer:customer')
        
    return render(request, 'addcustomer.html',{'form':form})



### Verdiği siparişlerin tablosu linkli bir şekilde eklenicek bu sayfaya
@login_required
def customer_details(request, customer_id):
    customer = get_object_or_404(CustomerInfo, id = customer_id)

    return render(request, 'customerdetails.html', {'customer':customer})
    
