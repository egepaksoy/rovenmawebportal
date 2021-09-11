from django.urls import path
from . import views


urlpatterns = [
    path('remote-access/', views.remote_access_view, name="remote_access"),
    path('local-access/', views.local_access_view, name="local_access"),
    path('time-settings/', views.time_settings_view, name="time_settings"),
]
