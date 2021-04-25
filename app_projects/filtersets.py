from django_filters.rest_framework import FilterSet, OrderingFilter, CharFilter, ChoiceFilter

from app_projects.models import Project, ProjectState


class ProjectFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='title', lookup_expr='icontains')
    state = ChoiceFilter(choices=ProjectState.choices)

    class Meta:
        model = Project
        fields = ['ordering', 'search', 'state']
