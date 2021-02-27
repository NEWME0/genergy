from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from app_entities.mixins import SupplyMixin, AffordMixin
from common.pagination import DefaultPagination
from common.permissions import IsSuperUser, IsAdminUser, IsStaffUser, IsAgentUser, ReadOnly
from app_entities.models import Item, Util, Work
from app_entities.filtersets import ItemFilterSet, UtilFilterSet, WorkFilterSet
from app_entities.serializers import ItemSerializer, UtilSerializer, WorkSerializer

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
