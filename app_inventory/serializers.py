from rest_framework.serializers import ModelSerializer

from app_inventory.models import Material, Instrument


class MaterialSerializer(ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class InstrumentSerializer(ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'
