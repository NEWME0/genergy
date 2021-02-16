from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=100)


class Cost(models.Model):
    title = models.CharField(max_length=100)


def pre_save_record(sender, instance, **kwargs):
    print('Hello')

    if hasattr(instance, 'cost'):
        instance.cost.title = instance.cost.title + '  updated'
        instance.cost.save()
    else:
        instance.cost = Cost(title='Created')
        instance.cost.save()


models.signals.post_save.connect(pre_save_record, sender=Record)
