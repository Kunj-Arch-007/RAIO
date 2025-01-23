# Generated by Django 5.1.1 on 2025-01-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0004_invoice_net_invoice_rupee"),
    ]

    operations = [
        migrations.AddField(
            model_name="party",
            name="party_amount_rupee",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AddField(
            model_name="party",
            name="party_calculated_amount",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AddField(
            model_name="party",
            name="party_calculated_amount_rupee",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
    ]