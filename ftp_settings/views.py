from django.shortcuts import render, redirect
from .models import *
from page_articles.models import *


def ftp_settings_view(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in RemoteAccessArticles.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break
        ftp_settings = Ftp_settings.objects.all().first()
        navbar_footer = NavbarFooterArticles.objects.get(lang=lang)
        if request.method == "POST":
            if request.POST.get("enable_pure_db") == "on":
                print(request.POST.get("enable_pure_db"))
                enable_pure_db = True
            else:
                enable_pure_db = False
            if request.POST.get("enable_pam") == "on":
                enable_pam = True
            else:
                enable_pam = False
            if request.POST.get("enable_ssl_cert") == "on":
                enable_ssl_cert = True
            else:
                enable_ssl_cert = False
            if request.POST.get("enable_verbose_log") == "on":
                enable_verbose_log = True
            else:
                enable_verbose_log = False
            if request.POST.get("enable_no_anonymous") == "on":
                enable_no_anonymous = True
            else:
                enable_no_anonymous = False
            ftp_settings.enable_pure_db = enable_pure_db
            ftp_settings.enable_pam = enable_pam
            ftp_settings.enable_ssl_cert = enable_ssl_cert
            ftp_settings.enable_verbose_log = enable_verbose_log
            ftp_settings.enable_no_anonymous = enable_no_anonymous
            ftp_settings.ssl_cert_path = request.POST.get("ssl_cert_path")
            ftp_settings.tls = request.POST.get("tls")
            ftp_settings.tls_chiper_suite = request.POST.get(
                "tls_cipher_suite")
            ftp_settings.supported_items = request.POST.get("supported_items")
            ftp_settings.syslog_facility_type = request.POST.get(
                "syslog_facility_type")
            ftp_settings.pure_ftp_base_path = request.POST.get(
                "pure_ftp_base_path")
            ftp_settings.pure_ftp_config_file = request.POST.get(
                "pure_ftp_config_file")
            ftp_settings.max_clients_number = request.POST.get(
                "max_clients_number")
            ftp_settings.max_clients_per_ip = request.POST.get(
                "max_clients_per_ip")
            ftp_settings.save()

            return redirect("ftp_settings")
        else:
            if ftp_settings.enable_pure_db:
                enable_pure_db = "true"
            else:
                enable_pure_db = "false"
            if ftp_settings.enable_pam:
                enable_pam = "true"
            else:
                enable_pam = "false"
            if ftp_settings.enable_ssl_cert:
                enable_ssl_cert = "true"
            else:
                enable_ssl_cert = "false"
            if ftp_settings.enable_verbose_log:
                enable_verbose_log = "true"
            else:
                enable_verbose_log = "false"
            if ftp_settings.enable_no_anonymous:
                enable_no_anonymous = "true"
            else:
                enable_no_anonymous = "false"
            context = {
                "ftp_settings": ftp_settings,
                "enable_pure_db": enable_pure_db,
                "enable_pam": enable_pam,
                "enable_ssl_cert": enable_ssl_cert,
                "enable_verbose_log": enable_verbose_log,
                "enable_no_anonymous": enable_no_anonymous,
                "navbar_articles": navbar_footer
            }
            return render(request, "ftp_settings/index.html", context=context)

    else:
        return redirect('login')
