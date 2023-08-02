from rest_framework.routers import DefaultRouter

from apps.cart.views import CartViewSet

router = DefaultRouter()
router.register("", CartViewSet, basename='cart')

urlpatterns = router.urls
