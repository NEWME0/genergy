from django.utils import timezone
from django.db.models import Model, DateTimeField

from common.manages import BaseManager


class BaseModel(Model):
    all_objects = BaseManager(with_deleted=True)
    objects = BaseManager(with_deleted=False)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(null=True)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        return super(BaseModel, self).delete(using=using, keep_parents=keep_parents)
