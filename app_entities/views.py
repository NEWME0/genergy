from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_nested.viewsets import NestedViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from common.pagination import DefaultPagination
from common.permissions import IsSuperUser, IsAdminUser, IsStaffUser, IsAgentUser, ReadOnly
from app_entities.mixins import SupplyMixin, AffordMixin
from app_entities.models import Item, Util, Work, UserItem, UserUtil
from app_entities.filtersets import ItemFilterSet, UtilFilterSet, WorkFilterSet
from app_entities.serializers import ItemSerializer, UtilSerializer, WorkSerializer, UserItemSerializer, \
    UserUtilSerializer

from rest_framework.permissions import IsAuthenticated


class ItemViewSet(SupplyMixin, AffordMixin, ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class UtilViewSet(SupplyMixin, AffordMixin, ModelViewSet):
    queryset = Util.objects.all()
    serializer_class = UtilSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UtilFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilterSet
    permission_classes = [
        IsAuthenticated and (IsSuperUser or IsAdminUser or (ReadOnly and (IsStaffUser or IsAgentUser)))
    ]


class UserItemViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = UserItem.objects.all()
    serializer_class = UserItemSerializer
    permission_classes = [
        IsAuthenticated
    ]
    parent_lookup_kwargs = {'user_pk': 'user__pk'}


class UserUtilViewSet(NestedViewSetMixin, ReadOnlyModelViewSet):
    queryset = UserUtil.objects.all()
    serializer_class = UserUtilSerializer
    permission_classes = [
        IsAuthenticated
    ]
    parent_lookup_kwargs = {'user_pk': 'user__pk'}
