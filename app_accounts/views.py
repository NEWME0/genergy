from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from common.pagination import DefaultPagination
from common.permissions import IsSuperUser, IsAdminUser, IsStaffUser, IsAgentUser, ReadOnly
from app_accounts.filtersets import UserFilterSet
from app_accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]

    @action(methods=['GET'], detail=False, url_path='me', url_name='user-profile', permission_classes=[IsAuthenticated])
    def me(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
