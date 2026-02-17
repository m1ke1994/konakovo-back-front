from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("contact", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("is_processed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Заявка",
                "verbose_name_plural": "Заявки",
                "ordering": ["-created_at"],
            },
        ),
    ]
