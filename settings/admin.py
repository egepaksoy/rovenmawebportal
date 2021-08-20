from django.contrib import admin
from .models import *


admin.site.register(RemoteAccessSettings)
admin.site.register(LocalAccessSettings)
admin.site.register(TimeSettings)
