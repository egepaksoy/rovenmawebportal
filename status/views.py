from django.shortcuts import render, redirect
from page_articles.models import LogArticles, NavbarFooterArticles, StaticsArticle
from .models import Statics


def log_view(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in LogArticles.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break

        articles = LogArticles.objects.get(lang=lang)
        navbar = NavbarFooterArticles.objects.get(lang=lang)
        if request.method == "POST":
            date = request.POST.get("date")
            date_text = date[8:10] + date[5:7] + date[:4]
            page = request.POST.get("page_number")
            if page == None:
                page = 1
            page = int(page)

            try:
                record_file = open("log_records/log"+str(date_text), "r")
                log_file = record_file.readlines()
                file_is_available = True
            except:
                file_is_available = False

            logs = []
            if file_is_available:
                for log_data in log_file:
                    if log_data != "":
                        log_datas = log_data.split("|")
                        logs.append({"date": log_datas[2].split(" ")[0], "time": log_datas[2].split(" ")[
                                    1], "source": log_datas[3], "type": log_datas[4], "level": log_datas[5], "data": log_datas[6]})
                record_file.close()
            log_len = len(logs)//10
            page_number = []
            if len(logs) % 10 != 1:
                log_len += 1

            for i in range(log_len):
                page_number.append(i+1)

            page_end = page*10
            page_start = page*10-10
            if page == 0:
                page_end = 10
                page_start = 0

            context = {
                "articles": articles,
                "navbar_articles": navbar,
                "logs": logs[page_start:page_end],
                "file_is_available": file_is_available,
                "date": date,
                "page_number": page_number,
                "page": page-1,
            }
            return render(request, "status/log.html", context)
        else:
            context = {
                "articles": articles,
                "navbar_articles": navbar
            }
            return render(request, "status/log.html", context=context)
    else:
        return redirect("login")


def statics(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in StaticsArticle.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break

        articles = StaticsArticle.objects.get(lang=lang)
        navbar = NavbarFooterArticles.objects.get(lang=lang)

        statics = Statics.objects.all().first()
        if statics.memory_now > statics.memory_top:
            statics.memory_top = statics.memory_now
            statics.save()
        if statics.cpu_now > statics.cpu_top:
            statics.cpu_top = statics.cpu_now
            statics.save()
        if statics.ssd_now > statics.ssd_top:
            statics.ssd_top = statics.ssd_now
            statics.save()

        context = {
            "statics": statics,
            "articles": articles,
            "navbar_articles": navbar
        }
        return render(request, "status/statics/charts.html", context)
    else:
        return redirect("login")


def packets(request):
    if request.user.is_authenticated:
        lang = "EN"
        cookie_lang = request.COOKIES.get("lang")
        for article in StaticsArticle.objects.all():
            if cookie_lang == article.lang:
                lang = article.lang
                break

        navbar = NavbarFooterArticles.objects.get(lang=lang)
        
        pcs = [{"title": "Yönetim Portu Gelen Trafik", "pcs": 24}, {"title": "Yönetim Portu Giden Trafik", "pcs": 42}, {"title": "Tek Yönlü Port Gelen Trafik", "pcs": 5}, {"title": "Tek Yönlü Port Giden Trafik", "pcs": 55}]
        
        context = {
            "navbar_articles": navbar,
            "pcs1": pcs[:2],
            "pcs2": pcs[2:]
        }

        return render(request, "status/statics/pcs.html", context)

    else:
        return redirect('login')
