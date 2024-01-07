from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def home_view(request):
    page_title = "Home"
    context = {"page_title": page_title}
    return render(request, "home.html", context)