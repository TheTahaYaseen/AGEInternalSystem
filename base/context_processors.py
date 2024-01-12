from django.contrib.auth.models import User
from employee.models import Employee

def get_employee_role(request):
    role = None
    if request.user.is_authenticated:
        try:
            employee = Employee.objects.get(associated_user=request.user)
            role = employee.associated_role if employee else None
        except Employee.DoesNotExist:
            pass

    return role
    
def access_to_shop_management_context(request):
    role = get_employee_role(request)
    has_access = role.access_to_shop_management if role else False
    return {"has_access_to_shop_management": has_access}

def access_to_factory_management_context(request):
    role = get_employee_role(request)
    has_access = role.access_to_factory_management if role else False
    return {"has_access_to_factory_management": has_access}

def access_to_warehouse_management_context(request):
    role = get_employee_role(request)
    has_access = role.access_to_warehouse_management if role else False
    return {"has_access_to_warehouse_management": has_access}