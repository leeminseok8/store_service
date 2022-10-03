from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models import Product

from .models import Order
from .serializers import (
    OrderCreateSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
)


class OrderCreateView(ListCreateAPIView):
    """
    주문 등록을 위한 뷰
    결제 금액이 30,000원 이상이면 배달비 무료
    """

    permission_classes = IsAuthenticated
    serializer_class = OrderCreateSerializer

    def post(self, request):
        products = Product.objects.get(id=request.data["product"])

        total_price = request.data["quantity"] * products.price

        if total_price < 30000:
            total_price += products.delivery_fee

        request.data["total_price"] = total_price

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

    def get(self, request):
        """
        주문 내역 리스트 조회를 위한 뷰
        """

        try:
            order = Order.objects.all()
            serializer = OrderListSerializer(order, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "불러올 수 없습니다."})


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    """
    주문 조회, 수정, 삭제를 위한 뷰
    """

    permission_classes = IsAuthenticated

    def get_queryset(self):
        queryset = Order.objects.filter(pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return OrderDetailSerializer
        elif self.request.method == "PATCH":
            return OrderUpdateSerializer
