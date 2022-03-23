
# Create your views here.

from math import prod
from msilib.schema import File
from multiprocessing import context
from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import AddProductForm, FirmForm, HeadForm, ProductVariants
from .models import Firm, Head, Product, Variant

#Pagination will be added to this view.
@login_required
def products(request):
    if request.method == "GET":


        all_products = Product.objects.all().order_by('head_name')
        page = request.GET.get('page',1)
        paginator = Paginator(all_products, 24)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)



        context = {
            'products': products,
        }
        return render(request, 'products.html', context)
    else:
        return render(request, 'products.html')





@login_required
def add_product(request):
    product_form = AddProductForm(request.POST or None, request.FILES or None)
      
    if request.method == 'POST':
        print(product_form.errors)
        if product_form.is_valid():
            product_form.save()

        return redirect('firms:allproducts')


    context = {
            'form':product_form,
        }    

    return render(request, 'addproduct.html', context)


@login_required
def add_variant(request, prodid):

    product = get_object_or_404(Product, id = prodid)
    data = {
        'product' : product
    }
    variant_form = ProductVariants(request.POST or None, initial=data)
    variant_form.fields['product'].disabled = True

    if request.method == 'POST' and 'submit' in request.POST:
        if variant_form.is_valid():
            print('buraya girdi')
            variant_form.save()

            return redirect('firms:details', prodid=prodid)
    elif request.method == 'POST' and 'submintandnew' in request.POST:

        if variant_form.is_valid():
            print('buraya girdi')
            variant_form.save()

            return redirect('firms:add_variant', prodid=prodid)
    
    return render(request, 'addproduct.html', {'form':variant_form})





@login_required
def delete_variant(request, prodid, variant_id):
    variant = get_object_or_404(Variant, id = variant_id)

    if variant:
        variant.delete()
        return redirect('firms:details', prodid=prodid)
    return redirect('firms:allproducts')


@login_required
def update_product(request, prodid):
    
    product = get_object_or_404(Product, id = prodid)
    product_form = AddProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == 'POST' and 'submit' in request.POST:

        if product_form.is_valid():
            print('form vlaid')
            product.save()
            return redirect('firms:allproducts')
    
    elif request.method == 'POST' and 'submintandnew' in request.POST:

        if product_form.is_valid():
            product_form.save()

            return redirect('firms:add_variant', prodid=prodid)

    return render(request, 'addproduct.html', {'form':product_form})





@login_required
def delete_product(request, prodid):

    product = get_object_or_404(Product, id = prodid)
    product.delete()
    return redirect('firms:allproducts')






@login_required
def details(request, prodid):

    if request.method == "GET":
        product = Product.objects.get(id = prodid)
        variants = Variant.objects.filter(product = prodid)

        context = {'product':product,
                    'variants': variants,
                    }

        return render(request, 'productdetails.html', context)

    return redirect('product:allproducts')


@login_required
def companies(request):

    firms = Firm.objects.all()
    heads = Head.objects.all()


    context ={
        'firms':firms,
        'heads':heads,
    }

    return render(request, 'firms.html', context)



@login_required
def add_company(request):
    firm_form = FirmForm(request.POST or None, initial={'user':request.user})
    firm_form.fields['user'].disabled = True

    if request.method == 'GET':
        return render(request, 'addproduct.html', {'brand_form':firm_form})
    print(firm_form.errors)
    if firm_form.is_valid():
        firm_form.save()
        return redirect('firms:companies')
    return redirect('firms:companies')

    

@login_required
def add_company_head(request):
    head_form = HeadForm(request.POST or None)
    head_form['user'].initial = request.user

    if request.method == 'GET':

        
        #head_form.fields['user'].widget = forms.HiddenInput()
        return render(request, 'addproduct.html', {'head_form':head_form})

    if head_form.is_valid():
        print('buraya girmiyor')
        head_form.save()
        return redirect('firms:companies')
    return redirect('firms:companies')



@login_required
def update_company(request, compid):
    return redirect('product:allproducts')

@login_required
def delete_company(request, compid):

    firm = get_object_or_404(Firm, id = compid)
    print(firm)
    print('burasi')
    if firm:
        firm.delete()
        return redirect('firms:companies')
    return redirect('firms:companies'),

@login_required
def delete_head(request, head_id):

    head = get_object_or_404(Head, id = head_id)

    if head:
        head.delete()
        return redirect('firms:companies')
    return redirect('firms:companies')


@login_required
def company_details(request, compid):
    return redirect('product:allproducts')
