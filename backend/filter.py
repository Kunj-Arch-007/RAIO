from .models import Contract

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
