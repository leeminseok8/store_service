from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView

from .serializers import SignInSerializer, SignUpSerializer


class SignUpView(CreateAPIView):
    """
    회원가입을 진행하는 View
    """

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid:
            serializer.save
            return HttpResponse(
                {"message": "회원가입에 성공하였습니다."}, status=status.HTTP_201_CREATED
            )

        else:
            return HttpResponse(
                {"message": "회원가입에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class SignInView(GenericAPIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)

        if serializer.is_valid():
            token = serializer.validated_data
            return HttpResponse(
                {
                    "message": "로그인 되었습니다.",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return HttpResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
