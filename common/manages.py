from django.utils import timezone
from django.db.models import QuerySet, Manager


class BaseQuerySet(QuerySet):    
    def delete(self):
        return super(BaseQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        return super(BaseQuerySet, self).delete()


class BaseManager(Manager):
    def __init__(self, *args, with_deleted=False, **kwargs):
        super(BaseManager, self).__init__(*args, **kwargs)
        self.with_deleted = with_deleted

    def get_queryset(self):
        if self.with_deleted:
            return BaseQuerySet(self.model)
        else:
            return BaseQuerySet(self.model).filter(deleted_at__isnull=True)

    def hard_delete(self):
        return self.get_queryset().hard_delete()
