from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0002_dayscenario_scenarioitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("contact", models.CharField(max_length=255)),
                ("service_title", models.CharField(max_length=255)),
                ("service_slug", models.CharField(max_length=255)),
                ("message", models.TextField(blank=True)),
                ("preferred_date", models.DateField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_processed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Заявка на услугу",
                "verbose_name_plural": "Заявки на услуги",
                "ordering": ["-created_at"],
            },
        ),
    ]
