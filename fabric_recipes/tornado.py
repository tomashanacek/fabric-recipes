from fabric.api import env, task, run
from fabric.context_managers import cd
from fabric.operations import require
from context_managers import virtualenv
import supervisor
import nginx


@task
def setup():
    require(
        "directory", "venv_directory", "www_directory", "package_name",
        "repository", "project_name")

    # 1. clone project
    with cd(env.www_directory):
        run("git clone %s %s" % (env.repository, env.project_name))

    # 2. create virtualenv
    with cd(env.directory):
        run("virtualenv venv")

    # 3. install requirements
    with virtualenv():
        run("pip install -r requirements.txt")

    # 4. configure supervisor
    env.supervisor = {
        "command": supervisor.tornado_command()
    }

    supervisor.setup()
    supervisor.reload()

    # 5. configure nginx
    nginx.setup()
    nginx.reload()


@task
def deploy():
    with virtualenv():
        run("git pull")
        run("pip install -r requirements.txt")
    supervisor.restart()
