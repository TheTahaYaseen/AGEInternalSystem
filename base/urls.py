from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("authentication/", include("authentication.urls")),
    path("bank_accounts/", include("bank_account.urls")),
    path("companys/", include("company.urls")),
    path("employees/", include("employee.urls")),
    path("roles/", include("role.urls")),
]
