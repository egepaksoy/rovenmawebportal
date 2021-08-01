from django.shortcuts import render, redirect


def remote_access(request):
    if request.user.is_authenticated:
        return render(request, "settings/remote_access.html")
    else:
        return redirect("login")
