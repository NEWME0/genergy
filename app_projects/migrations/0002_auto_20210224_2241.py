# Generated by Django 3.1.5 on 2021-02-24 20:41

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='project',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='projectexecutor',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='projectexercise',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='projectmaterial',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projectexecutor',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projectexercise',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projectmaterial',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]