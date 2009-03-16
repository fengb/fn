from django.db.models import Model
from django.db.models import CharField


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name

    @classmethod
    def hierarchical(cls):
        cls.objects.order_by('name')
