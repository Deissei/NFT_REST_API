from django.contrib.auth import get_user_model
from django.db import models

from apps.nft.models import Nft
from apps.collections_nft.models import CollectionNFT

User = get_user_model()


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('Покупка', 'Покупка'),
        ('Продажа', 'Продажа'),
    ] 
    STATUS_CHOICES = [
        ('В ожидании', 'В ожидании'),
        ('Успешно завершено', 'Успешно завершено'),
    ]

    nft_id = models.ForeignKey(
        Nft,
        on_delete=models.CASCADE,
        related_name="transaction_nft",
        null=True,
        blank=True,
    )
    collection_nft_id = models.ForeignKey(
        CollectionNFT,
        on_delete=models.CASCADE,
        related_name="transaction_collections",
        null=True,
        blank=True,
    )
    buyer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transaction_buyer",
    )
    seller_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transaction_seller",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    transaction_date = models.DateTimeField(
        auto_now_add=True,
    )
    transaction_type = models.CharField(
        max_length=7,
        choices=TRANSACTION_TYPE_CHOICES,
    )
    status = models.CharField(
        max_length=17,
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        return f"{self.status}"
    
    class Meta:
        ordering = ['-transaction_date']
    