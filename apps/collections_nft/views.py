from rest_framework import permissions, viewsets

from apps.collections_nft.models import CollectionNFT, PreviousPrice
from apps.collections_nft.serializers import CollectionNFTSerializer, CollectionNftLISTSerializer
from utils.permissions import IsCollectionNFTOwner


class CollectionNFTAPIViewSet(viewsets.ModelViewSet):
    queryset = CollectionNFT.objects.all()
    serializer_class = CollectionNFTSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            return [IsCollectionNFTOwner()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author, owner=author)

    def get_serializer_class(self):
        if self.action == 'list':
            return CollectionNftLISTSerializer
        return CollectionNFTSerializer
