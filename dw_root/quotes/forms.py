from django import forms
from django.forms import ModelForm, widgets

from .models import Customer

class CustomerForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Customer
        fields = '__all__'

        # widgets = {
        #     'jobfile' : forms.FileInput(attrs={'class': 'input-file-control'}),
        # }