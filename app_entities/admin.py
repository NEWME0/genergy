from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_entities.models import Item, Util, Work


@admin.register(Item)
class ItemAdmin(ModelAdmin):
    pass


@admin.register(Util)
class UtilAdmin(ModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(ModelAdmin):
    pass
