from unittest.mock import patch
from django.urls import path
from . import views


app_name = 'measurements'

urlpatterns = [
    path('all', views.products, name='products'),
]                                                                                                                                        