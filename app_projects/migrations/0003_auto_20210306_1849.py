# Generated by Django 3.1.5 on 2021-03-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0002_auto_20210224_2241'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='project',
            name='project_check_state',
        ),
        migrations.AlterField(
            model_name='project',
            name='state',
            field=models.CharField(choices=[('OPEN', 'Open'), ('DONE', 'Done'), ('HOLD', 'Hold')], default='HOLD', max_length=15),
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.CheckConstraint(check=models.Q(state__in=['OPEN', 'DONE', 'HOLD']), name='project_check_state'),
        ),
    ]
