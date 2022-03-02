from unittest.mock import patch
from django.urls import path
from . import views


app_name = 'firms'

urlpatterns = [
    path('all/', views.products, name='allproducts'),
    path('addproduct/', views.add_product, name='add_product'),
    path('update/<int:prodid>', views.update_product, name='update_product'),
    path('delete/<int:prodid>', views.delete_product, name='delete_product'),
    path('details/<int:prodid>', views.details, name='details'),
    path('addcompany/', views.add_company, name='add_company'),
    path('editcompany/<int:id>', views.update_company, name='edit_company'),
    path('delete/<int:id>', views.delete_company, name='delete_company'),
    path('companydetails/<int:id>', views.add_company, name='add_company'),    
    path('companies/', views.companies, name='companies'),
]                                                                                                                                        