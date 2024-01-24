from django.urls import path
from . import views

urlpatterns = [
    path("<str:association>/", views.inventory_view, name="inventory"),

    path("<str:association>/fibre_bale/add", views.add_fibre_bale_view, name="add_fibre_bale"),
    path("<str:association>/fibre_bale/<str:fibre_bale_id>/update", views.update_fibre_bale_view, name="update_fibre_bale"),
    path("<str:association>/fibre_bale/<str:fibre_bale_id>/delete", views.delete_fibre_bale_view, name="delete_fibre_bale"),

    path("<str:association>/rope_bundle/add", views.add_rope_bundle_view, name="add_rope_bundle"),
    path("<str:association>/rope_bundle/<str:rope_bundle_id>/update", views.update_rope_bundle_view, name="update_rope_bundle"),
    path("<str:association>/rope_bundle/<str:rope_bundle_id>/delete", views.delete_rope_bundle_view, name="delete_rope_bundle"),
]
