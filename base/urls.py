from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("authentication/", include("authentication.urls")),
    path("bank_accounts/", include("bank_account.urls")),
    path("companies/", include("company.urls")),
    path("customers/", include("customer.urls")),
    path("employees/", include("employee.urls")),
    path("expenses/", include("expense.urls")),
    path("roles/", include("role.urls")),
]
