from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DayScenario",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("contact", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("guests_count", models.PositiveIntegerField()),
                ("comment", models.TextField(blank=True)),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_processed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Сценарий дня",
                "verbose_name_plural": "Сценарии дня",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ScenarioItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
                ("quantity", models.IntegerField(default=1)),
                (
                    "scenario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="leads.dayscenario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент сценария",
                "verbose_name_plural": "Элементы сценария",
            },
        ),
    ]
