from django_filters.rest_framework import FilterSet, OrderingFilter, BooleanFilter

from app_accounts.models import User


class UserFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    is_admin = BooleanFilter(field_name='is_admin_account')
    is_staff = BooleanFilter(field_name='is_staff_account')
    is_agent = BooleanFilter(field_name='is_agent_account')
    is_basic = BooleanFilter(field_name='is_basic_account')

    class Meta:
        model = User
        fields = ['ordering']
