from rest_framework.routers import DefaultRouter

from apps.nft.views import NftAPIViewSet

router = DefaultRouter()

router.register('', NftAPIViewSet)

urlpatterns = router.urls
