from rest_framework.routers import DefaultRouter

from app_contracts.views import ContractViewSet


router = DefaultRouter()
router.register('contract', ContractViewSet, basename='contract')

urlpatterns = router.urls
