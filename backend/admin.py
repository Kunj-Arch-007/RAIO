from django.contrib import admin
from .models import Client, Contract, Invoice, Party, Expense, MonthlyReport

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'practice_name', 'start_date', 'end_date', 'email')  # Fields to display in admin
    list_filter = ('practice_name',)  # Filter option for practice_name

class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'contractor', 'provider', 'practice_name', 'client_revenue')  # Fields to display
    list_filter = ('practice_name', 'provider', 'contractor')  # Filter options

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice_number', 'contract', 'invoice_date', 'internal_invoice_number', 'usd_to_inr', 'net_invoice')  # Fields to display
    list_filter = ('contract', 'invoice_date')  # Filter options

class PartyAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'party_name', 'party_amount', 'party_percentage', 'party_amount_rupee', 'party_calculated_amount_rupee', 'party_calculated_amount')  # Fields to display
    list_filter = ('contract',)  # Filter option

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'expenses', 'profit_loss')  # Fields to display
    list_filter = ('contract',)  # Filter option

class MonthlyReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'contract', 'month_end_report_notification')  # Fields to display
    list_filter = ('contract',)  # Filter option

# Registering the models with the admin site
admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(MonthlyReport, MonthlyReportAdmin)
