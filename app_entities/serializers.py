from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.fields import FloatField
from rest_framework.serializers import ModelSerializer

from app_entities.models import Item, Util, Work, UserItem, UserUtil, UserItemSupply, UserUtilSupply


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
    class Meta:
        model = UserItem
        fields = ['item', 'user', 'count']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def validate(self, attrs):
        if not self.context['user'].is_agent_account:
            raise ValidationError(f"Items can be attached only to agent users.")

        if attrs['item'].count < attrs['count']:
            raise ValidationError(f"Item {attrs['item'].id} has not enough count ({attrs['item'].count}).")
        return attrs

    def save(self, **kwargs):
        user = self.context['user']
        item_id = self.validated_data['item']
        self.instance = self.instance or UserItem.objects.filter(user=user, item_id=item_id).first()
        return super(UserItemSerializer, self).save(**kwargs)

    @transaction.atomic()
    def create(self, validated_data):
        UserItemSupply.objects.create(user=self.context['user'], **validated_data)
        instance = UserItem.objects.create(user=self.context['user'], **validated_data)
        instance.item.count -= validated_data['count']
        instance.item.save()
        return instance

    @transaction.atomic()
    def update(self, instance, validated_data):
        UserItemSupply.objects.create(user=self.context['user'], **validated_data)
        instance.count += validated_data['count']
        instance.save()
        instance.item.count -= validated_data['count']
        instance.item.save()
        return instance

    def to_representation(self, instance):
        data = super(UserItemSerializer, self).to_representation(instance)
        data['item'] = ItemSerializer().to_representation(instance.item)
        return data


class UserUtilSerializer(ModelSerializer):
    class Meta:
        model = UserUtil
        fields = ['item', 'user', 'count']
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def validate(self, attrs):
        if not self.context['user'].is_agent_account:
            raise ValidationError(f"Utils can be attached only to agent users.")

        if attrs['util'].count < attrs['count']:
            raise ValidationError(f"Util {attrs['util'].id} has not enough count ({attrs['util'].count}).")
        return attrs

    def save(self, **kwargs):
        user = self.context['user']
        util_id = self.validated_data['util']
        self.instance = self.instance or UserUtil.objects.filter(user=user, util_id=util_id).first()
        return super(UserUtilSerializer, self).save(**kwargs)

    @transaction.atomic()
    def create(self, validated_data):
        UserUtilSupply.objects.create(user=self.context['user'], **validated_data)
        instance = UserUtil.objects.create(user=self.context['user'], **validated_data)
        instance.util.count -= validated_data['count']
        instance.util.save()
        instance.util.supply_set.create(user=self.context['user'], count=validated_data['count'])
        return instance

    @transaction.atomic()
    def update(self, instance, validated_data):
        UserUtilSupply.objects.create(user=self.context['user'], **validated_data)
        instance.count += validated_data['count']
        instance.save()
        instance.util.count -= validated_data['count']
        instance.util.save()
        return instance

    def to_representation(self, instance):
        data = super(UserUtilSerializer, self).to_representation(instance)
        data['util'] = UtilSerializer().to_representation(instance.util)
        return data
