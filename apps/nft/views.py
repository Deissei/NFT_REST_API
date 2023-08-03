from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from apps.nft.models import Nft
from apps.nft.serializers import NftLISTSerializer, NftSerializer
from apps.transactions.models import Transaction

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
        if self.action in ('purchase', ):
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user, author=user)
        return serializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return NftLISTSerializer
        return NftSerializer
    
    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        nft = self.get_object()
        user = request.user
        
        if user is None:
            raise ValidationError("Пользователь не аутентифицирован. Войдите в систему.")
    
        if user.balance < nft.price:
            raise ValidationError("У вас недостаточно средств!")
        
        transaction_check_buyer = Transaction.objects.create(
            nft_id=nft, 
            buyer_id=user, 
            seller_id=nft.owner, 
            price=nft.price, 
            transaction_type='Покупка', 
            status='В ожидании'
        )
        
        user.balance -= nft.price
        user.save()
        
        nft.owner = user
        nft.save()
        
        transaction_check_buyer.status = "Успешно завершено"
        transaction_check_buyer.save()  
        
        return Response({'message': "Покупка прошла успешно"})
