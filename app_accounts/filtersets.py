from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, OrderingFilter, BooleanFilter


class UserFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    is_admin = BooleanFilter(field_name='is_admin_account')
    is_staff = BooleanFilter(field_name='is_staff_account')
    is_agent = BooleanFilter(field_name='is_agent_account')
    is_basic = BooleanFilter(field_name='is_basic_account')

    class Meta:
        model = get_user_model()
        fields = ['ordering']
