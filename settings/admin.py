from django.contrib import admin
from .models import RemoteAccessSettings, LocalAccessSettings


admin.site.register(RemoteAccessSettings)
admin.site.register(LocalAccessSettings)
