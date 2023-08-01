from django_filters import rest_framework as filter

from apps.nft.models import Nft


class NftPriceFilter(filter.FilterSet):
    min_price = filter.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filter.NumberFilter(field_name="price", lookup_expr="lte")
    
    class Meta:
        model = Nft
        fields = (
            "auction", 
            "blockchain",
            "min_price",
            "max_price",
        )
