from .models import Contract
from .models import Client

# Function to filter and sort contracts by net_invoice in descending order
def filter_contracts_by_net_invoice(request):
    """
    Filters and sorts contracts by net_invoice in descending order if the 'filter' 
    parameter is present in the request.
    """
    contracts = Contract.objects.all()

    # Check if the user requested to filter contracts by net_invoice (descending)
    if request.method == 'POST' and 'filter_contract' in request.POST:
        contracts = contracts.order_by('-net_invoice')  # Sorting by net_invoice descending

    return contracts

def filter_clients_by_start_date(request):
    """
    Filters and sorts clients by start_date in descending order if the 'filter' 
    parameter is present in the request.
    """
    clients = Client.objects.all()

    if request.method == 'POST' and 'start-date' in request.POST:
        clients = clients.order_by('-start_date')  # Sorting by start_date descending
    
    if request.method == "POST" and "end-date" in request.POST:
        clients = clients.order_by('start_date')

    return clients