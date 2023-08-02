from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator

from apps.collections_nft.models import CollectionNFT
from apps.nft.models import Nft

User = get_user_model()


class CartItemNft(models.Model):
    nft = models.ForeignKey(
        Nft,
        on_delete=models.CASCADE,
        related_name="nft_cart",
    )
    count = models.IntegerField(
        default=1,
        validators=[
            MinLengthValidator(1),
        ]
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart_user",
    )
    items = models.ManyToManyField(
        CartItemNft,
        blank=True,
        related_name='cart_item'
    )
    
    def get_total_price(self):
        pass    
