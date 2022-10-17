# Generated by Django 4.1 on 2022-09-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=20)),
                ("product_sn", models.CharField(max_length=20)),
                ("product_name", models.CharField(max_length=20)),
                ("product_detail", models.CharField(max_length=200)),
                ("created_date", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["-created_date"],},
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=500)),
                ("img", models.CharField(default="", max_length=1000)),
                ("sn", models.CharField(default="", max_length=50)),
                ("defects", models.CharField(default="", max_length=2000)),
                ("hazards", models.CharField(default="", max_length=2000)),
                ("consumers", models.CharField(default="", max_length=2000)),
                ("supplier", models.CharField(default="", max_length=2000)),
                ("traders", models.CharField(default="", max_length=2000)),
                ("sold_venues", models.CharField(default="", max_length=1000)),
                ("avaiable_sale_date", models.CharField(default="", max_length=1000)),
                ("content", models.CharField(default="", max_length=2000)),
                ("published_date", models.CharField(default="", max_length=50)),
                ("category", models.CharField(default="", max_length=50)),
            ],
            options={"ordering": ["category"],},
        ),
    ]