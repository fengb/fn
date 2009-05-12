from django.contrib import admin
from . import models

admin.site.register(models.Manager)
admin.site.register(models.Observer)
admin.site.register(models.Updater)
