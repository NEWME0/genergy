from django.db.models import *


class Contract(Model):
    """
        Обьекты.
    """

    is_active = BooleanField(default=True)

    title = CharField(max_length=255)
    description = CharField(max_length=1023)
