from django.contrib.auth import get_user_model
from django.db.models import CharField, Model, ForeignKey, CASCADE, PositiveIntegerField, ManyToManyField
from polymorphic.models import PolymorphicModel


class InventoryItem(PolymorphicModel):
    title = CharField(max_length=100)
    count = PositiveIntegerField()
    price = PositiveIntegerField()


class Instrument(InventoryItem):
    """
        Instruments inventory.
    """
    users = ManyToManyField(to=get_user_model(), through='UserInstrument', through_fields=['item', 'user'])


class Material(InventoryItem):
    """
        Materials inventory.
    """
    users = ManyToManyField(to=get_user_model(), through='UserMaterial', through_fields=['item', 'user'])


class UserInstrument(Model):
    """
        User instrument inventory.
    """
    user = ForeignKey(to=get_user_model(), on_delete=CASCADE)
    item = ForeignKey(to=Instrument, on_delete=CASCADE)
    count = PositiveIntegerField()

    class Meta:
        unique_together = [['user', 'item']]


class UserMaterial(Model):
    """
        User material inventory.
    """
    user = ForeignKey(to=get_user_model(), on_delete=CASCADE)
    item = ForeignKey(to=Material, on_delete=CASCADE)
    count = PositiveIntegerField()

    class Meta:
        unique_together = [['user', 'item']]
