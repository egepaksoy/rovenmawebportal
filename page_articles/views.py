from django.shortcuts import redirect


def change_lang(request, lang):
    response = redirect("home")
    response.set_cookie("lang", lang)
    return response
