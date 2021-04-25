from rest_framework.mixins import ListModelMixin
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_nested.viewsets import NestedViewSetMixin

from common.mixins import CreateManyModelMixin
from common.pagination import DefaultPagination
from app_projects.models import Project, ProjectExercise, ProjectExecutor, ProjectMaterial
from app_projects.filtersets import ProjectFilterSet
from app_projects.serializers import ProjectSerializer, \
    ProjectExecutorSerializer, ProjectExerciseSerializer, ProjectMaterialSerializer
from common.permissions import IsSuperUser, IsAdminUser, IsAgentUser


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.with_totals().all()
    serializer_class = ProjectSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsAgentUser)
    ]

    def get_serializer_context(self):
        context = super(ProjectViewSet, self).get_serializer_context()
        context['owner'] = self.request.user
        return context


class ProjectExerciseViewSet(NestedViewSetMixin, ListModelMixin, CreateManyModelMixin, GenericViewSet):
    serializer_class = ProjectExerciseSerializer
    queryset = ProjectExercise.objects.all()
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsAgentUser)
    ]
    parent_lookup_kwargs = {'project_pk': 'project__pk'}

    def get_serializer_context(self):
        context = super(ProjectExerciseViewSet, self).get_serializer_context()
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_pk'])
        return context


class ProjectExecutorViewSet(NestedViewSetMixin, ListModelMixin, CreateManyModelMixin, GenericViewSet):
    serializer_class = ProjectExecutorSerializer
    queryset = ProjectExecutor.objects.all()
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsAgentUser)
    ]
    parent_lookup_kwargs = {'project_pk': 'project__pk'}

    def get_serializer_context(self):
        context = super(ProjectExecutorViewSet, self).get_serializer_context()
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_pk'])
        return context


class ProjectMaterialViewSet(NestedViewSetMixin, ListModelMixin, CreateManyModelMixin, GenericViewSet):
    serializer_class = ProjectMaterialSerializer
    queryset = ProjectMaterial.objects.all()
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsAgentUser)
    ]
    parent_lookup_kwargs = {'project_pk': 'project__pk'}

    def get_serializer_context(self):
        context = super(ProjectMaterialViewSet, self).get_serializer_context()
        context['project'] = get_object_or_404(Project, id=self.kwargs['project_pk'])
        context['user'] = self.request.user
        return context


class UserOwnProjectViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = Project.objects.with_totals().all()
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated
    ]
    parent_lookup_kwargs = {'user_pk': 'owner'}


class UserExeProjectViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = Project.objects.with_totals().all()
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated
    ]
    parent_lookup_kwargs = {'user_pk': 'executors__user'}
