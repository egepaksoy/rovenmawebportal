from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('delete/<str:username>', views.delete_user, name='delete'),
    path('change-password/<str:username>/', views.pass_change, name='pass_change'),
    path('authorization', views.authorization, name="auth"),
]
