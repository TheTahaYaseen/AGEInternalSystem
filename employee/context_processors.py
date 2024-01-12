from .models import Employee

def access_to_context(request):

    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(associated_user=request.user)
            role = employee.associated_role if employee else None
        except Employee.DoesNotExist:
            role = None

    if role:
        has_access_to_shop_management = role.has_access_to_shop_management 
        has_access_to_factory_management = role.has_access_to_factory_management 
        has_access_to_warehouse_management = role.has_access_to_warehouse_management 

    return {"has_access_to_shop_management": has_access_to_shop_management, "has_access_to_factory_management": has_access_to_factory_management, "has_access_to_warehouse_management": has_access_to_warehouse_management}
