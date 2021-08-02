from django.urls import path
from . import views


urlpatterns = [
    path('remote_access/', views.remote_access, name="remote_access"),
    path('local_access/', views.local_access, name="local_access"),
    path('time_settings/', views.time_settings, name="time_settings"),
]
