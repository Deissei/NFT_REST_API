from rest_framework import serializers

from apps.collections_nft.models import CollectionNFT
from apps.users.serializers import UserSerializer


class CollectionNFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionNFT
        fields = (
            'id',
            'title',
            'description',
            'image',
            'external_link',
            'price',
            'author',
            'owner',
            'created_at',
        )
        read_only_fields = (
            'author',
            'owner',
        )
