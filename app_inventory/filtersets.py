from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import *


class MaterialFilterSet(FilterSet):
    title = CharFilter(field_name='title')
    price = RangeFilter(field_name='price')
    count = RangeFilter(field_name='count')
    ordering = OrderingFilter(fields=['id', 'title', 'price', 'count'])


class InstrumentFilterSet(FilterSet):
    title = CharFilter(field_name='title')
    price = RangeFilter(field_name='price')
    count = RangeFilter(field_name='count')
    ordering = OrderingFilter(fields=['id', 'title', 'price', 'count'])
