
def add_renderer_variables(event):
    if event['renderer_name'] != 'json':
        request = event['request']
        app_globals = request.globals
        event.update({"g"       : app_globals
            , 'vctxt'           : request.root
            , 'STATIC_URL'      : request.root.static_prefix
            , 'ROOT_STATIC_URL' : request.root.static_prefix
            , 'VERSION_TOKEN'   : app_globals.VERSION_TOKEN
        })
    return event