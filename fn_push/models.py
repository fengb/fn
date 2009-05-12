from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from . import updaters

try:
    from multiprocessing import Process
except ImportError:
    # Not 2.6 so use threads instead
    from threading import Thread as Process


class Manager(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

    def send(self, message):
        for relation in dir(self):
            if relation.endswith('updater'):
                updater = getattr(self, relation)
                p = Process(target=updater.send, args=(message,))
                p.start()


class Observer(models.Model):
    manager = models.ForeignKey(Manager)
    subject = models.ForeignKey(ContentType)
    message = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return '%s: %s' % (self.manager, self.subject)

    def send(self, instance):
        self.manager.send(self.message % vars(instance))


class Updater(models.Model):
    manager = models.OneToOneField(Manager)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    updater = models.CharField(max_length=100, choices=updaters.choices())

    def __str__(self):
        return str(self.manager)

    def send(self, message):
        updaters[self.updater](self.username, self.password, message)
