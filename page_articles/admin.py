from django.contrib import admin
from .models import *


admin.site.register(LogArticles)
admin.site.register(RemoteAccessArticles)
admin.site.register(LocalAccessArticles)
admin.site.register(TimeSettingsArticles)
