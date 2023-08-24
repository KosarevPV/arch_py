from jinja2 import Environment, FileSystemLoader
from os.path import join


def render(template_name, folder='templates', **kwargs):
    file_path = join(folder, template_name)
    env = Environment()
    env.loader = FileSystemLoader(folder)
    template = env.get_template(template_name)

    return template.render(**kwargs)

