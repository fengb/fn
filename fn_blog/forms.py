from django.forms import ModelForm
from . import models


class Blog(ModelForm):
    class Meta(object):
        model = models.Blog


class Entry(ModelForm):
    class Meta(object):
        model = models.Entry
