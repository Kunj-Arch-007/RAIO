from django import forms
from .models import Contract, Client, Invoice, Expense, Party
from decimal import Decimal

class ContractForm(forms.ModelForm):
    # Additional fields not in the model (for display or calculations)
    total_agreement_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Calculated Percentage',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    total_transactions_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Total Transactions Amount',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    total_gross_invoice = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Gross Invoice',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    total_work_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Total Work Amount',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    total_net_invoice_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Net Invoice',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    total_capitation_charges = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Total Capitation Charges',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    
    class Meta:
        model = Contract
        fields = [
            'contractor', 'provider', 'practice_name',
            'client_revenue', 'agreement_percentage', 'fixed_fte_price', 'num_fte',
            'worked_hours', 'hourly_rate', 'number_of_transactions', 'transaction_rate',
            'ev_check', 'capitation_charges', 'credentialing_charges', 'mail_cost', 'capitation_charge_frequncy'
        ]
        widgets = {
            'client_revenue': forms.NumberInput(attrs={'class': 'form-control'}),
            'agreement_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'fixed_fte_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_fte': forms.NumberInput(attrs={'class': 'form-control'}),
            'worked_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'number_of_transactions': forms.NumberInput(attrs={'class': 'form-control'}),
            'transaction_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'ev_check': forms.NumberInput(attrs={'class': 'form-control'}), 
            'capitation_charges': forms.NumberInput(attrs={'class': 'form-control'}),
            'credentialing_charges': forms.NumberInput(attrs={'class': 'form-control'}),
            'net_invoice': forms.NumberInput(attrs={'class': 'form-control'}),
            'mail_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'capitation_charge_frequncy': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        client_revenue = cleaned_data.get('client_revenue') or Decimal('0.0')
        agreement_percentage = cleaned_data.get('agreement_percentage') or Decimal('0.0') 

        # Calculate totals based on optional values
        cleaned_data['total_agreement_amount'] = client_revenue * (agreement_percentage / Decimal('100'))

        worked_hours = cleaned_data.get('worked_hours') or Decimal('0')
        hourly_rate = cleaned_data.get('hourly_rate') or Decimal('0')
        cleaned_data['total_work_amount'] = worked_hours * hourly_rate

        number_of_transactions = cleaned_data.get('number_of_transactions') or Decimal('0.0')
        transaction_rate = cleaned_data.get('transaction_rate') or Decimal('0.0')
        cleaned_data['total_transactions_amount'] = number_of_transactions * transaction_rate

        return cleaned_data


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client  
        fields = ('practice_name', 'email', 'address', 'start_date', 'end_date', 'phone_number', 'website', 'notes')
        widgets = {
            'practice_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['contract', 'invoice_number', 'invoice_date', 'internal_invoice_number', 
                  'internal_invoice_date', 'usd_to_inr', 'net_invoice']
        widgets = {
            'contract': forms.Select(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'internal_invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'internal_invoice_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'usd_to_inr': forms.NumberInput(attrs={'class': 'form-control'}),
            'net_invoice': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['contract', 'expenses', 'profit_loss']


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['contract', 'party_1', 'party_1_amount', 'party_2', 'party_2_amount']
        # Ensure party_1, party_1_amount, party_2, and party_2_amount are optional in the model
