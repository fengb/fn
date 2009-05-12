from functools import partial

from . import twitter


class UpdaterCache(object):
    def __init__(self):
        self.funcs = {}

    def __getitem__(self, index):
        return self.funcs[index]

    def __setitem__(self, index, value):
        self.funcs[index] = value

    def choices(self):
        return [(name, name) for name in self.funcs]


updater_cache = UpdaterCache()
choices = updater_cache.choices

def register(arg):
    """Register a function to be used as an updater
    Note - the arguments must be (username, password, message)

    >>> @register
    >>> def awesome(username, password, message):
    >>>     print username, password
    >>>     print message

    >>> @register(name='awesome')
    >>> def lessawesome(username, password, message):
    >>>     print username, password
    >>>     print message
    """
    if callable(arg):
        updater_cache[arg.__name__] = arg
        return arg
    else:
        def decorator(func):
            updater_cache[arg] = func
            return func
        return decorator


@register('twitter')
def twitterupdate(username, password, message):
    twitter.Twitter(username, password).statuses.update(status=message)
