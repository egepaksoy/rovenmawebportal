from django.urls import path 
from . import views


urlpatterns = [
    path('video-transfer-settings/', views.settings, name='video_transfer_settings'),
    path('input-settings', views.input_view, name='video_input'),
    path('input_settings/save_input_settings', views.save_input, name='save_input_settings'),
    path('input_settings/save_output_settings', views.save_output, name='save_output_settings'),
]
