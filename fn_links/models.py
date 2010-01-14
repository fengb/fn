from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    owner = models.ForeignKey(User)
    url = models.URLField(max_length=200)
    text = models.CharField(max_length=100)
    ordinal = models.IntegerField()

    def __str__(self):
        return "%s: %s" % (owner, url)

    @classmethod
    def all_for_owners(cls):
        links_by_owner = (cls.objects.filter(owner=user).order_by('ordinal')
                              for user in User.objects.all())
        return [(links[0].owner, links)
                    for links in links_by_owner if links]
