from django.shortcuts import render, redirect
from .models import RemoteAccessSettings


def remote_access(request):
    if request.user.is_authenticated:
        values = RemoteAccessSettings.objects.all()
        return render(request, "settings/remote_access.html", {"value": values[0]})
    else:
        return redirect("login")
