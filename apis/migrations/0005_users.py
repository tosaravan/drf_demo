# Generated by Django 4.2.2 on 2023-07-04 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0004_drinkfeedback"),
    ]

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
                ("firstname", models.CharField(max_length=200)),
                ("lastname", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("mobile", models.CharField(max_length=20)),
                ("postcode", models.CharField(max_length=10)),
                ("country", models.CharField(max_length=50)),
            ],
        ),
    ]
