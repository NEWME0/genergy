from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from app_accounts.filtersets import UserFilterSet
from app_accounts.serializers import UserSerializer
from common.pagination import DefaultPagination


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions
