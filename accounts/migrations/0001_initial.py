# Generated by Django 4.1.1 on 2022-09-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=10, verbose_name="이름")),
                (
                    "username",
                    models.CharField(max_length=20, unique=True, verbose_name="아이디"),
                ),
                ("password", models.CharField(max_length=128, verbose_name="비밀번호")),
                ("sex", models.BooleanField(default=True, verbose_name="성별")),
                (
                    "mobile",
                    models.CharField(max_length=15, unique=True, verbose_name="핸대폰 번호"),
                ),
                ("address", models.CharField(max_length=100, verbose_name="주소")),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
