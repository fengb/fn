from django.conf import settings
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

    def add(self, arg):
        """Add a function to be used as an updater
        Note - the decorated function arguments must be (username, password, message)

        >>> @cache.register
        >>> def awesome(username, password, message):
        >>>     print username, password
        >>>     print message

        >>> @cache.register(name='awesome')
        >>> def lessawesome(username, password, message):
        >>>     print username, password
        >>>     print message
        """
        if callable(arg):
            self[arg.__name__] = arg
            return arg
        else:
            def decorator(func):
                self[arg] = func
                return func
            return decorator

cache = UpdaterCache()


@cache.add('twitter')
def twitterupdate(username, password, message):
    twitter.Twitter(username, password).statuses.update(status=message)
