from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PreviousPrice(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    previous_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


class CollectionNFT(models.Model):
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='collections_nft',
        blank=True,
        null=True,
    )
    external_link = models.CharField(
        max_length=256,
    )
    previous_prices = models.ManyToManyField(
        PreviousPrice,
        blank=True,
        related_name='previous_prices'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return f"{self.title}"
