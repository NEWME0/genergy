from django.db.models import *
from django.core.exceptions import ValidationError
from polymorphic.models import PolymorphicModel


class Entry(PolymorphicModel):
    """ Обьекты склада. """

    title = CharField(max_length=255, unique=True)


class Stock(Model):
    """ Обьекты на складе. """

    entry = ForeignKey(to=Entry, on_delete=PROTECT)
    count = PositiveIntegerField()
    price = FloatField()


class Instrument(Entry):
    """ Интструменты. Тип обьектов склада. """


class Consumable(Entry):
    """ Расходники (материалы). Тип обьектов склада. """
