from rest_framework.fields import FloatField, DurationField
from rest_framework.serializers import ModelSerializer

from app_projects.models import Project, ProjectExercise, ProjectExecutor, ProjectMaterial


class ProjectExerciseSerializer(ModelSerializer):
    class Meta:
        model = ProjectExercise
        fields = ['id', 'project', 'work', 'count']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectExecutorSerializer(ModelSerializer):
    class Meta:
        model = ProjectExecutor
        fields = ['id', 'project', 'user', 'hours']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectMaterialSerializer(ModelSerializer):
    class Meta:
        model = ProjectMaterial
        fields = ['id', 'project', 'item', 'count']
        extra_kwargs = {
            'project': {'read_only': True}
        }


class ProjectSerializer(ModelSerializer):
    exercises = ProjectExerciseSerializer(many=True, default=[])
    executors = ProjectExecutorSerializer(many=True, default=[])
    materials = ProjectMaterialSerializer(many=True, default=[])

    total_price = FloatField(read_only=True)
    materials_total_price = FloatField(read_only=True)
    exercises_total_price = FloatField(read_only=True)
    executors_total_hours = DurationField(read_only=True)

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
