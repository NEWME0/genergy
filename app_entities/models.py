from django.db.models import CharField, FloatField, CheckConstraint, Q

from common.models import BaseModel


class Item(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='item_price', check=Q(price__gte=0))
        ]


class Util(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='util_price', check=Q(price__gte=0))
        ]


class Work(BaseModel):
    title = CharField(max_length=255)
    price = FloatField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(name='work_price', check=Q(price__gte=0))
        ]
