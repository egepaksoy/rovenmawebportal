from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def register(request):
  if request.user.is_authenticated:
    
    form = CreateUserForm()

    if request.method == "POST":
      form = CreateUserForm(request.POST)
      password1 = request.POST.get("password1")
      print(password1)
      if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        messages.success(request, "User created: " + user)
        return redirect('home')

    context = {"form": form}

    return render(request, "register.html", context)
  else:
    return redirect('login')


def login_view(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = authenticate(request ,username=username, password=password)
      
      if user is not None:
        login(request, user)
        return redirect('home')
      
      else:
        messages.info(request, 'Incorrect username or password')

    return render(request, "login.html")


def logout_view(request):
  logout(request)
  return redirect("login")


@login_required(login_url="login")
def home(request):
  return render(request, "home.html")