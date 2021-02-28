from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from app_accounts.views import UserViewSet


app_router = DefaultRouter()
app_router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(app_router.urls)),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/verify', TokenVerifyView.as_view()),
    path('auth/refresh', TokenRefreshView.as_view()),
]
