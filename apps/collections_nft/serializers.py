from rest_framework import serializers

from apps.collections_nft.models import CollectionNFT
from apps.users.serializers import UserSerializer
from apps.collections_nft.models import PreviousPrice


class PerviousPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousPrice
        fields = (
            'id',
            'created_at',
            'previous_price',
        )


class CollectionNFTSerializer(serializers.ModelSerializer):
    previous_prices = PerviousPriceSerializer(many=True, read_only=True)
    class Meta:
        model = CollectionNFT
        fields = (
            'id',
            'title',
            'description',
            'image',
            'external_link',
            'previous_prices',
            'price',
            'author',
            'owner',
            'created_at',
            'nft_collections',
        )
        read_only_fields = (
            'author',
            'owner',
            'previous_prices',
            'nft_collections',
        )
    
    def update(self, instance, validated_data):
        new_price = validated_data.get('price')

        if new_price is not None and new_price != instance.price:
            previous_prices = instance.previous_prices.all()
            previous_price = PreviousPrice.objects.create(previous_price=instance.price)
            instance.previous_prices.add(previous_price)

            instance.price = new_price
            instance.save()

        return instance
