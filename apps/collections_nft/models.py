from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class CollectionNFT(models.Model):
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='collections_nft',
    )
    external_link = models.CharField(
        max_length=256,
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
