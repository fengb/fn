from django.db.models import Model
from django.db.models import CharField, TextField
from django.db.models import ForeignKey
from django.contrib.auth.models import User


class Style(Model):
    owner = ForeignKey(User)
    body = TextField()

    def __str__(self):
        return str(self.id)

    @classmethod
    def all_from_url(cls, path):
        # Be stupid for now. Add in support for breadcrumbs later
        return cls.objects.all()
