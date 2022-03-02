
from dataclasses import field
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Product, Variant

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
    helper = FormHelper()
    helper.add_input(Submit('submit', 'Kaydet', css_class='btn-success'))



class ProductVariants(forms.ModelForm):
    class Meta:
        model = Variant
        fields = "__all__"

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Kaydet', css_class = "btn-primary"))
    helper.add_input(Submit('submit', 'Kaydet ve Başka Varyant Ekle', css_class = "btn-primary"))
