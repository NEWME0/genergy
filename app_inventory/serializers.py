from rest_framework.fields import IntegerField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from app_inventory.models import Material, Instrument


class MaterialSerializer(ModelSerializer):
    count = IntegerField(min_value=0)
    price = IntegerField(min_value=0)

    class Meta:
        model = Material
        exclude = ['polymorphic_ctype']


class MaterialListSerializer(MaterialSerializer):
    detail = HyperlinkedIdentityField(view_name='material-detail')

    class Meta(MaterialSerializer.Meta):
        pass


class InstrumentSerializer(ModelSerializer):
    count = IntegerField(min_value=0)
    price = IntegerField(min_value=0)

    class Meta:
        model = Instrument
        exclude = ['polymorphic_ctype']


class InstrumentListSerializer(InstrumentSerializer):
    detail = HyperlinkedIdentityField(view_name='instrument-detail')

    class Meta(InstrumentSerializer.Meta):
        pass
