from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from accounts.pagination import DefaultPagination
from accounts.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPagination
