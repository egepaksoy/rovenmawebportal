from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def delete_user(request, username):
  if request.method == "POST":
    try:
        user = User.objects.get(username=username)
        user.delete()
        print("kullanıcı silindi")
        messages.success(request, "Kullanıcı Silindi: "+username)

    except User.DoesNotExist:
        messages.error(request, "Kullanıcı Bulunamadı")
  return redirect('register')


def register(request):
  if request.user.is_authenticated:

    form = CreateUserForm()

    if request.method == "POST":
      form = CreateUserForm(request.POST)
      password1 = request.POST.get('password1')
      password2 = request.POST.get('password2')

      if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        messages.success(request, "Kullanıcı Oluşturuldu: " + user)
        return redirect('register')

      elif password2 != password1:
        messages.info(request, "Şifreler Birbirinden Farklı")

      else:
        messages.info(request, "Kullanıcı sisteme kayıtlı")
    context = {
      "form": form,
      "users": User.objects.all(),
      }

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
      user = authenticate(request, username=username, password=password)

      if user is not None:
        login(request, user)
        return redirect('home')

      else:
        messages.info(request, 'Kullanıcı Adı Veya Parola Hatalı')

    return render(request, "login.html")


def logout_view(request):
  logout(request)
  return redirect("login")


@login_required(login_url="login")
def home(request):
  return render(request, "home.html")