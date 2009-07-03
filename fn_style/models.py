import re

from django.db import models
from django.contrib.auth.models import User


class Style(models.Model):
    owner = models.ForeignKey(User)
    match = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def all_from_url(cls, path):
        # Painfully poor performance
        return [style for style in cls.objects.all() if re.match(style, path)]
