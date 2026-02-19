from django.db import migrations, models


def fill_total_price(apps, schema_editor):
    ServiceRequest = apps.get_model("leads", "ServiceRequest")
    ServiceRequest.objects.filter(total_price__isnull=True).update(total_price=models.F("price"))


class Migration(migrations.Migration):
    dependencies = [
        ("leads", "0003_servicerequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="total_price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.RunPython(fill_total_price, migrations.RunPython.noop),
    ]
