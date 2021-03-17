from django.contrib.auth import get_user_model
from rest_framework.fields import FloatField, IntegerField, CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from app_entities.models import Item, Util, Work, UserItem


class WorkSerializer(ModelSerializer):
    price = FloatField(min_value=0)

    class Meta:
        model = Work
        fields = ['id', 'title', 'price']


class ItemSerializer(ModelSerializer):
    price = FloatField(min_value=0)
    sell_price = FloatField(min_value=0)

    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'count', 'sell_price']


class UtilSerializer(ModelSerializer):
    price = FloatField(min_value=0)

    class Meta:
        model = Util
        fields = ['id', 'title', 'price', 'count']


class UserItemSerializer(ModelSerializer):
    id = IntegerField(source='item.id', read_only=True)
    title = CharField(source='item.title', read_only=True)
    price = CharField(source='item.price', read_only=True)

    class Meta:
        model = UserItem
        fields = ['id', 'title', 'price', 'count']


class UserUtilSerializer(ModelSerializer):
    id = IntegerField(source='util.id', read_only=True)
    title = CharField(source='util.title', read_only=True)
    price = CharField(source='util.price', read_only=True)

    class Meta:
        model = UserItem
        fields = ['id', 'title', 'price', 'count']


class SupplySerializer(Serializer):
    count = IntegerField(min_value=0)

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class AffordSerializer(Serializer):
    count = IntegerField(min_value=0)
    user = PrimaryKeyRelatedField(queryset=get_user_model().objects.filter(is_agent_account=True))

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
