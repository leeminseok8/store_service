import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView

from orders.models import Order
from payments.models import Payment

from .serializers import PaymentCreateSerializer, PaymentDeleteSerializer


class PaymentCreateView(CreateAPIView):
    """
    결제를 위한 뷰
    payment_state에 따라 "결제 완료"와 "결제 취소" 상태가 됩니다.
    결제 성공 시 Order 테이블의 주문번호가 생성됩니다.
    """

    serializer_class = PaymentCreateSerializer
    permission_classes = IsAuthenticated

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        order_id = request.data["order"]
        paymented_order = Order.objects.get(id=order_id)
        paymented_order.order_number = uuid.uuid4()
        paymented_order.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PaymentDeleteView(UpdateAPIView):
    """
    결제 취소를 위한 뷰
    결제창에서 "결제 취소" 버튼을 누르면 동작
    update를 사용한 state 수정으로 소프트 delete 동작
    """

    serializer_class = PaymentDeleteSerializer
    permission_class = IsAuthenticated

    def get_queryset(self):
        queryset = Payment.objects.filter(pk=self.kwargs["pk"])
        return queryset
