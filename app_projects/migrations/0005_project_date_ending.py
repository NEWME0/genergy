# Generated by Django 3.1.5 on 2021-03-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0004_auto_20210317_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_ending',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
