from django.shortcuts import redirect, render
from .models import Company
from bank_account.models import BankAccount

# Create your views here.
def companies_view(request):
    
    page_title = "Companies"

    if not request.user.is_superuser:
        return redirect("home")

    companies = Company.objects.all()

    context = {"page_title": page_title, "companies": companies}
    return render(request, "companies.html", context)

def add_view(request):
    
    form_action = "Add"
    page_title = f"{form_action} Company"
    error = ""

    bank_accounts = BankAccount.objects.all()

    company_name = "" 
    associated_bank_account_number = "" 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        company_name = request.POST.get("company_name") 
        associated_bank_account_number = int(request.POST.get("associated_bank_account_number")) if request.POST.get("associated_bank_account_number") else ""  

        if company_name == "":
            error = "Donot leave the company name empty!"
        elif len(company_name) > 255:
            error = "Length of company name cannot be greater than 255 characters!"
        else:            
            try:
                company = Company.objects.get(name=company_name)
                error = f"Company: {company_name} already exists!"
            except Company.DoesNotExist:
                if associated_bank_account_number != "":
                    associated_bank_account = BankAccount.objects.get(account_number=associated_bank_account_number)
                else:
                    associated_bank_account = None
                company = Company.objects.create(
                    name=company_name,
                    associated_bank_account=associated_bank_account,
                )

                return redirect("companies")
    

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "company_name": company_name, "associated_bank_account_number": associated_bank_account_number, "bank_accounts": bank_accounts}
    return render(request, "company_form.html", context)

    
def update_view(request, company_id):

    form_action = "Update"
    page_title = f"{form_action} Company"
    error = ""

    bank_accounts = BankAccount.objects.all()

    associated_company = Company.objects.get(id=company_id)

    if associated_company.associated_bank_account != None:
        associated_bank_account_number = associated_company.associated_bank_account.account_number 
    else:
        associated_bank_account_number = None 
    company_name = associated_company.name 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        company_name = request.POST.get("company_name") 
        associated_bank_account_number = int(request.POST.get("associated_bank_account_number")) if request.POST.get("associated_bank_account_number") else ""  


        if company_name == "":
            error = "Donot leave the company name empty!"
        elif len(company_name) > 255:
            error = "Length of company name cannot be greater than 255 characters!"
        else:            
            try:
                company = Company.objects.get(name=company_name)
                if str(company.id) != company_id:
                    error = f"Company: {company_name} already exists!"
            except Company.DoesNotExist:
                pass

            if not error:
                if associated_bank_account_number != "":
                    associated_bank_account = BankAccount.objects.get(account_number=associated_bank_account_number)
                else:
                    associated_bank_account = None
    
                associated_company.associated_bank_account = associated_bank_account
                associated_company.name = company_name
                associated_company.save()

                return redirect("companies")

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "company_name": company_name, "associated_bank_account_number": associated_bank_account_number, "bank_accounts": bank_accounts}
    return render(request, "company_form.html", context)

def delete_view(request, company_id):

    associated_company = Company.objects.get(id=company_id)

    page_title = "Delete Company"

    if not request.user.is_superuser:
        return redirect("home")

    item_category = "Company"
    item = associated_company.name

    if request.method == "POST":
        associated_company.delete()
        return redirect("companies")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
