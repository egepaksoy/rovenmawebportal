from django.urls import path 
from . import views


urlpatterns = [
    path('video-transfer-settings/', views.settings, name='video_transfer_settings'),
]
