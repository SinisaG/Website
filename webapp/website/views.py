from pyramid.view import view_config
from pyramid.response import Response

dic={'projects':'', 'clients':'', 'methodology':'', 'team':''}

class RootContext(object):
	def __init__(self, request):
		self.request=request
	def active(self, route):
		return "active" if route==self.request.matched_route.name else ""

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
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
@view_config(route_name='team', renderer='team.html')
@view_config(route_name='methodology', renderer='methodology.html')
@view_config(route_name='clients', renderer='clients.html')
@view_config(route_name='projects', renderer='projects.html')
@view_config(route_name='home', renderer='index.html')
def my_view(context, request):
	return {}

