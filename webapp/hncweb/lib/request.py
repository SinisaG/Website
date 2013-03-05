
class JsonAwareRedirect(Exception):
    def __init__(self, location):
        self.location = location

def is_json(request):
    return 'application/json' in request.content_type

def fwd_raw(request, location):
    raise JsonAwareRedirect(location = location)

def rld_url(request, with_query = True, *args, **kwargs):
    if with_query:
        return request.current_route_url(_query = request.GET, *args, **kwargs)
    else:
        return request.current_route_url(*args, **kwargs)

def rld(request, with_query = True, *args, **kwargs):
    raise JsonAwareRedirect(location = request.rld_url(with_query, *args, **kwargs))
def fwd(request, route_name, *args, **kwargs):
    raise JsonAwareRedirect(location = request.fwd_url(route_name, *args, **kwargs))

def fwd_url(request, route_name, secure = False, *args, **kwargs):
    if secure:
        return request.route_url(route_name, _scheme = request.globals.secure_scheme, *args, **kwargs)
    else:
        return request.route_url(route_name, _scheme = "http", *args, **kwargs)

def extend_request(config):
    def furl(request):
        return request.params.get("furl") or request.path_qs
    config.add_request_method(furl, 'furl', reify=True)

    def globals(request):
        return request.registry.settings["g"]
    config.add_request_method(globals, 'globals', reify=True)
    config.add_request_method(is_json, 'is_json', reify=True)
    config.add_request_method(fwd_raw)
    config.add_request_method(rld_url)
    config.add_request_method(rld)
    config.add_request_method(fwd)
    config.add_request_method(fwd_url)