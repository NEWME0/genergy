from django_filters.rest_framework import FilterSet, OrderingFilter, CharFilter

from app_entities.models import Item, Util, Work


class ItemFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['ordering']


class UtilFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Util
        fields = ['ordering']


class WorkFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Work
        fields = ['ordering']
