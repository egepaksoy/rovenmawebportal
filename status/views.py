from django.shortcuts import render, redirect
from .models import Log


def log_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            date = request.POST.get("date")
            logs = Log.objects.filter(date__range=[date, date])
            context = {
                "logs": logs
            }
            return render(request, "status/log.html", context)
        else:
            return render(request, "status/log.html")
    else:
        return redirect("login")
