from django.db import models
from django.db.models import Model
from django.db.models import ForeignKey, CharField, TextField, DateField
from django.contrib.auth.models import User

from django.db.models import permalink

import string

alphanumeric = string.lowercase + string.digits


class Blog(Model):
    owner = ForeignKey(User)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Entry(Model):
    blog = ForeignKey(Blog)
    title = CharField(max_length=100)
    internal = CharField(max_length=10, unique=True)
    body = TextField()
    created = DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self):
        self.internal = ''.join(c for c in self.title.lower() if c in alphanumeric)[:10]
        Model.save(self)
