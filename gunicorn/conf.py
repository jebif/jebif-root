import os
import sys

paths = ['/home/jebif/lib/Django','/home/jebif/apps/root','/home/jebif/apps/root/cv']
for p in paths :
	if p not in sys.path :
		sys.path.append(p)

os.environ["DJANGO_SETTINGS_MODULE"] = "jebif.settings"

bind = "unix:/var/run/gunicorn/jebif/sock"
pidfile = "/var/run/gunicorn/jebif/pid"
max_requests = 500
umask = 0007

def when_ready( server ) :
	from jebif.gunicorn import monitor
	monitor.start(interval=5.0)
	monitor.track(os.path.join(os.path.dirname(__file__), 'touch_to_restart'))

