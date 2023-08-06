from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.nft.views import NftAPIViewSet

router = DefaultRouter()

router.register('', NftAPIViewSet)

urlpatterns = [
    path('nft/<int:pk>/purchase/', NftAPIViewSet.as_view({'post': "purchase"})),
    path('nft/<int:pk>/add_price_auction', NftAPIViewSet.as_view({'post': 'add_price_auction'}))
]

urlpatterns = router.urls
