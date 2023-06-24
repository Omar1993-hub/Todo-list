import django_filters
from .models import *
from django_filters import CharFilter
from django.forms.widgets import TextInput


class TodoFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains',widget = TextInput(attrs={
        'placeholder': 'Search by title',
        'class': 'form-control', 
        }), label='Search')
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['dateCreated', 'user']
