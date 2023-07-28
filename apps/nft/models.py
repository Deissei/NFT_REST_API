from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.collections_nft.models import CollectionNFT

User = get_user_model()


class Nft(models.Model):
    BLOCKCHAIN_CHOICES = [
        ("ETH", "Ethereum"),
    ]
    STATUS_CHOICES = [
        ("Available", "available"),
        ("Available", "available"),
    ]

    title = models.CharField(
        max_length=256,
    )
    image = models.ImageField(
        upload_to='nft',
        blank=True,
        null=True,
    )
    auction = models.BooleanField(
        default=False,
    )
    auction_end_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    external_link = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    blockchain = models.CharField(
        max_length=3,
        choices=BLOCKCHAIN_CHOICES,
    )
    royalties = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )
    supply = models.IntegerField(
        validators=[
            MinValueValidator(0),
        ]        
    )

    collection_id = models.ForeignKey(
        CollectionNFT,
        on_delete=models.CASCADE,
        related_name="nft_collections",
    )
    available = models.BooleanField(
        default=True,
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="owned_nfts",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="authored_nfts",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']
