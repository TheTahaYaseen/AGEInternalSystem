from django.shortcuts import redirect, render
from .models import Customer

# Create your views here.
def customers_view(request):
    
    page_title = "Customers"

    if not request.user.is_superuser:
        return redirect("home")

    customers = Customer.objects.all()

    context = {"page_title": page_title, "customers": customers}
    return render(request, "customers.html", context)

def add_view(request):
    
    form_action = "Add"
    page_title = f"{form_action} Customer"
    error = ""

    customer_name = "" 
    customer_balance = 0

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        customer_name = request.POST.get("customer_name") 
        customer_balance = int(request.POST.get("customer_balance")) if request.POST.get("customer_balance") else 0

        if customer_name == "":
            error = "Donot leave the customer name empty!"
        elif len(customer_name) > 255:
            error = "Length of customer name cannot be greater than 255 characters!"
        else:            
            try:
                customer = Customer.objects.get(name=customer_name)
                error = f"Customer called {customer_name} already exists!"
            except Customer.DoesNotExist:
                customer = Customer.objects.create(
                    name=customer_name,
                    balance=customer_balance
                )
                return redirect("customers")    

    context = {"page_title": page_title, "form_action": form_action, "error": error, "customer_name": customer_name, "customer_balance": customer_balance}
    return render(request, "customer_form.html", context)

    
def update_view(request, customer_id):

    form_action = "Update"
    page_title = f"{form_action} Customer"
    error = ""

    associated_customer = Customer.objects.get(id=customer_id)

    customer_name = associated_customer.name 
    customer_balance = associated_customer.balance 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        customer_name = request.POST.get("customer_name") 
        customer_balance = int(request.POST.get("customer_balance")) 

        if customer_name == "":
            error = "Donot leave the customer name empty!"
        elif len(customer_name) > 255:
            error = "Length of customer name cannot be greater than 255 characters!"
        else:            
            try:
                customer = Customer.objects.get(name=customer_name)
                if customer.id != associated_customer.id:
                    error = f"Customer called {customer_name} already exists!"
            except Customer.DoesNotExist:
                pass

            if not error:
                associated_customer.name = customer_name
                associated_customer.balance = customer_balance
                associated_customer.save()

                return redirect("customers")
            
    context = {"page_title": page_title, "form_action": form_action, "error": error, "customer_name": customer_name, "customer_balance": customer_balance}
    return render(request, "customer_form.html", context)

def delete_view(request, customer_id):

    associated_customer = Customer.objects.get(id=customer_id)

    page_title = "Delete Customer"

    item_category = "Customer"
    item = associated_customer.name

    if request.method == "POST":
        associated_customer.delete()
        return redirect("customers")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
