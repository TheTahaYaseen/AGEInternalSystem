from django.urls import path
from . import views

urlpatterns = [
    path("", views.roles_view, name="roles"),
    path("add", views.add_view, name="add_role"),
    path("update/<str:role_id>", views.update_view, name="update_role"),
    path("delete/<str:role_id>", views.delete_view, name="delete_role"),
]
