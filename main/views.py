from django.shortcuts import render,redirect
from main.forms import loginForm,registerForm
# Create your views here.
def home(request):
    return render(request,"main/index.html")

def login(request):
    if request.method =="POST":
        form = loginForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = loginForm()
    return render(request,"main/login.html",{"form":form})

def register(request):
    if request.method =="POST":
        form = registerForm(request.POST)
        if form.is_valid():
            return redirect("login")
    else:
        form = registerForm()
    return render(request,"main/register.html",{"form":form})