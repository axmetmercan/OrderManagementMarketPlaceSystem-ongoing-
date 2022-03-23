
from dataclasses import field, fields
from pyexpat import model
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Firm, Head, Product, Variant

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"




class ProductVariants(forms.ModelForm):
    class Meta:
        model = Variant
        fields = "__all__"



class FirmForm(forms.ModelForm):
    class Meta:
        model = Firm
        fields = "__all__"
        widgets = {'user':forms.HiddenInput()}

class HeadForm(forms.ModelForm):
    class Meta:
        model = Head
        fields = "__all__"
        widgets = {'user': forms.HiddenInput()}
