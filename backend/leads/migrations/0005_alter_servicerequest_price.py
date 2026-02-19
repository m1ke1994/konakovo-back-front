from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0004_servicerequest_price_total_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicerequest",
            name="price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
