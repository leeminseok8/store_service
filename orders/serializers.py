from rest_framework import serializers

from .models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    주문 등록 시리얼라이저
    등록 시 결제 대기창으로 이동
    """

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        order.save()
        return order

    class Meta:
        model = Order
        fields = ["id", "total_price", "quantity", "order_number", "product", "user"]


class OrderListSerializer(serializers.ModelSerializer):
    """
    주문 리스트 조회 시리얼라이저
    """

    payment_state = serializers.SlugRelatedField(
        read_only=True, slug_field="payment_state", source="payment"
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "user",
            "product",
            "total_price",
            "quantity",
            "order_number",
            "created_at",
            "updated_at",
            "payment_state",
        ]


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
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ["id", "quantity", "total_price"]
