from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from app_accounts.views import UserViewSet
from app_entities.views import UserItemViewSet, UserUtilViewSet
from app_projects.views import UserOwnProjectViewSet, UserExeProjectViewSet

app_router = DefaultRouter()
app_router.register('users', UserViewSet, basename='user')

user_router = NestedDefaultRouter(app_router, r'users', lookup='user')
user_router.register('own-projects', UserOwnProjectViewSet, basename='user-own-project')
user_router.register('exe-projects', UserExeProjectViewSet, basename='user-exe-project')
user_router.register('items', UserItemViewSet, basename='user-item')
user_router.register('utils', UserUtilViewSet, basename='user-util')

urlpatterns = [
    path('', include(app_router.urls)),
    path('', include(user_router.urls)),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/verify', TokenVerifyView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
]
