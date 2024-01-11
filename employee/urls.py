from django.urls import path
from . import views

urlpatterns = [
    path("", views.employees_view, name="employees"),
    path("add", views.add_view, name="add_employee"),
    path("update/<str:employee_id>", views.update_view, name="update_employee"),
    path("delete/<str:employee_id>", views.delete_view, name="delete_employee"),
]
