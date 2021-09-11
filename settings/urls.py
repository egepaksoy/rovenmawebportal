from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('remote-access/', views.remote_access_view, name="remote_access"),
    path('local-access/', views.local_access_view, name="local_access"),
    path('time-settings/', views.time_settings_view, name="time_settings"),
=======
    path('remote_access/', views.remote_access_view, name="remote_access"),
    path('local_access/', views.local_access_view, name="local_access"),
    path('time_settings/', views.time_settings_view, name="time_settings"),
>>>>>>> aba21ce77ea5bdd24dc3655e915e89772037ce9e
]
