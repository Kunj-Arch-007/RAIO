from decimal import Decimal
from django.db import models
from django.utils import timezone

class Client(models.Model):
    practice_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.practice_name


class Contract(models.Model):
    contractor = models.CharField(max_length=255, blank=True)
    provider = models.CharField(max_length=255, blank=True)
    practice_name = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    fixed_fte_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    num_fte = models.IntegerField(blank=True, null=True, default=0)
    gross_invoice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    ev_check = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    capitation_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
    capitation_charge_frequncy = models.IntegerField(blank=True, null=True, default=0.0)
    credentialing_charges = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
    net_invoice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    client_revenue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    agreement_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0.0)
    agreement_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    worked_hours = models.IntegerField(blank=True, null=True, default=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
    hour_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    number_of_transactions = models.IntegerField(blank=True, null=True, default=0)
    transaction_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
    total_transactions_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    mail_cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)

    def save(self, *args, **kwargs):
        # Calculate client_revenue percentage as client_revenue * (agreement_percentage / 100)
        self.agreement_amount = (self.client_revenue or Decimal('0.0')) * ((self.agreement_percentage or Decimal('0.0')) / 100)
        
        # Calculate hour_amount as worked_hours * hourly_rate
        self.hour_amount = (self.worked_hours or Decimal('0')) * (self.hourly_rate or Decimal('0.0'))

        # Calculate total_transactions_amount as fnumber_of_transactions * transaction_rate
        self.total_transactions_amount = (self.number_of_transactions or Decimal('0.0')) * (self.transaction_rate or Decimal('0.0'))

        # Calculating the gross_invoice
        self.gross_invoice = (self.agreement_amount or Decimal('0.0')) + (self.hour_amount or Decimal('0.0')) + (self.total_transactions_amount or Decimal('0.0')) + (self.mail_cost or Decimal('0.0'))

        # Calculating the Net Invoice Amount
        self.net_invoice = (self.gross_invoice or Decimal('0.0')) - ((self.gross_invoice or Decimal('0.0')) * Decimal('0.1'))

        # Calculating the capitaion charges
        # self.capitation_charges = (self.net_invoice or Decimal('0.0')) * (self.capitation_charge_frequncy or Decimal('0.0'))
        self.capitation_charges = (self.net_invoice or Decimal('0.0')) * Decimal(self.capitation_charge_frequncy or 0)

        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.contractor} - {self.practice_name}"


class Invoice(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True)
    invoice_number = models.CharField(max_length=50, blank=True)
    invoice_date = models.DateField(default=timezone.now, blank=True, null=True)
    internal_invoice_number = models.CharField(max_length=50, blank=True)
    internal_invoice_date = models.DateField(default=timezone.now, blank=True, null=True)
    usd_to_inr = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    net_invoice = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.invoice_number


class Party(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True)
    party_1 = models.CharField(max_length=255, blank=True)
    party_1_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    party_2 = models.CharField(max_length=255, blank=True)
    party_2_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.party_1} & {self.party_2} - {self.contract}"


class Expense(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True)
    expenses = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    profit_loss = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.0)
    def __str__(self):
        return f"Expense for {self.contract}"


class MonthlyReport(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, blank=True, null=True)
    month_end_report_notification = models.BooleanField(default=False)

    def __str__(self):
        return f"Monthly Report for {self.contract}"
