from rest_framework import permissions, viewsets

from apps.nft.models import Nft
from apps.nft.serializers import NftSerializer, NftLISTSerializer
from utils.permissions import IsCollectionNFTOwner


class NftAPIViewSet(viewsets.ModelViewSet):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer

    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            return [IsCollectionNFTOwner()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user, author=user)
        return serializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return NftLISTSerializer
        return NftSerializer
