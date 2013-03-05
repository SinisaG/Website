from datetime import datetime
from lib.subscribers import add_renderer_variables
from pyramid.config import Configurator
from . import views
from pyramid.mako_templating import renderer_factory
from hncweb.lib.request import extend_request
from hncweb.lib.globals import Globals



def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings["g"] = g = Globals(**settings)
    config = Configurator(settings=settings)

    extend_request(config)
    config.add_subscriber(add_renderer_variables, 'pyramid.events.BeforeRender')
    config.add_renderer(".html", renderer_factory)


    if g.is_debug:
        config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(views)
    config.scan()
    return config.make_wsgi_app()