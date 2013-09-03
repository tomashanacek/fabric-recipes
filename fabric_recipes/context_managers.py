from fabric.api import env
from fabric.context_managers import cd, prefix
from contextlib import contextmanager


@contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield
