from django.db import models

from utils.timestamp import TimeStampedModel


class Product(TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    origin = models.CharField(max_length=100)

    class Meta:
        db_table = "products"


class Thumbnail(TimeStampedModel):
    image = models.CharField(max_length=1000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "thumbnails"
