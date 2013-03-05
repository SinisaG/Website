from pyramid.view import view_config
from pyramid.response import Response

dic={'projects':'', 'clients':'', 'methodology':'', 'team':''}

class RootContext(object):
    static_prefix = '/static/'
    def __init__(self, request):
        self.request=request
    def active(self, *route):
        return "active" if self.request.matched_route.name in route else ""

def includeme(config):
    config.add_route('home', '/', factory=RootContext)
    config.add_route('projects', '/projects', factory=RootContext)
    config.add_route('clients', '/clients', factory=RootContext)
    config.add_route('methodology', '/methodology', factory=RootContext)
    config.add_route('team', '/team', factory=RootContext)
    config.add_route('gymondo', '/projects/gymondo', factory=RootContext)
    config.add_route('friendfund', '/projects/friendfund', factory=RootContext)
    config.add_route('giftcannon', '/projects/giftcannon', factory=RootContext)
    return config

@view_config(route_name='giftcannon', renderer='/projects/giftcannon.html')
@view_config(route_name='friendfund', renderer='/projects/friendfund.html')
@view_config(route_name='gymondo', renderer='/projects/gymondo.html')
@view_config(route_name='team', renderer='pages/team.html')
@view_config(route_name='methodology', renderer='pages/methodology.html')
@view_config(route_name='clients', renderer='pages/clients.html')
@view_config(route_name='projects', renderer='pages/projects.html')
@view_config(route_name='home', renderer='pages/index.html')
def my_view(context, request):
    return {}

