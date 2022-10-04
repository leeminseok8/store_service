from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, CreateAPIView

from .serializers import SignInSerializer, SignUpSerializer


class SignUpView(CreateAPIView):
    """
    회원가입을 진행하는 View
    """

    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "회원가입에 성공하였습니다."}, status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {"message": "회원가입에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class SignInView(GenericAPIView):
    """
    JWT를 사용한 로그인 기능
    """

    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return Response(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
