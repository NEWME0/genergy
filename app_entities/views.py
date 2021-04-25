from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from app_entities.mixins import ListCreateModelMixin
from common.pagination import DefaultPagination
from common.permissions import IsSuperUser, IsAdminUser, IsStaffUser, IsAgentUser, ReadOnly
from app_entities.models import Item, Util, Work, UserItem, UserUtil
from app_entities.filtersets import ItemFilterSet, UtilFilterSet, WorkFilterSet
from app_entities.serializers import ItemSerializer, UtilSerializer, WorkSerializer, \
    UserItemSerializer, UserUtilSerializer


class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class UtilViewSet(ModelViewSet):
    queryset = Util.objects.all()
    serializer_class = UtilSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UtilFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class UserItemViewSet(ListModelMixin, ListCreateModelMixin, GenericViewSet):
    serializer_class = UserItemSerializer
    queryset = UserItem.objects.all()
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsStaffUser or (ReadOnly and IsAgentUser))
    ]


class UserUtilViewSet(ListModelMixin, ListCreateModelMixin, GenericViewSet):
    serializer_class = UserUtilSerializer
    queryset = UserUtil.objects.all()
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or IsStaffUser or (ReadOnly and IsAgentUser))
    ]
