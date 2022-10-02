from re import M
from django.db import models

from utils.timestamp import TimeStampedModel


class Payments(TimeStampedModel):
    payment_method = models.CharField(max_length=10)
    payment_state = models.BooleanField(default=True)
