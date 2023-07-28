from django.contrib import admin

from apps.nft.models import Nft

@admin.register(Nft)
class NftAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_filter = ('created_at', )
