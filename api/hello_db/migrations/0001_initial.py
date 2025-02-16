# Generated by Django 5.1.6 on 2025-02-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hello",
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
                ("world", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "hello",
            },
        ),
    ]
