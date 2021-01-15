from django.db.models import *

from app_deposit.models import Consumable, Instrument


class ServiceConsumable(Model):
    """ Расходники (материалы) используемые для выполнения одной работы. """

    consumable = ForeignKey(to=Consumable, on_delete=CASCADE)
    service = ForeignKey(to='Service', on_delete=CASCADE)
    count = PositiveIntegerField()


class ServiceInstrument(Model):
    """ Интсрументы используемые при выполнении одной работы. """

    instrument = ForeignKey(to=Instrument, on_delete=CASCADE)
    service = ForeignKey(to='Service', on_delete=CASCADE)
    count = PositiveIntegerField()


class Service(Model):
    """ Тип работ. """

    title = CharField(max_length=255, unique=True)

    consumables = ManyToManyField(to=Consumable, through=ServiceConsumable, through_fields=['service', 'consumable'])
    instruments = ManyToManyField(to=Instrument, through=ServiceInstrument, through_fields=['service', 'instrument'])
