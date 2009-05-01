from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from . import twitter
from .models import TwitterUser


class TweetSender(object):
    def __init__(self, sender, instance):
        self.sender = sender
        self.instance = instance

        if hasattr(sender, 'owner'):
            try:
                self.user = TwitterUser.objects.get(django_user=self.instance.owner)
            except models.ObjectDoesNotExist:
                self.user = None
        else:
            self.user = None

    def tweetable(self):
        if self.user:
            try:
                sender_type = ContentType.objects.get_for_model(self.sender)
                watcher = self.user.updatewatcher_set.get(content_type=sender_type)
                return watcher.active
            except models.ObjectDoesNotExist:
                return False
        else:
            return False

    def send(self):
        twitter.Twitter(self.user.username, self.user.password).statuses.update(status=self.message())

    def message(self):
        return 'Updated %s(%s): %s' % (self.sender.__name__, self.instance,
                                   settings.URL_BASE + self.instance.get_absolute_url())

def send_tweet(sender, instance, *args, **kwargs):
    sender = TweetSender(sender, instance)
    if sender.tweetable():
        sender.send()

models.signals.post_save.connect(send_tweet)
