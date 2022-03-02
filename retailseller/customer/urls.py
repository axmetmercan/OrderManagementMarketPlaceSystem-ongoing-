from os import name
from django.contrib import admin
from django.urls import path
from . import views 


app_name = 'customer'

urlpatterns = [
    path('', views.customer, name='customer'),
    path('addcustomer/', views.adding_customer, name='add_customer'),
    path('addcustomer/<int:customer_id>', views.edit_customer, name='edit_customer'),
    path('details/<int:customer_id>', views.customer_details, name='customer_details'),
]                                                                       