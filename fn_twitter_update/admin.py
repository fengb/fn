from django.contrib import admin
from . import models

admin.site.register(models.TwitterUser)
admin.site.register(models.UpdateWatcher)
