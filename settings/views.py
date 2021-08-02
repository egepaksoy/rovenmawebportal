from django.shortcuts import render, redirect
from .models import RemoteAccessSettings, LocalAccessSettings

# TODO: yanlarda küçük yardım balonları olucak
def remote_access(request):
    if request.user.is_authenticated:
        values = RemoteAccessSettings.objects.all().first()
        if request.method == "POST":
            values.dhcp_enabled = request.POST.get("dhcp_setting")
            values.ip_address = request.POST.get("ip_address")
            values.port = request.POST.get("port")
            values.subnet_mask = request.POST.get("subnet_mask")
            values.broadcast_address = request.POST.get("broadcast_address")
            values.gateway_address = request.POST.get("gateway_address")
            values.dns_address = request.POST.get("dns_address")
            values.dhcp_address = request.POST.get("dhcp_address")
            values.save()

            return redirect("remote_access")
        else:
            if values.dhcp_enabled:
                enable = "selected"
                disable = ""
            else:
                enable = ""
                disable = "selected"

            return render(request, "settings/remote_access.html", {"value": values})
    else:
        return redirect("login")


def local_access(request):
    if request.user.is_authenticated:
        values = LocalAccessSettings.objects.all().first()
        if request.method == "POST":
            values.baud_rate = request.POST.get("baud_rate")
            values.data_bits = request.POST.get("data_bits")
            values.stop_bits = request.POST.get("stop_bits")
            values.parity = request.POST.get("parity")
            values.save()

            return redirect("local_access")

        return render(request, "settings/local_access.html", {"values": values})
    else:
        return redirect("login")


def time_settings(request):
    if request.user.is_authenticated:

        return render(request, "settings/time_settings.html")
    else:
        return redirect("login")
