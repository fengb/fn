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

    @permalink
    def get_absolute_url(self):
        return 'fn_blog.blog.__member__', [self.id]


class Entry(Model):
    blog = ForeignKey(Blog)
    title = CharField(max_length=100)
    body = TextField()
    created = DateField(auto_now=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return 'fn_blog.entry.__member__', [self.id]
