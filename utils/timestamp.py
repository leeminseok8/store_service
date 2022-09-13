from django.db import models


class TimeStampedModel(models.Model):
    """
    생성 날짜, 수정 날짜 필드 생성을 위한 기본 모델
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
