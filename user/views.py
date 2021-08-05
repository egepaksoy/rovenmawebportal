from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def delete_user(request, username):
    if request.method == "POST" and request.user != username:
        try:
            user = User.objects.get(username=username)
            user.delete()
            print("kullanıcı silindi")
            messages.success(request, "Kullanıcı Silindi: " + username)

        except User.DoesNotExist:
            messages.error(request, "Kullanıcı Bulunamadı")

    return redirect('register')


def register(request):
    if request.user.is_authenticated and request.user.is_superuser:
        lang = request.COOKIES.get("lang")
        if not request.COOKIES.get("lang"):
            lang = "EN"

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if form.is_valid():
                form.save()
                username = form.cleaned_data.get("username")
                messages.success(request, "Kullanıcı Oluşturuldu: " + username)
                usertype = request.POST.get("usertype")

                user = User.objects.get(username=username)

                if usertype == "superuser":
                    user.is_staff = True
                    user.is_superuser = True
                    user.save()
                elif usertype == "staff":
                    user.is_staff = True
                    user.is_superuser = False
                    user.save()

                return redirect('register')

            messages.info(request, form.errors)

        context = {
            "form": form,
            "users": User.objects.all(),
        }

        return render(request, "user/register.html", context)

    if request.user.is_superuser == False:
        messages.info(request, "Bu alana erişmek için Super Admin olmanız gerekir.")
        return redirect("home")

    else:
        return redirect('login')


def login_view(request):
    if request.user.is_authenticated:
        lang = request.COOKIES.get("lang")
        if not request.COOKIES.get("lang"):
            lang = "EN"
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

        return render(request, "user/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def home(request):
    if request.user.is_authenticated:
        if not request.COOKIES.get("lang"):
            response = render(request, "home.html")
            response.set_cookie("lang", "EN")
            return response
        else:
            return render(request, "home.html")
    else:
        return redirect("login")
