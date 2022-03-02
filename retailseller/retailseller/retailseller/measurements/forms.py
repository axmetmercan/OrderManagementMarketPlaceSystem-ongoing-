
from statistics import mode
from unittest import mock
from measurements.models import MeasuementName, Measurement
from django import forms



class MeasurementForm(forms.ModelForm):

    class Meta:
        model = MeasuementName
        fields = '__all__'

class MeasurementWindow(forms.ModelForm):

    class Meta:
        model = Measurement
        fields = '__all__'

