from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'username', 'password', 'first_name', 'last_name', 'email', 'is_active', 'last_login', 'date_joined',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
        }
        # gender, IDNP, phone
        # staff, manager, worker
        # stavka, razmer stavki
        # procent, razmer protsenta
