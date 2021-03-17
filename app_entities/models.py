from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import CharField, FloatField, ForeignKey, PositiveIntegerField
from django.db.models.deletion import PROTECT
from django.db.models.query_utils import Q
from django.db.models.constraints import CheckConstraint, UniqueConstraint

from common.models import BaseModel


User = get_user_model()


class Work(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='work_price', check=Q(price__gte=0))
        ]


class Item(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)
    count = PositiveIntegerField(default=0)
    sell_price = FloatField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='item_price', check=Q(price__gte=0)),
            CheckConstraint(name='item_sell_price', check=Q(price__gte=0))
        ]

    def supply(self, count: int):
        self.count += count
        self.save()

    def afford(self, count: int, user: User):
        user_item, created = UserItem.objects.get_or_create(user=user, item=self)
        user_item.count += count
        self.count -= count

        with transaction.atomic():
            user_item.save()
            self.save()


class Util(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)
    count = PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='util_price', check=Q(price__gte=0))
        ]

    def supply(self, count: int):
        self.count += count
        self.save()

    def afford(self, count: int, user: User):
        user_item, created = UserUtil.objects.get_or_create(user=user, util=self)
        user_item.count += count
        self.count -= count

        with transaction.atomic():
            user_item.save()
            self.save()


class UserItem(BaseModel):
    item = ForeignKey(to=Item, on_delete=PROTECT, related_name='in_use')
    user = ForeignKey(to=User, on_delete=PROTECT, related_name='items')
    count = PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(name='unique_user_item', fields=['item', 'user'])
        ]


class UserUtil(BaseModel):
    util = ForeignKey(to=Util, on_delete=PROTECT, related_name='in_use')
    user = ForeignKey(to=User, on_delete=PROTECT, related_name='utils')
    count = PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(name='unique_user_util', fields=['util', 'user'])
        ]
