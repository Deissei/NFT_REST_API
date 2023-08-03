from rest_framework import serializers

from apps.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = (
            'id',
            'nft_id',
            'buyer_id',
            'seller_id',
            'price',
            'transaction_date',
            'transaction_type',
            'status',
        )