from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ['is_superuser', 'is_active', 'is_staff', 'user_permissions', 'groups']
        extra_kwargs = {
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
            'password': {'write_only': True},
        }
