from django.urls import path
from . import views


urlpatterns = [
    path('ftp-settings', views.ftp_settings, name="ftp_settings"),
]
