from django.db.models import Model
from django.db.models import CharField, ForeignKey


class Category(Model):
    name = CharField(max_length=100)
    parent = ForeignKey('self', null=True, blank=True)

    def children(self):
        return self.category_set.order_by('name')

    def __str__(self):
        return self.name

    @classmethod
    def hierarchical(cls):
        return cls.objects.filter(parent=None).order_by('name')
