from django.urls import path
from . import views

urlpatterns = [
    path("<str:association>/", views.expenses_view, name="expenses"),
    path("<str:association>/add", views.add_view, name="add_expense"),
    path("<str:association>/update/<str:expense_id>", views.update_view, name="update_expense"),
    path("<str:association>/delete/<str:expense_id>", views.delete_view, name="delete_expense"),
]
