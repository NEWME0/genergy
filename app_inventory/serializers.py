from rest_framework.fields import IntegerField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from app_inventory.models import Material, Instrument, UserMaterial, UserInstrument


class UserMaterialSerializer(ModelSerializer):
    class Meta:
        model = UserMaterial
        fields = '__all__'


class MaterialSerializer(ModelSerializer):
    count = IntegerField(min_value=0)
    price = IntegerField(min_value=0)
    users = UserMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        exclude = ['polymorphic_ctype']


class MaterialListSerializer(MaterialSerializer):
    detail = HyperlinkedIdentityField(view_name='material-detail')

    class Meta(MaterialSerializer.Meta):
        pass


class UserInstrumentSerializer(ModelSerializer):
    class Meta:
        model = UserInstrument
        fields = '__all__'


class InstrumentSerializer(ModelSerializer):
    count = IntegerField(min_value=0)
    price = IntegerField(min_value=0)
    users = UserInstrumentSerializer(many=True, read_only=True)

    class Meta:
        model = Instrument
        exclude = ['polymorphic_ctype']


class InstrumentListSerializer(InstrumentSerializer):
    detail = HyperlinkedIdentityField(view_name='instrument-detail')

    class Meta(InstrumentSerializer.Meta):
        pass
