from django.db import models
from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CharField, TextField, DateField, BooleanField
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
    body = TextField()
    public = BooleanField()
    created = DateField(auto_now_add=True)

    def __str__(self):
        return self.title
