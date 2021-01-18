from django.contrib import messages
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.pagination import DefaultPagination
from app_contracts.models import Contract
from app_contracts.serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    pagination_class = DefaultPagination

    def list(self, request, *args, **kwargs):
        return super(ContractViewSet, self).list(request, *args, **kwargs)

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        return super(ContractViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(ContractViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(ContractViewSet, self).destroy(request, *args, **kwargs)
