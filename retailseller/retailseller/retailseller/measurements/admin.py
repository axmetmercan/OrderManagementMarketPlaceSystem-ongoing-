from django.contrib import admin
from .models import MeasuementName, Measurement

# Register your models here.
    
admin.site.register(MeasuementName)
admin.site.register(Measurement)