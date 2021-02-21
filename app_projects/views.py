from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin

from common.pagination import DefaultPagination
from app_projects.models import Project, ProjectExercise, ProjectExecutor, ProjectMaterial
from app_projects.filtersets import ProjectFilterSet, \
    ProjectExecutorFilterSet, ProjectExerciseFilterSet, ProjectMaterialFilterSet
from app_projects.serializers import ProjectSerializer, \
    ProjectExecutorSerializer, ProjectExerciseSerializer, ProjectMaterialSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions


class ProjectExerciseViewSet(ModelViewSet):
    serializer_class = ProjectExerciseSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectExerciseFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions
    queryset = ProjectExercise.objects.all()
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs.get('project_pk'))


class ProjectExecutorViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = ProjectExecutorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectExecutorFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions
    queryset = ProjectExecutor.objects.all()
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs.get('project_pk'))


class ProjectMaterialViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = ProjectMaterialSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectMaterialFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions
    queryset = ProjectMaterial.objects.all()
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }

    def perform_create(self, serializer):
        serializer.save(project_id=self.kwargs.get('project_pk'))
