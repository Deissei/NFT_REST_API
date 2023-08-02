from rest_framework import serializers

from apps.cart.models import Cart, CartItemNft


class CartItemNftSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CartItemNft
        fields = (
            'id',
            'nft',
            'count',
            'created_at',
        )
        read_only_fields = (
            'id',
        )


class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = (
            'id',
            'items',
        )
