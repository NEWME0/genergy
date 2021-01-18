from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from app_contracts.models import Contract


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
