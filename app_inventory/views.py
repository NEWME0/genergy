from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from app_inventory.filtersets import MaterialFilterSet, InstrumentFilterSet
from app_inventory.models import Material, Instrument
from app_inventory.pagination import MaterialPagination, InstrumentPagination
from app_inventory.serializers import MaterialSerializer, InstrumentSerializer


class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    pagination_class = MaterialPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MaterialFilterSet

    def list(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(MaterialViewSet, self).destroy(request, *args, **kwargs)


class InstrumentViewSet(ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    pagination_class = InstrumentPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = InstrumentFilterSet

    def list(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(InstrumentViewSet, self).destroy(request, *args, **kwargs)
