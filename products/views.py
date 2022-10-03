from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Product
from .seralizers import (
    ProductPostSerializer,
    ProductListSerializer,
    ProductDetailSerializer,
    ProductUpdateSerializer,
)
from .permissions import IsOwnerOrReadOnly


class ProductPostView(ListCreateAPIView):
    """
    상풍 등록을 위한 뷰
    title, content, price, origin, thumbnail 생성
    """

    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request):
        serializer = ProductPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "등록이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"message": "등록에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

    def get(self, request):
        try:
            product = Product.objects.all()
            serializer = ProductListSerializer(product, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "불러올 수 없습니다."})


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    """
    상풍 조회, 수정, 삭제를 위한 뷰
    """

    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Product.objects.filter(pk=self.kwargs["pk"])
        return queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailSerializer
        elif self.request.method == "PATCH":
            return ProductUpdateSerializer
