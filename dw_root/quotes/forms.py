from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets

from .models import Customer, DigitalSign


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Customer
        fields = '__all__'

        # widgets = {
        #     'jobfile' : forms.FileInput(attrs={'class': 'input-file-control'}),
        # }


class DigitalSignForm(ModelForm):

    class Meta:
        model = DigitalSign
        fields = '__all__'
        exclude = ['username',]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }
