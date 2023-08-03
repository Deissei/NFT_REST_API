from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from apps.collections_nft.models import CollectionNFT, PreviousPrice
from apps.collections_nft.serializers import (CollectionNftLISTSerializer,
                                              CollectionNFTSerializer)
from apps.transactions.models import Transaction

from utils.permissions import IsCollectionNFTOwner


class CollectionNFTAPIViewSet(viewsets.ModelViewSet):
    queryset = CollectionNFT.objects.all()
    serializer_class = CollectionNFTSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'destroy'):
            return [IsCollectionNFTOwner()]
        if self.action in ('purchase', ):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author, owner=author)

    def get_serializer_class(self):
        if self.action == 'list':
            return CollectionNftLISTSerializer
        return CollectionNFTSerializer
    
    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        collections = self.get_object()
        user = request.user
        
        if user is None:
            raise ValidationError("Пользователь не аутентифицирован. Войдите в систему.")
    
        if user.balance < collections.price:
            raise ValidationError("У вас недостаточно средств!")
        
        transaction_check_buyer = Transaction.objects.create(
            collection_nft_id=collections, 
            buyer_id=user, 
            seller_id=collections.owner, 
            price=collections.price, 
            transaction_type='Покупка', 
            status='В ожидании'
        )
        
        user.balance -= collections.price
        user.save()
        
        collections.owner = user
        collections.save()
        
        transaction_check_buyer.status = "Успешно завершено"
        transaction_check_buyer.save()
        
        return Response({'message': "Покупка прошла успешно"})
