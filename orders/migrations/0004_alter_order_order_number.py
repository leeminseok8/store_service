# Generated by Django 4.1.1 on 2022-10-03 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_order_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_number",
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]
