
from django.contrib import admin
from .models import CustomerInfo
# Register your models here.

@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display =['name','surname', 'email','phone']
    list_display_links = ['name','surname']
    search_fields = ['name', 'surname']
    list_filter = ['name']
    class Meta:
        model = CustomerInfo


