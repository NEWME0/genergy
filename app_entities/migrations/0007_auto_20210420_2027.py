# Generated by Django 3.1.5 on 2021-04-20 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_entities', '0006_auto_20210420_2015'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='itemuserattachment',
            name='item_user_transaction',
        ),
    ]
