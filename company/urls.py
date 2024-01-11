from django.urls import path
from . import views

urlpatterns = [
    path("", views.companies_view, name="companies"),
    path("add", views.add_view, name="add_company"),
    path("update/<str:company_id>", views.update_view, name="update_company"),
    path("delete/<str:company_id>", views.delete_view, name="delete_company"),
]
