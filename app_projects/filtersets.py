from django_filters.rest_framework import FilterSet, OrderingFilter, CharFilter, ChoiceFilter

from app_projects.models import Project, ProjectExecutor, ProjectExercise, ProjectMaterial, ProjectState


class ProjectFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='title', lookup_expr='icontains')
    state = ChoiceFilter(choices=ProjectState.choices)

    class Meta:
        model = Project
        fields = ['ordering', 'search', 'state']


class ProjectExerciseFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='work__title', lookup_expr='icontains')

    class Meta:
        model = ProjectExercise
        fields = ['ordering', 'search']


class ProjectMaterialFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='item__title', lookup_expr='icontains')

    class Meta:
        model = ProjectMaterial
        fields = ['ordering', 'search']


class ProjectExecutorFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])
    search = CharFilter(field_name='user__fullname', lookup_expr='icontains')

    class Meta:
        model = ProjectExecutor
        fields = ['ordering', 'search']
