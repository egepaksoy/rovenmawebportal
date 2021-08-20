from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('status.urls')),
    path('', include('settings.urls')),
    path('', include('page_articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()