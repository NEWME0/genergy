from rest_framework.routers import DefaultRouter

from app_inventory.views import MaterialViewSet, InstrumentViewSet

router = DefaultRouter()
router.register('instrument', InstrumentViewSet, basename='instrument')
router.register('material', MaterialViewSet, basename='material')
urlpatterns = router.get_urls()
