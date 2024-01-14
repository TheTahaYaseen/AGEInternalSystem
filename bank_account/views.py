from django.shortcuts import redirect, render
from .models import Bank, BankAccount

# Create your views here.
def bank_accounts_view(request):
    
    page_title = "Bank Accounts"

    if not request.user.is_superuser:
        return redirect("home")

    bank_accounts = BankAccount.objects.all()

    context = {"page_title": page_title, "bank_accounts": bank_accounts}
    return render(request, "bank_accounts.html", context)

def add_view(request):
    
    form_action = "Add"
    page_title = f"{form_action} Bank Account"
    error = ""

    banks = Bank.objects.all()

    bank_name = "" 
    account_number = "" 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        bank_name = request.POST.get("bank_name") 
        account_number = request.POST.get("account_number") 

        if bank_name == "" or account_number == "":
            error = "Donot leave the bank name or account number empty!"
        elif len(bank_name) > 255:
            error = "Length of bank name cannot be greated than 255 characters!"
        else:            
            try:
                bank_account = BankAccount.objects.get(account_number=account_number)
                error = f"Bank account: {account_number} already exists!"
            except BankAccount.DoesNotExist:
                bank, created = Bank.objects.get_or_create(name=bank_name)
                bank_account = BankAccount.objects.create(
                    associated_bank=bank,
                    account_number=account_number,
                )

                return redirect("bank_accounts")

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "bank_name": bank_name, "account_number": account_number, "banks": banks}
    return render(request, "bank_account_form.html", context)

    
def update_view(request, bank_account_id):

    form_action = "Update"
    page_title = f"{form_action} Bank Account"
    error = ""

    banks = Bank.objects.all()

    associated_bank_account = BankAccount.objects.get(id=bank_account_id)

    account_number = associated_bank_account.account_number 
    bank_name = associated_bank_account.associated_bank.name 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        bank_name = request.POST.get("bank_name") 
        account_number = request.POST.get("account_number") 

        if bank_name == "" or account_number == "":
            error = "Donot leave the bank name or account number empty!"
        elif len(bank_name) > 255:
            error = "Length of bank name cannot be greater than 255 characters!"
        else:            
            try:
                bank_account = BankAccount.objects.get(account_number=account_number)
                if str(bank_account.id) != bank_account_id:
                    error = f"Bank account: {account_number} already exists!"
            except BankAccount.DoesNotExist:
                pass

            if not error:
                bank, created = Bank.objects.get_or_create(name=bank_name)

                associated_bank_account.account_number = account_number
                associated_bank_account.associated_bank = bank
                associated_bank_account.save()

                return redirect("bank_accounts")

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "bank_name": bank_name, "account_number": account_number, "banks": banks}
    return render(request, "bank_account_form.html", context)

def delete_view(request, bank_account_id):

    associated_bank_account = BankAccount.objects.get(id=bank_account_id)

    page_title = "Delete Bank Account"

    if not request.user.is_superuser:
        return redirect("home")

    item_category = "Bank Account"
    item = associated_bank_account.account_number

    if request.method == "POST":
        associated_bank_account.delete()
        return redirect("bank_accounts")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
