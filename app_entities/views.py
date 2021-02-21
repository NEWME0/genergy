from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from common.pagination import DefaultPagination
from app_entities.models import Item, Util, Work
from app_entities.filtersets import ItemFilterSet, UtilFilterSet, WorkFilterSet
from app_entities.serializers import ItemSerializer, UtilSerializer, WorkSerializer


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ItemFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions


class UtilViewSet(ModelViewSet):
    queryset = Util.objects.all()
    serializer_class = UtilSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UtilFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions


class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilterSet
    permission_classes = [AllowAny]  # Todo: update permissions
