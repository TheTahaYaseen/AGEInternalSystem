from django.urls import path
from . import views

urlpatterns = [
    path("", views.customers_view, name="customers"),
    path("add", views.add_view, name="add_customer"),
    path("update/<str:customer_id>", views.update_view, name="update_customer"),
    path("delete/<str:customer_id>", views.delete_view, name="delete_customer"),
]
