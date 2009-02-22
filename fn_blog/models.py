from django.db.models import Model
from django.db.models import ForeignKey, ManyToManyField
from django.db.models import CharField, TextField, DateTimeField, BooleanField
from django.db.models import permalink

from django.contrib.auth.models import User
from fn_category.models import Category


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
    public = BooleanField()
    categories = ManyToManyField(Category)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return 'fn_blog.entry.__member__', [self.id]
