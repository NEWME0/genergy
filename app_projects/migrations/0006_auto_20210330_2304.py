# Generated by Django 3.1.5 on 2021-03-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0005_project_date_ending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
