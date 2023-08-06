from rest_framework import serializers

from apps.nft.models import Nft, NftAuction


class AuctionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NftAuction
        fields = (
            'id',
            'user_id',
            'price',
            'created_at',
        )


class NftLISTSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nft
        fields = (
            'id',
            'title',
            'author',
            'price',
            'blockchain',
            'image',
        )


class NftSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    auction_prices = AuctionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Nft
        fields = (
            'id',
            'title',
            'image',
            'auction',
            'auction_end_date',
            'auction_prices',
            'external_link',
            'description',
            'price',
            'blockchain',
            'royalties',
            'supply',
            'collection_id',
            'available',
            'created_at',
            'owner',
            'author',
        )
        read_only_fields = (
            'owner',
            'author',
            'auction_prices',
        )
    
    def create(self, validated_data):
        auction = validated_data['auction']
        auction_end_date = validated_data['auction_end_date']
        if auction and not auction_end_date:
            raise serializers.ValidationError("No end date for auction!")
        
        image_file = self.context['request'].FILES.get('image')  # Получаем файл изображения из запроса
        if image_file:
            validated_data['image'] = image_file  # Добавляем файл изображения в словарь validated_data
        else:
            # Если файл изображения отсутствует в запросе PATCH, оставляем текущее изображение без изменений
            validated_data['image'] = self.instance.image


        nft_instance = Nft.objects.create(**validated_data)

        return nft_instance
    
    def update(self, instance, validated_data):
        auction = validated_data['auction']
        auction_end_date = validated_data['auction_end_date']
        if auction and not auction_end_date:
            raise serializers.ValidationError("No end date for auction!")

        return super().update(instance, validated_data)


class NFTCOllectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nft
        fields = (
            'id',
            'image',
        )


class AuctionPriceSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        write_only=True,
    )
    
    class Meta:
        model = NftAuction
        fields = ('price', )
