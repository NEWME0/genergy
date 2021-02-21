from django_filters.rest_framework import FilterSet, OrderingFilter

from app_projects.models import Project, ProjectExecutor, ProjectExercise, ProjectMaterial


class ProjectFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = Project
        fields = ['ordering']


class ProjectExerciseFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = ProjectExercise
        fields = ['ordering']


class ProjectExecutorFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = ProjectExecutor
        fields = ['ordering']


class ProjectMaterialFilterSet(FilterSet):
    ordering = OrderingFilter(fields=['id'])

    class Meta:
        model = ProjectMaterial
        fields = ['ordering']
