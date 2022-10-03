from re import M
from django.db import models

from orders.models import Order
from utils.timestamp import TimeStampedModel


class Payment(TimeStampedModel):
    payment_method = models.CharField(max_length=10)
    payment_state = models.BooleanField(default=True)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = "payments"
