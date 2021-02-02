from django.db.models import CharField, IntegerField
from polymorphic.models import PolymorphicModel


class InventoryItem(PolymorphicModel):
    title = CharField(max_length=100)
    count = IntegerField()
    price = IntegerField()


class Instrument(InventoryItem):
    """
        Instruments
    """


class Material(InventoryItem):
    """
        Materials
    """
