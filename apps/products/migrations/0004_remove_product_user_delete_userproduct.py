# Generated by Django 4.1.1 on 2022-09-14 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_thumbnail_table_userproduct_product_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="user",
        ),
        migrations.DeleteModel(
            name="UserProduct",
        ),
    ]
