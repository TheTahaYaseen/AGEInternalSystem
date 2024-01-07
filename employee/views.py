from django.shortcuts import render

# Create your views here.
def employees_view(request):
    context = {}
    return render(request, "employees.html", context)