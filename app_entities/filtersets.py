from django_filters.rest_framework import FilterSet
from django_filters.rest_framework.filters import OrderingFilter

from app_entities.models import Item, Util, Work


class ItemFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = Item
        fields = ['ordering']


class UtilFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = Util
        fields = ['ordering']


class WorkFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = Work
        fields = ['ordering']
