from django.db import models
from django.contrib.auth.models import User
from fn_category.models import Category


class Blog(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'fn_blog.views.blog', str(self.id)

    def entries_by_user(self, user):
        if self.owner == user:
            return self.entry_set.order_by('-created')
        else:
            return self.entry_set.filter(public=True).order_by('-created')


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=100)
    body = models.TextField()
    public = models.BooleanField()
    categories = models.ManyToManyField(Category)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'fn_blog.views.entry', str(self.id)

    @property
    def owner(self):
        return self.blog.owner
