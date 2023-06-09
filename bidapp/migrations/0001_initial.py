# Generated by Django 4.2.1 on 2023-05-06 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
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
                ("name", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="pics")),
                ("description", models.CharField(max_length=100)),
                (
                    "basePrice",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Upcoming", "Upcoming"),
                            ("Active", "Active"),
                            ("Closed", "Closed"),
                        ],
                        default="Active",
                        max_length=20,
                    ),
                ),
                ("start_date", models.DateField(blank=True, null=True)),
                ("exp_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_details",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
