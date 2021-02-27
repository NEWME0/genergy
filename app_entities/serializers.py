from rest_framework.fields import FloatField
from rest_framework.serializers import ModelSerializer

from app_entities.models import Item, Util, Work


class ItemSerializer(ModelSerializer):
    price = FloatField(min_value=0)

    class Meta:
        model = Item
        fields = ['id', 'title', 'price']


class UtilSerializer(ModelSerializer):
    price = FloatField(min_value=0)

    class Meta:
        model = Util
        fields = ['id', 'title', 'price']


class WorkSerializer(ModelSerializer):
    price = FloatField(min_value=0)

    class Meta:
        model = Work
        fields = ['id', 'title', 'price']
