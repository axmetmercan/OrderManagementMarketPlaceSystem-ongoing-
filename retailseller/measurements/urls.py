from unittest.mock import patch
from django.urls import path
from . import views


app_name = 'measurements'

urlpatterns = [
    path('addmeasurement/<int:customer_id>', views.add_measurement, name='add_measurement'),
    path('addmeasurement/<int:customer_id>/<int:measurement_id>', views.add_measure_to_customer, name='add_measure_to_customer'),
    path('delete/<int:customer_id>/<int:measurement_id>/<int:measurement_detail_id>', views.delete_a_measurement, name='delete_measurement'),
]                                                                                                                                        