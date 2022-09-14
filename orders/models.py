from re import T
from django.db import models

from utils.timestamp import TimeStampedModel

from products.models import Product
from accounts.models import User


class Order(TimeStampedModel):
    quantity = models.PositiveIntegerField()
    delivery_fee = models.IntegerField()
    total_price = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"
