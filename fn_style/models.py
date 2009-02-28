from django.db.models import Model
from django.db.models import CharField, TextField
from django.db.models import ForeignKey
from django.contrib.auth.models import User


class Style(Model):
    owner = ForeignKey(User)
    body = TextField()

    @classmethod
    def for_url(cls, url):
        return [url.style for url in Url.objects.filter(match=url)]


class Url(Model):
    style = ForeignKey(Style)
    match = CharField(max_length=100)
