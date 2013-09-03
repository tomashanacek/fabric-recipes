from jinja2 import Environment, FileSystemLoader
from fabric.api import env
from fabric.utils import apply_lcwd


def render_template(filename, context=None, template_dir=None):
    template_dir = template_dir or env.templates_dir
    template_dir = apply_lcwd(template_dir, env)

    jenv = Environment(loader=FileSystemLoader(template_dir))
    text = jenv.get_template(filename).render(**context or {})

    text = text.encode('utf-8')
    return text
