from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):

    error = ""
    page_title = "Login"
    username = ""
    password = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            error = "Please fillout both fields!"
        else:
            try:
                user = User.objects.get(username=username)
            
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("home") 
                else:
                    error = "Username or password is incorrect!"

            except User.DoesNotExist:
                error = "User does not exist!"

    context = {"page_title": page_title, "error": error, "username": username, "password": password}
    return render(request, "login.html", context)

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("login")   
