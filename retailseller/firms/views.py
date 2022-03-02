
# Create your views here.

from msilib.schema import File
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import AddProductForm, ProductVariants
from .models import Firm, Head, Product, Variant

#Pagination will be added to this view.
@login_required
def products(request):
    if request.method == "GET":
        all_products = Product.objects.all().order_by('head_name')
        context = {
            'products': all_products,
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
            product_id = product_form.save()

        product = Product.objects.get(id = product_id.id)
        product_data = {
            'brand':product.brand,
            'head_name': product.head_name,
            'code': product.code,
            'category':product.category,
            'color':product.color,
            'widt':product.width,
            'max_width':product.max_width,
            'unit_price':product.unit_price,
        
        }
        print(product_id.code)
        variant_data = {
            'variant_code':product_id.code,    
        }

        product_form = AddProductForm(request.POST or None, request.FILES or None, initial=product_data)
        variant_form = ProductVariants(request.POST or None, initial=variant_data)

        context = {
            'form':product_form,
            'variants':variant_form,
        }    
        print(variant_form.errors)

        return render(request, 'addproduct.html', context)


    context = {
            'form':product_form,
        }    

    return render(request, 'addproduct.html', context)








@login_required
def update_product(request, prodid):
    return redirect('product:allproducts')

@login_required
def delete_product(request, prodid):
    return redirect('product:allproducts')

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
    return redirect('product:allproducts')

@login_required
def update_company(request, compid):
    return redirect('product:allproducts')

@login_required
def delete_company(request, compid):
    return redirect('product:allproducts')

@login_required
def company_details(request, compid):
    return redirect('product:allproducts')
