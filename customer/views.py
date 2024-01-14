from django.shortcuts import redirect, render
from .models import Customer
from employee.context_processors import access_to_context

# Create your views here.
def customers_view(request):
    
    page_title = "Customers"

    access = access_to_context(request)

    if not access["has_access_to_shop_management"] or not access["has_access_to_factory_management"]:
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

    access = access_to_context(request)

    if not access["has_access_to_shop_management"] or not access["has_access_to_factory_management"]:
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

    access = access_to_context(request)

    if not access["has_access_to_shop_management"] or not access["has_access_to_factory_management"]:
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

    access = access_to_context(request)

    if not access["has_access_to_shop_management"] or not access["has_access_to_factory_management"]:
        return redirect("home")

    item_category = "Customer"
    item = associated_customer.name

    if request.method == "POST":
        associated_customer.delete()
        return redirect("customers")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
