from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class TwitterUser(models.Model):
    django_user = models.OneToOneField(User)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class UpdateWatcher(models.Model):
    user = models.ForeignKey(TwitterUser)
    content_type = models.ForeignKey(ContentType)
    active = models.BooleanField()

    def __str__(self):
        return '%s: %s' % (self.user.username, self.content_type)
