# Generated by Django 5.1.1 on 2025-01-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_party_1_amount_party_party_amount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='net_invoice_rupee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
