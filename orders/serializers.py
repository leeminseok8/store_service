from rest_framework import serializers

from .models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    주문 등록 시리얼라이저
    현재 POST로 받아오고 있지만, Product에서 GET으로
    다른 컬럼을 가져와서 자동으로 등록 예정
    """

    def create(self, validated_data):
        # total_prices = self.validated_data.pop("total_price")
        # final_price = total_prices * self.validated_data.get("quantity")
        # validated_data["total_price"] = final_price
        order = Order.objects.create(**validated_data)
        order.save()
        return order

    class Meta:
        model = Order
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    """
    주문 조회 시리얼라이저
    """

    class Meta:
        model = Order
        exclude = ["created_at", "updated_at"]


class OrderUpdateSerializer(serializers.ModelSerializer):
    """
    주문 수정 시리얼라이저
    """

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.total_price = validated_data.get("total_price", instance.total_price)
        instance.delivery_fee = validated_data.get(
            "delivery_fee", instance.delivery_fee
        )
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ["quantity", "total_price", "delivery_fee"]
