from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Order
from .serializers import (
    OrderCreateSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
)


class OrderCreateView(CreateAPIView):
    """
    주문 등록을 위한 뷰
    """

    permission_classes = [AllowAny]
    serializer_class = OrderCreateSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "주문 등록이 완료되었습니다."}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "주문 등록에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    """
    주문 조회, 수정, 삭제를 위한 뷰
    """

    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Order.objects.filter(pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderDetailSerializer
        elif self.request.method == "PATCH":
            return OrderUpdateSerializer
