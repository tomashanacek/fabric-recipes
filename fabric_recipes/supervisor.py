import os
import utils
from fabric.api import env, task, run
from fabric.contrib import files
from fabric.operations import require


def tornado_command(script_name="app.py"):
    return (
        "%s %s "
        "--port=%%(process_num)s "
        "--log_file_prefix=/var/log/%%(program_name)s-%%(process_num)s.log" %
        (os.path.join(env.venv_directory, "bin/python"),
         os.path.join(env.directory, env.package_name, script_name))
    )


@task
def setup():
    require("project_name", "supervisor", "numprocs_start", "numprocs")

    text = utils.render_template("supervisor.conf", env)

    files.append(env.supervisor_conf, text)


@task
def reload():
    run("supervisorctl reread && supervisorctl update")


@task
def restart():
    require("project_name")

    run("supervisorctl restart %s:" % env.project_name)
