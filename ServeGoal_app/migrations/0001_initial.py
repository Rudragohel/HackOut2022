# Generated by Django 4.1.1 on 2022-09-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("name", models.CharField(max_length=32)),
                ("email", models.EmailField(default="", max_length=254)),
                ("password", models.CharField(default="", max_length=70)),
            ],
        ),
    ]
