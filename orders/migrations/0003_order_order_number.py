# Generated by Django 4.1.1 on 2022-10-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_remove_order_delivery_fee"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_number",
            field=models.CharField(editable=False, max_length=128, null=True),
        ),
    ]