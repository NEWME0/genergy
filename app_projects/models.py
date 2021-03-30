from datetime import timedelta

from django.db.models import *
from django.db.models.aggregates import Sum
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from app_entities.models import Item, Work
from common.models import BaseModel

User = get_user_model()


class ProjectExercise(BaseModel):
    project = ForeignKey(to='Project', on_delete=CASCADE, related_name='exercises')
    work = ForeignKey(to=Work, on_delete=PROTECT)
    count = PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'work'], name='project_exercise_unique'),
        ]


class ProjectMaterial(BaseModel):
    project = ForeignKey(to='Project', on_delete=CASCADE, related_name='materials')
    item = ForeignKey(to=Item, on_delete=PROTECT)
    count = PositiveIntegerField(default=1)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'item'], name='project_material_unique')
        ]


class ProjectExecutor(BaseModel):
    project = ForeignKey(to='Project', on_delete=CASCADE, related_name='executors')
    user = ForeignKey(to=User, on_delete=PROTECT)
    hours = DurationField(default=timedelta)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'user'], name='project_executor_unique'),
            CheckConstraint(check=Q(hours__gte=timedelta()), name='project_executor_hours'),
        ]


class ProjectState(TextChoices):
    OPEN = 'OPEN', _('Open')
    DONE = 'DONE', _('Done')
    HOLD = 'HOLD', _('Hold')


class ProjectQuerySet(QuerySet):
    def with_totals(self):
        exercises_total_price = ProjectExercise.objects.filter(project=OuterRef('id')).values('project').annotate(
            total=Sum(ExpressionWrapper(F('count') * F('work__price'), output_field=FloatField()))
        ).values('total')

        materials_total_price = ProjectMaterial.objects.filter(project=OuterRef('id')).values('project').annotate(
            total=Sum(ExpressionWrapper(F('count') * F('item__price'), output_field=FloatField()))
        ).values('total')

        executors_total_hours = ProjectExecutor.objects.filter(project=OuterRef('id')).values('project').annotate(
            total=Sum('hours')
        ).values('total')

        return self.order_by().annotate(
            exercises_total_price=Subquery(exercises_total_price),
            materials_total_price=Subquery(materials_total_price),
            executors_total_hours=Subquery(executors_total_hours),
        )


class Project(BaseModel):
    objects = ProjectQuerySet.as_manager()

    title = CharField(max_length=255, unique=True)
    state = CharField(max_length=15, choices=ProjectState.choices, default=ProjectState.HOLD)
    owner = ForeignKey(to=User, on_delete=PROTECT, related_name='own_projects')

    prepaid = FloatField(default=0)
    discount = IntegerField(default=0)
    date_ending = DateTimeField(default=None, null=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(state__in=ProjectState.values), name='project_check_state'),
            CheckConstraint(check=Q(discount__gte=0, discount__lte=100), name='project_check_discount'),
            CheckConstraint(check=Q(prepaid__gte=0), name='project_check_prepaid'),
        ]
