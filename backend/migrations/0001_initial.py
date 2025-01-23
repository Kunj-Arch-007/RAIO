# Generated by Django 5.1.1 on 2025-01-15 10:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('practice_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('website', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractor', models.CharField(blank=True, max_length=255)),
                ('provider', models.CharField(blank=True, max_length=255)),
                ('fixed_fte_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('num_fte', models.IntegerField(blank=True, default=0, null=True)),
                ('gross_invoice', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('ev_check', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('capitation_charges', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('capitation_charge_frequncy', models.IntegerField(blank=True, default=0.0, null=True)),
                ('credentialing_charges', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('net_invoice', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('client_revenue', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('agreement_percentage', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('agreement_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('worked_hours', models.IntegerField(blank=True, default=0, null=True)),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('hour_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('number_of_transactions', models.IntegerField(blank=True, default=0, null=True)),
                ('transaction_rate', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('total_transactions_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('mail_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('practice_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenses', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('profit_loss', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(blank=True, max_length=50)),
                ('invoice_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('internal_invoice_number', models.CharField(blank=True, max_length=50)),
                ('internal_invoice_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('usd_to_inr', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('net_invoice', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.contract')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_end_report_notification', models.BooleanField(default=False)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_1', models.CharField(blank=True, max_length=255)),
                ('party_1_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('party_2', models.CharField(blank=True, max_length=255)),
                ('party_2_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.contract')),
            ],
        ),
    ]
