from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app_accounts.views import UserViewSet


app_router = DefaultRouter()
app_router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(app_router.urls))
]
