from rest_framework import serializers

from apps.products.models import Product, Thumbnail


class ThumbnailSerializer(serializers.ModelSerializer):
    """
    썸네일 이미지 생성 시리얼라이저
    유저 테이블에 FK
    """

    class Meta:
        model = Thumbnail
        fields = ["image"]


class ProductPostSerializer(serializers.ModelSerializer):
    """
    상품 생성 시리얼라이저
    """

    thumbnail = ThumbnailSerializer()

    def create(self, validated_data):
        thumbnails = self.validated_data.pop("thumbnail")
        product = Product.objects.create(**validated_data)
        product.save()

        if thumbnails:
            for thumbnail in thumbnails:
                Thumbnail.objects.create(
                    product_id=product.id, image=thumbnails[thumbnail]
                )
        return product

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "delivery_fee",
            "origin",
            "thumbnail",
        ]


class ProductListSerializer(serializers.ModelSerializer):
    """
    상품 리스트 조회 생성 시리얼라이저
    """

    class Meta:
        model = Product
        fields = ["id", "title", "price"]


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    상품 조회 시리얼라이저
    """

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at"]


class ProductUpdateSerializer(serializers.ModelSerializer):
    """
    상품 수정 시리얼라이저
    """

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.price = validated_data.get("price", instance.price)
        instance.delivery_fee = validated_data.get("delivery_fee", instance.price)
        instance.origin = validated_data.get("origin", instance.origin)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = ["title", "content", "price", "delivery_fee", "origin"]
