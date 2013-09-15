from jinja2 import Environment, FileSystemLoader
from fabric.api import env, task, run
from fabric.utils import apply_lcwd
from fabric.operations import require
from fabric.context_managers import cd
from context_managers import virtualenv


def render_template(filename, context=None, template_dir=None):
    template_dir = template_dir or env.templates_dir
    template_dir = apply_lcwd(template_dir, env)

    jenv = Environment(loader=FileSystemLoader(template_dir))
    text = jenv.get_template(filename).render(**context or {})

    text = text.encode('utf-8')
    return text


@task
def clone_project():
    require("www_directory", "repository", "project_name")

    with cd(env.www_directory):
        run("git clone %s %s" % (env.repository, env.project_name))


@task
def create_virtualenv():
    require("directory")

    with cd(env.directory):
        run("virtualenv venv")


@task
def install_requirements():
    with virtualenv():
        run("pip install -r requirements.txt")
