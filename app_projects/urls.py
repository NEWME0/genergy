from django.urls import path, include
from rest_framework_nested import routers

from app_projects.views import ProjectViewSet, \
    ProjectExerciseViewSet, ProjectExecutorViewSet, ProjectMaterialViewSet

app_router = routers.DefaultRouter()
app_router.register(r'projects', ProjectViewSet)

project_router = routers.NestedDefaultRouter(app_router, r'projects', lookup='project')
project_router.register(r'exercises', ProjectExerciseViewSet, basename='project-exercise')
project_router.register(r'executors', ProjectExecutorViewSet, basename='project-executor')
project_router.register(r'materials', ProjectMaterialViewSet, basename='project-material')


urlpatterns = [
    path('', include(app_router.urls)),
    path('', include(project_router.urls)),
]
