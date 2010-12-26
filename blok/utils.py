__author__ = 'kilonet'

from werkzeug import Local, LocalManager
from os import path
from werkzeug import Response
from jinja2 import Environment, FileSystemLoader


local = Local()
local_manager = LocalManager([local])
application = local('application')


def datetimeformat_filter (datetime):
    return datetime.strftime("%a %b %d, %H:%M")

TEMPLATE_PATH = path.join(path.dirname(__file__), 'templates')
jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_PATH))
jinja_env.filters['datetimeformat'] = datetimeformat_filter


def render_template(template, **context):
    return Response(jinja_env.get_template(template).render(**context),
                    mimetype='text/html')




