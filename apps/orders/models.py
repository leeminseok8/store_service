from re import T
from django.db import models

from utils.timestamp import TimeStampedModel

from apps.products.models import Product
from apps.accounts.models import User


class Order(TimeStampedModel):
    quantity = models.PositiveIntegerField()
    total_price = models.IntegerField()
    order_number = models.CharField(max_length=128, null=True, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"
