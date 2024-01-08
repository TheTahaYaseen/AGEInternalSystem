from django.shortcuts import redirect, render

from .models import Role

# Create your views here.
def roles_view(request):
    
    page_title = "Roles"

    if not request.user.is_superuser:
        return redirect("home")

    roles = Role.objects.all()

    context = {"page_title": page_title, "roles": roles}
    return render(request, "roles.html", context)

def add_view(request):
    
    form_action = "Add"
    page_title = f"{form_action} Role"
    error = ""

    role = "" 
    access_to_shop_management = "" 
    access_to_factory_management = "" 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        role = request.POST.get("role") 
        access_to_shop_management = request.POST.get("access_to_shop_management") 
        access_to_factory_management = request.POST.get("access_to_factory_management") 

        if role == "":
            error = "Donot leave the role empty!"
        elif len(role) > 255:
            error = "Length of role cannot be greated than 255 characters!"
        else:            
            try:
                role = Role.objects.get(role=role)
                error = f"Role of {role} already exists!"
            except Role.DoesNotExist:
                if access_to_shop_management == "No":
                    access_to_shop_management = False
                else:
                    access_to_shop_management = True

                if access_to_factory_management == "No":
                    access_to_factory_management = False
                else:
                    access_to_factory_management = True

                role = Role.objects.create(
                    role=role,
                    access_to_shop_management=access_to_shop_management,
                    access_to_factory_management=access_to_factory_management
                )

                return redirect("roles")

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "role": role, "access_to_shop_management": access_to_shop_management, "access_to_factory_management": access_to_factory_management}
    return render(request, "role_form.html", context)

    
def update_view(request, role_id):

    form_action = "Update"
    page_title = f"{form_action} Role"
    error = ""

    associated_role = Role.objects.get(id=role_id)

    role = associated_role.role 
    access_to_shop_management = associated_role.access_to_shop_management 
    access_to_factory_management = associated_role.access_to_factory_management 

    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        role = request.POST.get("role") 
        access_to_shop_management = request.POST.get("access_to_shop_management") 
        access_to_factory_management = request.POST.get("access_to_factory_management") 

        if role == "":
            error = "Donot leave the role empty!"
        elif len(role) > 255:
            error = "Length of role cannot be greated than 255 characters!"
        else:            
            if role != associated_role.role:
                try:
                    role = Role.objects.get(role=role)
                    error = f"Role of {role} already exists!"
                except Role.DoesNotExist:
                    pass

            if not error:

                    if access_to_shop_management == "No":
                        access_to_shop_management = False
                    else:
                        access_to_shop_management = True

                    if access_to_factory_management == "No":
                        access_to_factory_management = False
                    else:
                        access_to_factory_management = True

                    associated_role.role = role
                    associated_role.access_to_shop_management = access_to_shop_management
                    associated_role.access_to_factory_management = access_to_factory_management
                    associated_role.save()

            return redirect("roles")

    context = {"page_title": page_title, "form_action": form_action, "error": error, 
               "role": role, "access_to_shop_management": access_to_shop_management, "access_to_factory_management": access_to_factory_management}
    return render(request, "role_form.html", context)

def delete_view(request, role_id):

    associated_role = Role.objects.get(id=role_id)

    page_title = "Delete Role"

    item_category = "Role"
    item = associated_role.role

    if request.method == "POST":
        associated_role.delete()
        return redirect("roles")

    context = {"page_title": page_title, "item_category": item_category, "item": item}
    return render(request, "delete.html", context)
