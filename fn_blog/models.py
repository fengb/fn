from django.db.models import ForeignKey, ManyToManyField
from django.db.models import CharField, TextField, DateField, BooleanField
from django.contrib.auth.models import User
>>>>>>> other

<<<<<<< local
from django.contrib.auth.models import User
from fn_category.models import Category
=======
>>>>>>> other


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
    categories = ManyToManyField(Category)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
