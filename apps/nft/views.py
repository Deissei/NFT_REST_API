from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from apps.nft.models import Nft
from apps.nft.serializers import NftLISTSerializer, NftSerializer
from utils.filters import NftPriceFilter
from utils.permissions import IsCollectionNFTOwner


class NftAPIViewSet(viewsets.ModelViewSet):
    queryset = Nft.objects.all()
    serializer_class = NftSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ("title", "author__username", "collection_id__title")
    filterset_class = NftPriceFilter

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
