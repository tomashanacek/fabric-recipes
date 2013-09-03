from fabric.api import env
import os


__version__ = "0.1.0"

env.templates_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "templates")
env.supervisor_conf = "/etc/supervisord.conf"
