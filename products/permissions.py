from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    관리자 : 상품 및 결제, 주문 CRUD 권한 부여
    이용자 : 회원가입, 결제, 주문 외에는 R 권한 부여
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """

    def has_permission(self, request, view):

        user = request.user

        if request.method in SAFE_METHODS:
            return True
        if user.is_authenticated:
            if user.is_staff:
                return True
            else:
                return False
