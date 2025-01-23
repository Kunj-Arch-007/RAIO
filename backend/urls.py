from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Landing Page
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # The Ultimate section of Contrats 
    path('contracts/', views.contract_list, name='contract_list'),
    path('contracts/create/', views.contract_create, name='contract_create'),
    path('contracts/update/<int:pk>/', views.contract_update, name='contract_update'),
    path('contracts/delete/<int:pk>/', views.contract_delete, name='contract_delete'),
    
    # The Ultimate section of Clients
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/update/<int:pk>/', views.client_update, name='client_update'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),
    
    # The Ultimate section of Invoices
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/update/<int:pk>/', views.invoice_update, name='invoice_update'),
    path('invoices/delete/<int:pk>/', views.invoice_delete, name='invoice_delete'),
    
    # The Ultimate section of Expenses
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/create/', views.expense_create, name='expense_create'),
    path('expenses/update/<int:pk>/', views.expense_update, name='expense_update'),
    path('expenses/delete/<int:pk>/', views.expense_delete, name='expense_delete'),
    
    # The Ultimate section of Party
    path('parties/', views.party_list, name='party_list'),
    path('parties/create/', views.party_create, name='party_create'),
    path('parties/update/<int:pk>/', views.party_update, name='party_update'),
    path('parties/delete/<int:pk>/', views.party_delete, name='party_delete'),
    
    
    path('pending-invoices/', views.pending_invoices, name='pending_invoices'),
    path('generate-reports/', views.generate_reports, name='generate_reports'),
]