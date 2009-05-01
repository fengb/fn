from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from . import twitter
from .models import TwitterUser


class TweetSender(object):
    def __init__(self, sender, instance):
        self.sender = sender
        self.instance = instance

    @property
    def user(self):
        if not hasattr(self, '_user'):
            self._user = TwitterUser.objects.get(django_user=self.instance.owner)
        return self._user

    @property
    def watcher(self):
        if not hasattr(self, '_watcher'):
            sender_type = ContentType.objects.get_for_model(self.sender)
            self._watcher = self.user.updatewatcher_set.get(content_type=sender_type)
        return self._watcher

    @property
    def message(self):
        return self.watcher.message % vars(self.instance)

    def tweetable(self):
        try:
            return self.watcher.active
        except models.ObjectDoesNotExist:
            return False
        except models.AttributeError:
            return False

    def send(self):
        twitter.Twitter(self.user.username, self.user.password).statuses.update(status=self.message)

def send_tweet(sender, instance, *args, **kwargs):
    sender = TweetSender(sender, instance)
    if sender.tweetable():
        sender.send()

models.signals.post_save.connect(send_tweet)
