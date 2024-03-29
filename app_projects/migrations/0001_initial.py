# Generated by Django 3.1.5 on 2021-02-24 20:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_entities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('ACTIVE', 'Active'), ('CLOSED', 'Closed'), ('SKETCH', 'Sketch')], default='SKETCH', max_length=15)),
                ('prepaid', models.FloatField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='own_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_entities.item')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='app_projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.PositiveIntegerField(default=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='app_projects.project')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_entities.work')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectExecutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hours', models.DurationField(default=datetime.timedelta)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executors', to='app_projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='projectmaterial',
            constraint=models.UniqueConstraint(fields=('project', 'item'), name='project_material_unique'),
        ),
        migrations.AddConstraint(
            model_name='projectexercise',
            constraint=models.UniqueConstraint(fields=('project', 'work'), name='project_exercise_unique'),
        ),
        migrations.AddConstraint(
            model_name='projectexecutor',
            constraint=models.UniqueConstraint(fields=('project', 'user'), name='project_executor_unique'),
        ),
        migrations.AddConstraint(
            model_name='projectexecutor',
            constraint=models.CheckConstraint(check=models.Q(hours__gte=datetime.timedelta(0)), name='project_executor_hours'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.CheckConstraint(check=models.Q(state__in=['ACTIVE', 'CLOSED', 'SKETCH']), name='project_check_state'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.CheckConstraint(check=models.Q(('discount__gte', 0), ('discount__lte', 100)), name='project_check_discount'),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.CheckConstraint(check=models.Q(prepaid__gte=0), name='project_check_prepaid'),
        ),
    ]
