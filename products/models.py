from django.db import models

from accounts.models import User
from utils.timestamp import TimeStampedModel


class Product(TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    origin = models.CharField(max_length=100)
    # user = models.ManyToManyField(User, through="UserProduct")

    class Meta:
        db_table = "products"


# class UserProduct(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     class Meta:
#         db_table = "users_products"


class Thumbnail(TimeStampedModel):
    image = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "thumbnails"
