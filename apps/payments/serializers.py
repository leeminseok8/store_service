from rest_framework import serializers

from apps.payments.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    """
    결제 생성 시리얼라이저
    """

    class Meta:
        model = Payment
        fields = ["payment_method", "payment_state", "order"]


class PaymentDeleteSerializer(serializers.ModelSerializer):
    """
    결제 취소 시리얼라이저
    """

    class Meta:
        model = Payment
        fields = ["payment_state"]

    def update(self, instance, validated_data):
        instance.payment_state = False
        instance.save()

        return instance
