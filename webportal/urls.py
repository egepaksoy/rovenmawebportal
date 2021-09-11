from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('', include('status.urls')),
    path('', include('settings.urls')),
    path('', include('page_articles.urls')),
<<<<<<< HEAD
    path('', include('video_transfer.urls')),
    path('', include('ftp_settings.urls')),
=======
>>>>>>> aba21ce77ea5bdd24dc3655e915e89772037ce9e
]

urlpatterns += staticfiles_urlpatterns()
