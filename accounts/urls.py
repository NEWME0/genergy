from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')

urlpatterns = router.get_urls()
