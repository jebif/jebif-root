import os
import sys

paths = ['/home/jebif/lib/Django','/home/jebif/apps/root','/home/jebif/apps/root/cv']
for p in paths :
        if p not in sys.path :
                sys.path.append(p)

os.environ["DJANGO_SETTINGS_MODULE"] = "jebif.settings"

from jebif.apache import monitor
monitor.start(interval=10.0)
monitor.track(os.path.join(os.path.dirname(__file__), 'touch_to_restart'))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

