from django.contrib import admin

from apps.collections_nft.models import CollectionNFT


@admin.register(CollectionNFT)
class CollectionNFTAdmin(admin.ModelAdmin):
    list_display = ['title', 'author_id', 'owner_id']
    list_filter = ['created_at', 'title']
