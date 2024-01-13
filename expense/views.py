from django.shortcuts import redirect, render
from django.urls import reverse

from employee.models import Employee
from .models import Expense, ExpenseCategory

# Create your views here.
def expenses_view(request, association):
    
    page_title = f"{association.title()} Expenses"

    if not request.user.is_superuser:
        return redirect("home")

    expenses = Expense.objects.filter(association=association)

    context = {"page_title": page_title, "expenses": expenses}
    return render(request, "expenses.html", context)

def add_view(request, association):
    
    form_action = "Add"
    page_title = f"{form_action} {association.title()} Expense"
    error = ""

    expense_amount = "" 
    expense_category = "" 
    expense_reason = "" 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        expense_amount = int(request.POST.get("expense_amount")) if request.POST.get("expense_amount") else "" 
        expense_category = request.POST.get("expense_category") 
        expense_reason = request.POST.get("expense_reason") 

        if expense_amount == "" or expense_category == "":
            error = "Donot leave the expense amount or category empty!"
        elif len(expense_category) > 255:
            error = "Length of expense catexpense_category cannot be greater than 255 characters!"
        else:            
            expense_category, created = ExpenseCategory.objects.get_or_create(category=expense_category)
            reported_by = Employee.objects.get(associated_user=request.user)

            expense = Expense.objects.create(
                amount=expense_amount,
                category=expense_category,
                reason=expense_reason,
                association=association,
                reported_by=reported_by
            )

            redirect_url = reverse("expenses", kwargs={"association": association})
            return redirect(redirect_url)    

    context = {"page_title": page_title, "form_action": form_action, "error": error, "expense_amount": expense_amount, "expense_category": expense_category, "expense_reason": expense_reason}
    return render(request, "expense_form.html", context)

    
def update_view(request, association, expense_id):

    form_action = "Update"
    page_title = f"{form_action} {association.title()} Expense"
    error = ""

    expense = Expense.objects.get(id=expense_id)

    expense_amount = expense.amount 
    expense_category = expense.category.category 
    expense_reason = expense.reason 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        expense_amount = int(request.POST.get("expense_amount")) if request.POST.get("expense_amount") else "" 
        expense_category = request.POST.get("expense_category") 
        expense_reason = request.POST.get("expense_reason") 

        if expense_amount == "" or expense_category == "":
            error = "Donot leave the expense amount or category empty!"
        elif len(expense_category) > 255:
            error = "Length of expense catexpense_category cannot be greater than 255 characters!"
        else:            
            expense_category, created = ExpenseCategory.objects.get_or_create(category=expense_category)

            expense.amount = expense_amount
            expense.category = expense_category
            expense.reason = expense_reason 
            expense.save()

            redirect_url = reverse("expenses", kwargs={"association": association})
            return redirect(redirect_url)
            
    context = {"page_title": page_title, "form_action": form_action, "error": error, "expense_amount": expense_amount, "expense_category": expense_category, "expense_reason": expense_reason}
    return render(request, "expense_form.html", context)

def delete_view(request, association, expense_id):

    expense = Expense.objects.get(id=expense_id)

    page_title = f"Delete {association.title()} Expense"

    item_category = "Expense"
    item = f"{expense.amount} for {expense.category.category}"

    if request.method == "POST":
        expense.delete()
        redirect_url = reverse("expenses", kwargs={"association": association})
        return redirect(redirect_url)

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
