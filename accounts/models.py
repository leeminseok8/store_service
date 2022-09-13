from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from utils.timestamp import TimeStampedModel


class UserManager(BaseUserManager):
    """
    유저 및 관리자를 생성하기 위한 모델
    회원가입 시 필수 입력 사항 : [username, mobile, address, password]
    """

    def create_user(self, username, mobile, address, password=None):
        if not username:
            raise ValueError("계정 이름을 입력해주세요.")
        if not password:
            raise ValueError("비밀번호를 입력해주세요.")
        if not mobile:
            raise ValueError("핸드폰 번호을 입력해주세요.")
        if not address:
            raise ValueError("주소를 입력해주세요.")

        user = self.model(
            username=username,
            password=password,
            mobile=mobile,
            address=address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, mobile, address, password=None):
        user = self.create_user(
            username=username,
            password=password,
            mobile=mobile,
            address=address,
        )

        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampedModel):
    """
    관리할 유저 정보와 유저/관리자 권한을 구분하는 모델
    """

    name = models.CharField(verbose_name="이름", max_length=10)
    username = models.CharField(verbose_name="아이디", max_length=20, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    sex = models.BooleanField(verbose_name="성별", default=True)
    mobile = models.CharField(verbose_name="핸드폰 번호", max_length=15, unique=True)
    address = models.CharField(verbose_name="주소", max_length=100)

    # state
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["mobile", "address"]

    class meta:
        db_table = "accounts"
