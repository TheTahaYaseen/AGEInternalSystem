from django.shortcuts import redirect, render
from .models import Employee
from bank_account.models import BankAccount
from role.models import Role

# Create your views here.
def employees_view(request):
    
    page_title = "Employees"

    if not request.user.is_superuser:
        return redirect("home")

    employees = Employee.objects.all()

    context = {"page_title": page_title, "employees": employees}
    return render(request, "employees.html", context)

def add_view(request):
    
    form_action = "Add"
    page_title = f"{form_action} Employee"
    error = ""

    bank_accounts = BankAccount.objects.all()
    roles = Role.objects.all()

    employee_name = "" 
    associated_bank_account_number = "" 
    associated_role = "" 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        employee_name = request.POST.get("employee_name") 
        associated_bank_account_number = int(request.POST.get("associated_bank_account_number")) if request.POST.get("associated_bank_account_number") else ""  
        associated_role = request.POST.get("associated_role") 

        if employee_name == "" and associated_role != "":
            error = "Donot leave the employee name or role empty!"
        elif len(employee_name) > 255:
            error = "Length of employee name cannot be greater than 255 characters!"
        else:            
            if associated_bank_account_number != "":
                associated_bank_account = BankAccount.objects.get(account_number=associated_bank_account_number)
            else:
                associated_bank_account = None

            associated_role = Role.objects.get(role=associated_role)

            employee = Employee.objects.create(
                name=employee_name,
                associated_bank_account=associated_bank_account,
                associated_role=associated_role,
            )

            return redirect("employees")
    

    context = {"page_title": page_title, "form_action": form_action, "error": error, "bank_accounts": bank_accounts, "roles": roles,
               "employee_name": employee_name, "associated_bank_account_number": associated_bank_account_number, "associated_role": associated_role}
    return render(request, "employee_form.html", context)

    
def update_view(request, employee_id):

    form_action = "Update"
    page_title = f"{form_action} Employee"
    error = ""

    bank_accounts = BankAccount.objects.all()
    roles = Role.objects.all()

    associated_employee = Employee.objects.get(id=employee_id)

    if associated_employee.associated_bank_account != None:
        associated_bank_account_number = associated_employee.associated_bank_account.account_number 
    else:
        associated_bank_account_number = None 
    employee_name = associated_employee.name 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        employee_name = request.POST.get("employee_name") 
        associated_bank_account_number = int(request.POST.get("associated_bank_account_number")) if request.POST.get("associated_bank_account_number") else ""  
        associated_role = request.POST.get("associated_role") 

        if employee_name == "" and associated_role != "":
            error = "Donot leave the employee name or role empty!"
        elif len(employee_name) > 255:
            error = "Length of employee name cannot be greater than 255 characters!"
        else:            
            if associated_bank_account_number != "":
                associated_bank_account = BankAccount.objects.get(account_number=associated_bank_account_number)
            else:
                associated_bank_account = None

            associated_role = Role.objects.get(role=associated_role)

            associated_employee.name = employee_name
            associated_employee.associated_bank_account = associated_bank_account
            associated_employee.associated_role = associated_role
            associated_employee.save()

            return redirect("employees")

    context = {"page_title": page_title, "form_action": form_action, "error": error, "bank_accounts": bank_accounts, "roles": roles,
               "employee_name": employee_name, "associated_bank_account_number": associated_bank_account_number, "associated_role": associated_role}
    return render(request, "employee_form.html", context)

def delete_view(request, employee_id):

    associated_employee = Employee.objects.get(id=employee_id)

    page_title = "Delete Employee"

    item_category = "Employee"
    item = associated_employee.name

    if request.method == "POST":
        associated_employee.delete()
        return redirect("employees")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
