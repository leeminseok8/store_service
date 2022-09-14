from rest_framework import serializers

from .models import Product, Thumbnail
from accounts.models import User


class ThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thumbnail
        fields = ["image"]


class ProductPostSerializer(serializers.ModelSerializer):
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
        fields = ["id", "title", "content", "price", "origin", "thumbnail"]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
