import django_filters
from django_filters import CharFilter, ModelMultipleChoiceFilter

from .models import *

class SignFilter(django_filters.FilterSet):

    class Meta:
        model = DigitalSign
        fields = ['customer','start_date', 'end_date']
