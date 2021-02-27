from django.contrib.auth import get_user_model
from rest_framework.fields import BooleanField, FloatField, IntegerField
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    is_admin = BooleanField(source='is_admin_account', default=False)
    is_staff = BooleanField(source='is_staff_account', default=False)
    is_agent = BooleanField(source='is_agent_account', default=False)
    is_basic = BooleanField(source='is_basic_account', default=False)

    hour_price = FloatField(min_value=0, default=100)
    agent_rate = IntegerField(min_value=0, max_value=100, default=10)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username', 'password',
            'fullname', 'gender', 'phone', 'idnp',
            'is_admin', 'is_staff', 'is_agent', 'is_basic',
            'hour_price', 'agent_rate',
            'last_login', 'date_joined'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'read_only': True},
            'date_joined': {'read_only': True},
        }

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance = super(UserSerializer, self).update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance
