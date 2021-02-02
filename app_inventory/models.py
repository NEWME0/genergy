from django.contrib.auth import get_user_model
from django.db.models import CharField, Model, ForeignKey, CASCADE, PositiveIntegerField
from polymorphic.models import PolymorphicModel


class InventoryItem(PolymorphicModel):
    title = CharField(max_length=100)
    count = PositiveIntegerField()
    price = PositiveIntegerField()


class Instrument(InventoryItem):
    """
        Instruments inventory.
    """


class Material(InventoryItem):
    """
        Materials inventory.
    """


class UserInstrument(Model):
    """
        User instrument inventory.
    """
    user = ForeignKey(to=get_user_model(), on_delete=CASCADE)
    item = ForeignKey(to=Instrument, on_delete=CASCADE)
    count = PositiveIntegerField()


class UserMaterial(Model):
    """
        User material inventory.
    """
    user = ForeignKey(to=get_user_model(), on_delete=CASCADE)
    item = ForeignKey(to=Material, on_delete=CASCADE)
    count = PositiveIntegerField()
