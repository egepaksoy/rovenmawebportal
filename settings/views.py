from django.shortcuts import render, redirect
from .models import *
from page_articles.models import RemoteAccessArticles, LocalAccessArticles, TimeSettingsArticles, NavbarFooterArticles


# TODO: yanlarda küçük yardım balonları olucak
def remote_access_view(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in RemoteAccessArticles.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break
        articles = RemoteAccessArticles.objects.get(lang=lang)
        navbar = NavbarFooterArticles.objects.get(lang=lang)
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

            return render(request, "settings/remote_access.html", {"value": values, "articles": articles, "navbar_articles": navbar})
    else:
        return redirect("login")


def local_access_view(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in LocalAccessArticles.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break
        articles = LocalAccessArticles.objects.get(lang=lang)
        navbar = NavbarFooterArticles.objects.get(lang=lang)
        values = LocalAccessSettings.objects.all().first()

        if request.method == "POST":
            if request.POST.get("open_cli") != "on":
                values.baud_rate = request.POST.get("baud_rate")
                values.data_bits = request.POST.get("data_bits")
                values.stop_bits = request.POST.get("stop_bits")
                values.parity = request.POST.get("parity")
                
                if request.POST.get("open_cli") == "on":
                    values.open_cli = True
                else:
                    values.open_cli = False
            else:
                    values.open_cli = True

            values.save()

            return redirect("local_access")

        return render(request, "settings/local_access.html", {"values": values, "articles": articles, "navbar_articles": navbar})
    else:
        return redirect("login")


def time_settings_view(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in TimeSettingsArticles.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break
        articles = TimeSettingsArticles.objects.get(lang=lang)
        navbar = NavbarFooterArticles.objects.get(lang=lang)
        times = [0]
        for time in range(24):
            times.append(time+1)

        time_setting = TimeSettings.objects.all().first()

        if request.method == "POST":
            time_setting.use_ntp = request.POST.get("ntp_use")
            time_setting.time = request.POST.get("time")
            time_setting.date = request.POST.get("date")
            time_setting.server1 = request.POST.get("server1")
            time_setting.server2 = request.POST.get("server2")
            time_setting.timezone = request.POST.get("timezone")
            time_setting.save()
            return redirect("time_settings")
        else:
            hour = str(time_setting.time.hour)
            minute = str(time_setting.time.minute)
            day = str(time_setting.date.day)
            month = str(time_setting.date.month)
            if len(hour) == 1:
                hour = "0"+hour
            if len(minute) == 1:
                minute = "0"+minute
            if len(month) == 1:
                month = "0"+month
            if len(day) == 1:
                day = "0"+day
            context = {
                "times": times,
                "articles": articles,
                "time_settings": time_setting,
                "navbar_articles": navbar,
                "time": hour+":"+minute,
                "date": str(time_setting.date.year)+"-"+month+"-"+day
            }
            return render(request, "settings/time_settings.html", context=context)
    else:
        return redirect("login")
