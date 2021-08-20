from django.urls import path
from . import views


urlpatterns = [
    path('lang/<str:lang>', views.change_lang, name="change_lang")
]