from datetime import timedelta

from django.db.models import *
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from app_entities.models import Item, Work
from common.models import BaseModel

User = get_user_model()


class ProjectState(TextChoices):
    ACTIVE = 'ACTIVE', _('Active')
    CLOSED = 'CLOSED', _('Closed')
    SKETCH = 'SKETCH', _('Sketch')


class Project(BaseModel):
    title = CharField(max_length=255)
    state = CharField(max_length=15, choices=ProjectState.choices, default=ProjectState.SKETCH)
    owner = ForeignKey(to=User, on_delete=PROTECT, related_name='own_projects')

    prepaid = FloatField(default=0)
    discount = IntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(state__in=ProjectState.values), name='project_check_state'),
            CheckConstraint(check=Q(discount__gte=0, discount__lte=100), name='project_check_discount'),
            CheckConstraint(check=Q(prepaid__gte=0), name='project_check_prepaid'),
        ]


class ProjectExercise(BaseModel):
    project = ForeignKey(to=Project, on_delete=CASCADE, related_name='exercises')
    work = ForeignKey(to=Work, on_delete=PROTECT)
    count = PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'work'], name='project_exercise_unique'),
        ]


class ProjectExecutor(BaseModel):
    project = ForeignKey(to=Project, on_delete=CASCADE, related_name='executors')
    user = ForeignKey(to=User, on_delete=PROTECT)
    hours = DurationField(default=timedelta)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'user'], name='project_executor_unique'),
            CheckConstraint(check=Q(hours__gte=timedelta()), name='project_executor_hours'),
        ]


class ProjectMaterial(BaseModel):
    project = ForeignKey(to=Project, on_delete=CASCADE, related_name='materials')
    item = ForeignKey(to=Item, on_delete=PROTECT)
    count = PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'item'], name='project_material_unique')
        ]