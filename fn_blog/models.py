from django.db.models import Model
from django.db.models import ForeignKey, ManyToManyField
from django.db.models import CharField, TextField, DateField, BooleanField
from django.contrib.auth.models import User
from fn_category.models import Category


class Blog(Model):
    owner = ForeignKey(User)
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

    def entries_by_user(self, user):
        if self.owner == user:
            return self.entry_set.order_by('-created')
        else:
            return self.entry_set.filter(public=True).order_by('-created')


class Entry(Model):
    blog = ForeignKey(Blog)
    title = CharField(max_length=100)
    body = TextField()
    public = BooleanField()
    categories = ManyToManyField(Category)
    created = DateField(auto_now_add=True)

    def __str__(self):
        return self.title
