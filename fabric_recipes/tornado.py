from fabric.api import env, task, run
from fabric.operations import require
from context_managers import virtualenv
import supervisor
import nginx
import utils


@task
def setup():
    require(
        "directory", "venv_directory", "www_directory", "package_name",
        "repository", "project_name")

    # 1. clone project
    utils.clone_project()

    # 2. create virtualenv
    utils.create_virtualenv()

    # 3. install requirements
    utils.install_requirements()

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
