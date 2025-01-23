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
            'contractor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contractor'}),
            'provider': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Provider'}),   
            'practice_name': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Practice Name'}),
            'client_revenue': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Client Revenue'}),
            'agreement_percentage': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Agreement Percentage'}),
            'fixed_fte_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Fixed FTE Price'}),
            'num_fte': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of FTE'}),
            'worked_hours': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Worked Hours'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Hourly Rate'}),
            'number_of_transactions': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Transactions'}),
            'transaction_rate': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Transaction Rate'}),
            'ev_check': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'EV Check'}), 
            'capitation_charges': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capitation Charges'}),
            'credentialing_charges': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Credentialing Charges'}),
            'net_invoice': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Net Invoice'}),
            'mail_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mail Cost'}),
            'capitation_charge_frequncy': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capitation Charge Frequency'}),
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
            'practice_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Practice Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Start Date'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'End Date'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes'}),
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        # Additional fields not in the model (for display or calculations)
        total_net_invoice_amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Net Invoice',
        widget=forms.TextInput(attrs={'readonly': 'readonly'})) 

        model = Invoice
        fields = ['contract', 'invoice_number', 'invoice_date', 'internal_invoice_number', 
                  'internal_invoice_date', 'usd_to_inr', 'net_invoice']
        widgets = {
            'contract': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Contract'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Invoice Number'}),
            'invoice_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Invoice Date'}),
            'internal_invoice_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Internal Invoice Number'}),
            'internal_invoice_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Internal Invoice Date'}),
            'usd_to_inr': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'USD to INR'}),
            'net_invoice': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Net Invoice'}),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['contract', 'expenses', 'profit_loss']
        widgets = {
            'contract': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Contract'}),
            'expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expenses'}),
            'profit_loss': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Profit Loss'}),
        }


class PartyForm(forms.ModelForm):
    class Meta:
        model = Party
        fields = ['contract', 'party_name', 'party_amount', 'party_percentage', 'party_amount_rupee', 'party_calculated_amount_rupee', 'party_calculated_amount']
        widgets = {
            'party_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Partner Name'}),
            'contract': forms.Select(attrs={'class': 'form-control'}),
            'party_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Amount'}),
        }
        # Ensure party_1, party_1_amount, party_2, and party_2_amount are optional in the model
