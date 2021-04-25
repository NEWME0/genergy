from collections import OrderedDict
from typing import Union

from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.fields import FloatField, DurationField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from app_accounts.models import User
from app_projects.models import Project, ProjectExercise, ProjectExecutor, ProjectMaterial
from app_entities.serializers import WorkSerializer, ItemSerializer


def discounted(price: float, discount: int) -> float:
    return (price * (100 - discount)) / 100


class ProjectUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname']


class ProjectExerciseSerializer(ModelSerializer):
    total_price = SerializerMethodField()
    final_price = SerializerMethodField()

    @classmethod
    def get_total_price(cls, instance: ProjectExercise):
        return instance.count * instance.work.price

    @classmethod
    def get_final_price(cls, instance: ProjectExercise):
        return discounted(instance.count * instance.work.price, instance.project.discount)

    def to_representation(self, instance: ProjectExercise):
        data = super(ProjectExerciseSerializer, self).to_representation(instance)
        data['work'] = WorkSerializer().to_representation(instance.work)
        return data

    @transaction.atomic()
    def create(self, validated_data):
        instance, created = ProjectExercise.objects.get_or_create(
            project=self.context['project'],
            work=validated_data['work']
        )
        instance.count += validated_data['count']
        instance.save()
        return instance

    class Meta:
        model = ProjectExercise
        fields = ['project', 'work', 'count', 'total_price', 'final_price']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectMaterialSerializer(ModelSerializer):
    total_price = SerializerMethodField()
    final_price = SerializerMethodField()

    @classmethod
    def get_total_price(cls, instance: ProjectMaterial):
        return instance.count * instance.item.price

    @classmethod
    def get_final_price(cls, instance: ProjectMaterial):
        return discounted(instance.count * instance.item.price, instance.project.discount)

    def validate(self, attrs):
        user_attachment = attrs['item'].user_attachment.filter(user=self.context['user']).first()
        if getattr(user_attachment, 'count', 0) < attrs['count']:
            raise ValidationError('Not enough items.')
        return attrs

    def to_representation(self, instance: Union[ProjectMaterial, OrderedDict]):
        if isinstance(instance, OrderedDict):
            instance = self.Meta.model.objects.get(
                project=self.context['project'],
                user=self.context['user'],
                item=instance['item'],
            )

        data = super(ProjectMaterialSerializer, self).to_representation(instance)
        item = getattr(instance, 'item', None)
        data['item'] = ItemSerializer().to_representation(item)
        return data

    @transaction.atomic()
    def create(self, validated_data):
        instance, created = ProjectMaterial.objects.get_or_create(
            project=self.context['project'],
            user=self.context['user'],
            item=validated_data['item']
        )
        instance.count += validated_data['count']
        instance.save()
        user_attachment = instance.item.user_attachment.get(user=self.context['user'])
        user_attachment.count -= validated_data['count']
        user_attachment.save()
        return instance

    class Meta:
        model = ProjectMaterial
        fields = ['project', 'item', 'user', 'count', 'total_price', 'final_price']
        extra_kwargs = {
            'project': {'read_only': True},
            'user': {'read_only': True}
        }


class ProjectExecutorSerializer(ModelSerializer):
    def to_representation(self, instance: Union[ProjectExecutor, OrderedDict]):
        data = super(ProjectExecutorSerializer, self).to_representation(instance)
        user = getattr(instance, 'user', None) or instance['user']
        data['user'] = ProjectUserSerializer().to_representation(user)
        return data

    @transaction.atomic()
    def create(self, validated_data):
        instance, created = ProjectExecutor.objects.get_or_create(
            project=self.context['project'],
            user=validated_data['user']
        )
        instance.hours += validated_data['hours']
        instance.save()
        return instance

    class Meta:
        model = ProjectExecutor
        fields = ['project', 'user', 'hours']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectSerializer(ModelSerializer):
    exercises = ProjectExerciseSerializer(many=True, default=[], read_only=True)
    executors = ProjectExecutorSerializer(many=True, default=[], read_only=True)
    materials = ProjectMaterialSerializer(many=True, default=[], read_only=True)

    materials_total_price = FloatField(read_only=True)
    exercises_total_price = FloatField(read_only=True)
    executors_total_hours = DurationField(read_only=True)

    total_price = SerializerMethodField()
    final_price = SerializerMethodField()
    materials_final_price = SerializerMethodField()
    exercises_final_price = SerializerMethodField()

    @classmethod
    def get_materials_final_price(cls, instance: Project):
        if hasattr(instance, 'materials_total_price'):
            return discounted(instance.materials_total_price, instance.discount)

    @classmethod
    def get_exercises_final_price(cls, instance: Project):
        if hasattr(instance, 'exercises_total_price'):
            return discounted(instance.exercises_total_price, instance.discount)

    @classmethod
    def get_total_price(cls, instance: Project):
        if hasattr(instance, 'exercises_total_price') and hasattr(instance, 'materials_total_price'):
            return instance.exercises_total_price + instance.materials_total_price

    @classmethod
    def get_final_price(cls, instance: Project):
        if hasattr(instance, 'exercises_total_price') and hasattr(instance, 'materials_total_price'):
            return discounted(instance.exercises_total_price + instance.materials_total_price, instance.discount)

    def create(self, validated_data):
        validated_data['owner'] = self.context['owner']
        return super(ProjectSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        validated_data['owner'] = instance.owner
        return super(ProjectSerializer, self).update(instance, validated_data)

    def to_representation(self, instance: Project):
        data = super(ProjectSerializer, self).to_representation(instance)
        data['owner'] = ProjectUserSerializer().to_representation(instance.owner)
        return data

    class Meta:
        model = Project
        exclude = ['deleted_at']
        extra_kwargs = {
            'owner': {'read_only': True}
        }
