from os import name
from statistics import mode
from django import forms
from .models import CustomerInfo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = '__all__'
        

### Crispy Form View in Template
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset('Müşteri Bilgileri',
                Row(
                    Column('name', css_class='form-group col-md-3 mb-0'),
                    Column('surname',css_class = 'form-group col-md-3 mb-0'),
                    css_class='container row ms-auto',
                    ),
                Row(
                    Column('phone', css_class='form-group col-md-3 mb-0'),
                    Column('email',css_class = 'form-group col-md-3 mb-0'),
                    css_class='container row ms-auto',
                    ),
                    css_class = 'border boder-bottom pb-3 text text-center pt-3'
            ),
            Fieldset('Fatura Bilgileri',
                Row(
                    Column('invoince_type', css_class = 'form-group col-md-2 mb-0'),
                    Column('turkish_id', css_class = 'form-group col-md-3 mb-0'),
                    Column('tax_id', css_class = 'form-group col-md-3 mb-0'),
                    css_class='container row ms-auto',
                    ),
                Row(

                    Column('tax_name', css_class = 'form-group col-md-4 mb-0'),
                    Column('tax_surname', css_class = 'form-group col-md-4 mb-0'),
                    css_class='container row ms-auto',
                ),
                Row(

                    Column('tax_office', css_class = 'form-group col-md-4 mb-0'),
                    Column('tax_title', css_class = 'form-group col-md-4 mb-0'),
                    css_class='container row ms-auto',
                ),
                Row(

                    Column('invoince_address', css_class = 'form-group col-md-8 mb-0'),
                    css_class='container row ms-auto',
                ),
               css_class = 'border boder-bottom pb-3 text text-center',
            ),
            Submit('submit','Değişiklikleri Kaydet', 
            css_class='btn btn-success  container-fluid'),
        )

