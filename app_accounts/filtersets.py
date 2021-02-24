from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, OrderingFilter


class UserFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = get_user_model()
        fields = ['ordering']
