from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from app_accounts.models import User


class ListCreateModelMixin(GenericViewSet):
    def get_queryset(self):
        return self.queryset.filter(user_id=self.kwargs.get('user_pk'))

    def get_serializer_context(self):
        context = super(ListCreateModelMixin, self).get_serializer_context()
        context['user'] = get_object_or_404(User, id=self.kwargs.get('user_pk'))
        return context

    def create(self, request, *args, **kwargs):
        request_data = request.data if isinstance(request.data, list) else [request.data]
        serializers = [self.get_serializer(data=data) for data in request_data]
        are_valid = [s.is_valid(raise_exception=False) for s in serializers]

        if all(are_valid):
            values = [s.save() for s in serializers]
            return Response({}, status=status.HTTP_201_CREATED)

        else:
            errors = [s.errors for s in serializers]
            return Response(errors, status.HTTP_400_BAD_REQUEST)
