from django.urls import path
from . import views

urlpatterns = [
    path("", views.bank_accounts_view, name="bank_accounts"),
    path("add", views.add_view, name="add_bank_account"),
    path("update/<str:bank_account_id>", views.update_view, name="update_bank_account"),
    path("delete/<str:bank_account_id>", views.delete_view, name="delete_bank_account"),
]
