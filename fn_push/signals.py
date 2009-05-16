from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.db.models import signals

from . import models


def callback(sender, instance, created, **kwargs):
    if created and hasattr(instance, 'user'):
        try:
            sender_type = ContentType.objects.get_for_model(sender)
            manager = models.Manager.objects.get(user=instance.user)
            observer = manager.observer_set.get(subject=sender_type)
        except ObjectDoesNotExist:
            pass
        else:
            observer.send(instance)

signals.post_save.connect(callback, weak=False)
