from django.db.models import *
from django.contrib.auth import get_user_model


class Item(Model):
    user = ForeignKey(to=get_user_model(), related_name='items', on_delete=CASCADE)
    title = CharField(max_length=100)
