from rest_framework.fields import FloatField, DurationField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from app_accounts.models import User
from app_entities.models import Work, Item
from app_projects.models import Project, ProjectExercise, ProjectExecutor, ProjectMaterial


def discounted(price: float, discount: int) -> float:
    return (price * (100 - discount)) / 100


class ProjectWorkSerializer(ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'title', 'price']


class ProjectItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price']


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
        data['work'] = ProjectWorkSerializer().to_representation(instance.work)
        return data

    class Meta:
        model = ProjectExercise
        fields = ['id', 'project', 'work', 'count', 'total_price', 'final_price']
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

    def to_representation(self, instance: ProjectMaterial):
        data = super(ProjectMaterialSerializer, self).to_representation(instance)
        data['user'] = ProjectItemSerializer().to_representation(instance.item)
        return data

    class Meta:
        model = ProjectMaterial
        fields = ['id', 'project', 'item', 'count', 'total_price', 'final_price']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectExecutorSerializer(ModelSerializer):
    def to_representation(self, instance: ProjectExecutor):
        data = super(ProjectExecutorSerializer, self).to_representation(instance)
        data['user'] = ProjectUserSerializer().to_representation(instance.user)
        return data

    class Meta:
        model = ProjectExecutor
        fields = ['id', 'project', 'user', 'hours']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectSerializer(ModelSerializer):
    exercises = ProjectExerciseSerializer(many=True, default=[])
    executors = ProjectExecutorSerializer(many=True, default=[])
    materials = ProjectMaterialSerializer(many=True, default=[])

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

    def to_representation(self, instance: Project):
        data = super(ProjectSerializer, self).to_representation(instance)
        data['owner'] = ProjectUserSerializer().to_representation(instance.owner)
        return data

    class Meta:
        model = Project
        exclude = ['deleted_at']

    def create(self, validated_data: dict):
        exercises_data = validated_data.pop('exercises', [])
        executors_data = validated_data.pop('executors', [])
        materials_data = validated_data.pop('materials', [])

        # Create project
        instance: Project = super(ProjectSerializer, self).create(validated_data)

        # Create list of exercises
        exercises = [ProjectExercise(project=instance, **data) for data in exercises_data]
        instance.exercises.bulk_create(exercises)

        # Create list of executors
        executors = [ProjectExecutor(project=instance, **data) for data in executors_data]
        instance.executors.bulk_create(executors)

        # Create list of materials
        materials = [ProjectMaterial(project=instance, **data) for data in materials_data]
        instance.materials.bulk_create(materials)

        return instance

    def update(self, instance: Project, validated_data: dict):
        exercises_data = validated_data.pop('exercises', [])
        executors_data = validated_data.pop('executors', [])
        materials_data = validated_data.pop('materials', [])

        # Todo: update related
        print(exercises_data)
        print(executors_data)
        print(materials_data)

        # Update project
        instance: Project = super(ProjectSerializer, self).update(instance, validated_data)

        return instance
