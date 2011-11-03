import os
import sys

paths = ['/home/jebif/lib/Django','/home/jebif/apps/root','/home/jebif/apps/root/cv']
for p in paths :
	if p not in sys.path :
		sys.path.append(p)

os.environ["DJANGO_SETTINGS_MODULE"] = "jebif.settings"

