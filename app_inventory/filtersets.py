from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import *

from app_inventory.models import Material, Instrument


class MaterialFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id', 'title', 'price', 'count'])
    title = CharFilter(field_name='title')

    class Meta:
        model = Material
        fields = ['title', 'ordering']


class InstrumentFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id', 'title', 'price', 'count'])
    title = CharFilter(field_name='title')

    class Meta:
        model = Instrument
        fields = ['title', 'ordering']
