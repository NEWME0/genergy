from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from app_accounts.views import UserViewSet
from app_entities.views import UserItemViewSet, UserUtilViewSet, UserOwnProjectViewSet

app_router = DefaultRouter()
app_router.register('users', UserViewSet, basename='user')

user_router = NestedDefaultRouter(app_router, r'users', lookup='user')
user_router.register('items', UserItemViewSet, basename='user_item')
user_router.register('utils', UserUtilViewSet, basename='user_util')
user_router.register('own_projects', UserOwnProjectViewSet, basename='user_own_project')

urlpatterns = [
    path('', include(app_router.urls)),
    path('', include(user_router.urls)),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/verify', TokenVerifyView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
]
