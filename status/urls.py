from django.urls import path
from . import views


urlpatterns = [
    path('log/', views.log_view, name="log"),
    path('statics/', views.statics, name="statics"),
]