from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_entities.views import ItemViewSet, UtilViewSet, WorkViewSet, ItemSupplyViewSet, UtilSupplyViewSet

app_router = DefaultRouter()
app_router.register('items/supply', ItemSupplyViewSet, basename='item-supply')
app_router.register('utils/supply', UtilSupplyViewSet, basename='item-supply')
app_router.register('items', ItemViewSet, basename='item')
app_router.register('utils', UtilViewSet, basename='util')
app_router.register('works', WorkViewSet, basename='work')

urlpatterns = [
    path('', include(app_router.urls)),
]
