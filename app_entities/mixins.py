from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from app_entities.serializers import SupplySerializer, AffordSerializer
from common.permissions import IsSuperUser, IsAdminUser, IsStaffUser


class SupplyMixin:
    @action(
        methods=['POST'], detail=True, url_path='supply', url_name='item-supply',
        permission_classes=[IsAuthenticated & (IsSuperUser | IsAdminUser | IsStaffUser)],
        serializer_class=SupplySerializer
    )
    def supply(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        supply_count = serializer.validated_data['count']
        instance = self.get_object()
        instance.supply(count=supply_count)
        return Response()


class AffordMixin:
    @action(
        methods=['POST'], detail=True, url_path='afford', url_name='item-afford',
        permission_classes=[IsAuthenticated & (IsSuperUser | IsAdminUser | IsStaffUser)],
        serializer_class=AffordSerializer
    )
    def afford(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        afford_count = serializer.validated_data['count']
        afford_user = serializer.validated_data['user']

        instance = self.get_object()
        if afford_count > instance.count:
            raise ValidationError(f'Can not afford ({afford_count}) more than have ({instance.count}).')

        instance.afford(count=afford_count, user=afford_user)
        return Response()
