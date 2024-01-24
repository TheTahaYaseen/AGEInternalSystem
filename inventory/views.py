from django.shortcuts import redirect, render
from django.urls import reverse
from employee.context_processors import access_to_context

from employee.models import Employee
from .models import FibreBale, RopeBundle

# Create your views here.
def inventory_view(request, association):
    
    page_title = f"{association.title()} Inventory"

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")

    fibre_bales = FibreBale.objects.filter(association=association)
    rope_bundles = RopeBundle.objects.filter(association=association)

    context = {"page_title": page_title, "fibre_bales": fibre_bales, "rope_bundles": rope_bundles}
    return render(request, "inventory.html", context)

def add_fibre_bale_view(request, association):
    
    form_action = "Add"
    page_title = f"{form_action} {association.title()} Fibre Bale"
    error = ""

    fibre_bale_weight = "" 

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")
    
    if request.method == "POST":
        fibre_bale_weight = int(request.POST.get("fibre_bale_weight")) if request.POST.get("fibre_bale_weight") else "" 

        if fibre_bale_weight == "":
            error = "Donot leave the fibre bale weight empty!"
        else:            
            added_by = Employee.objects.get(associated_user=request.user)

            fibre_bale = FibreBale.objects.create(
                weight=fibre_bale_weight,
                association=association,
                added_by=added_by
            )

            redirect_url = reverse("inventory", kwargs={"association": association})
            return redirect(redirect_url)    

    context = {"page_title": page_title, "form_action": form_action, "error": error, "fibre_bale_weight": fibre_bale_weight}
    return render(request, "fibre_bale_form.html", context)

    
def update_fibre_bale_view(request, association, fibre_bale_id):

    form_action = "Update"
    page_title = f"{form_action} {association.title()} Fibre Bale"
    error = ""

    fibre_bale = FibreBale.objects.get(id=fibre_bale_id)

    fibre_bale_weight = fibre_bale.weight 

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")
    
    if request.method == "POST":
        fibre_bale_weight = int(request.POST.get("fibre_bale_weight")) if request.POST.get("fibre_bale_weight") else "" 

        if fibre_bale_weight == "":
            error = "Donot leave the fibre bale weight empty!"
        else:            
            fibre_bale.weight = fibre_bale_weight
            fibre_bale.save()

            redirect_url = reverse("inventory", kwargs={"association": association})
            return redirect(redirect_url)
            
    context = {"page_title": page_title, "form_action": form_action, "error": error, "fibre_bale_weight": fibre_bale_weight}
    return render(request, "fibre_bale_form.html", context)

def delete_fibre_bale_view(request, association, fibre_bale_id):

    fibre_bale = FibreBale.objects.get(id=fibre_bale_id)

    page_title = f"Delete {association.title()} Fibre Bale"

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")

    item_category = "Fibre Bale"
    item = f"With weight: {fibre_bale.weight}"

    if request.method == "POST":
        fibre_bale.delete()
        redirect_url = reverse("inventory", kwargs={"association": association})
        return redirect(redirect_url)

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)

def add_rope_bundle_view(request, association):
    
    form_action = "Add"
    page_title = f"{form_action} {association.title()} Rope Bundle"
    error = ""

    rope_bundle_weight = "" 
    rope_bundle_size = "" 

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")
    
    if request.method == "POST":
        rope_bundle_weight = int(request.POST.get("rope_bundle_weight")) if request.POST.get("rope_bundle_weight") else "" 
        rope_bundle_size = int(request.POST.get("rope_bundle_size")) if request.POST.get("rope_bundle_size") else "" 

        if rope_bundle_weight == "":
            error = "Donot leave the rope bundle weight empty!"
        else:            
            added_by = Employee.objects.get(associated_user=request.user)

            rope_bundle = RopeBundle.objects.create(
                weight=rope_bundle_weight,
                size=rope_bundle_size,
                association=association,
                added_by=added_by
            )

            redirect_url = reverse("inventory", kwargs={"association": association})
            return redirect(redirect_url)    

    context = {"page_title": page_title, "form_action": form_action, "error": error, "rope_bundle_weight": rope_bundle_weight, "rope_bundle_size": rope_bundle_size}
    return render(request, "rope_bundle_form.html", context)

    
def update_rope_bundle_view(request, association, rope_bundle_id):

    form_action = "Update"
    page_title = f"{form_action} {association.title()} Rope Bundle"
    error = ""

    rope_bundle = RopeBundle.objects.get(id=rope_bundle_id)

    rope_bundle_weight = rope_bundle.weight 
    rope_bundle_size = rope_bundle.size 

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")
    
    if request.method == "POST":
        rope_bundle_weight = int(request.POST.get("rope_bundle_weight")) if request.POST.get("rope_bundle_weight") else "" 
        rope_bundle_size = int(request.POST.get("rope_bundle_size")) if request.POST.get("rope_bundle_size") else "" 

        if rope_bundle_weight == "":
            error = "Donot leave the rope bundle weight empty!"
        else:            
            rope_bundle.weight = rope_bundle_weight
            rope_bundle.size = rope_bundle_size
            rope_bundle.save()

            redirect_url = reverse("inventory", kwargs={"association": association})
            return redirect(redirect_url)
            
    context = {"page_title": page_title, "form_action": form_action, "error": error, "rope_bundle_weight": rope_bundle_weight, "rope_bundle_size": rope_bundle_size}
    return render(request, "rope_bundle_form.html", context)

def delete_rope_bundle_view(request, association, rope_bundle_id):

    rope_bundle = RopeBundle.objects.get(id=rope_bundle_id)

    page_title = f"Delete {association.title()} Rope Bundle"

    access = access_to_context(request)

    if not access[f"has_access_to_{association}_management"]:
        return redirect("home")

    item_category = "Rope Bundle"
    item = f"With weight; {rope_bundle.weight} and of size; {rope_bundle.size} mm"

    if request.method == "POST":
        rope_bundle.delete()
        redirect_url = reverse("inventory", kwargs={"association": association})
        return redirect(redirect_url)

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
