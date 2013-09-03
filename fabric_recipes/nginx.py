from fabric.api import env, task, run
from fabric.contrib import files
from fabric.operations import require


@task
def setup():
    require("project_name", "project_domain", "numprocs_start", "numprocs")

    files.upload_template(
        filename="nginx.conf",
        destination="/etc/nginx/sites-enabled/%s" % env.project_domain,
        context=env,
        use_jinja=True,
        template_dir=env.templates_dir)


@task
def reload():
    run("/etc/init.d/nginx reload")
