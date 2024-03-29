# Generated by Django 3.1.5 on 2021-04-25 07:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_entities', '0006_auto_20210420_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserItemSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supply_set', to='app_entities.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_supply_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='UserUtilSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('count', models.PositiveIntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='util_supply_set', to=settings.AUTH_USER_MODEL)),
                ('util', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supply_set', to='app_entities.util')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='utilsupply',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='utilsupply',
            name='util',
        ),
        migrations.DeleteModel(
            name='ItemSupply',
        ),
        migrations.DeleteModel(
            name='UtilSupply',
        ),
    ]
