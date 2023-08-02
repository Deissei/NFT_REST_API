from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions
from rest_framework.mixins import (
    RetrieveModelMixin,
)

from apps.cart.serializers import CartSerializer

from apps.cart.models import Cart


class CartViewSet(
    RetrieveModelMixin,
    GenericViewSet,
):
    def get_queryset(self):
        cart = Cart.objects.filter(user=self.request.user)
        return cart
    
    basename = 'cart'
    
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
