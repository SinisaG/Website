from pyramid.config import Configurator
from . import views
    

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    config.add_renderer('.html', 'pyramid.mako_templating.renderer_factory')
    config.include(views)
    config.scan()
    return config.make_wsgi_app()	
