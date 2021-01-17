from django.contrib.auth import get_user_model
from django.db.models import *


class BaseModel(Model):
    """
        Base model.
    """

    date_created = DateTimeField(auto_now_add=True)
    date_updated = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
