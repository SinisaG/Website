import logging, os, random

log = logging.getLogger(__name__)


APP_ROOT = os.path.abspath(os.path.join(__file__, "..", "..", ".."))
VERSION_FILE = os.path.join(APP_ROOT, "VERSION_TOKEN")

if os.path.exists(VERSION_FILE):
    VERSION_TOKEN = open(VERSION_FILE).read().strip()
else:
    VERSION_TOKEN = random.random()
log.info("USING NEW STATIC RESOURCE TOKEN: %s", VERSION_TOKEN)

from dogpile.cache import make_region



class Globals(object):
    mailConfig = {"mail.on":True,"mail.transport":"smtp", "mail.smtp.tls":True}
    def __init__ (self, **settings):
        self.is_debug = settings.get('pyramid.debug_templates', 'false') == 'true'
        self.VERSION_TOKEN = "v={}".format(VERSION_TOKEN)
        self.cache = make_region().configure_from_config(settings, "cache.")


