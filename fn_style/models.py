from django.db import models
from django.contrib.auth.models import User


class Style(models.Model):
    owner = models.ForeignKey(User)
    body = models.TextField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def all_from_url(cls, path):
        # Be stupid for now. Add in support for breadcrumbs later
        return cls.objects.all()
