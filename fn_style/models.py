from django.db.models import Model
from django.db.models import CharField, TextField
from django.db.models import ForeignKey
from django.contrib.auth.models import User


class Style(Model):
    owner = ForeignKey(User)
    body = TextField()

    def __str__(self):
        return str(self.id)


class Url(Model):
    style = ForeignKey(Style)
    match = CharField(max_length=100)

    def __str__(self):
        return self.match

    @classmethod
    def styles(cls, path):
        # TODO: Make this structure less confusing
        # This isn't reversed. We need to find all entries that matches.
        urls = Url.objects.extra(where=['%s LIKE match'], params=[path])
        return [url.style for url in urls]
