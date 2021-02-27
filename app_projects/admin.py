from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app_projects.models import Project


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    pass
