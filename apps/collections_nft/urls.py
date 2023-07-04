from rest_framework.routers import DefaultRouter

from apps.collections_nft.views import CollectionNFTAPIViewSet

router = DefaultRouter()

router.register('', CollectionNFTAPIViewSet)

urlpatterns = [
    
] + router.urls
