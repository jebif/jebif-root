from django.conf.urls.defaults import *
from django.contrib import admin

from jebif import settings

admin.autodiscover()

urlpatterns = patterns('',
    # add 'django.contrib.admindocs' to INSTALLED_APPS 
    # to enable admin documentation
    # (r'^admin/doc/',    include('django.contrib.admindocs.urls')),

    (r'^admin/',        include(admin.site.urls)),
    (r'^admin_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	(r'^accounts/login/$', 'django.contrib.auth.views.login'),

	(r'^membership/', 	include('membership.urls')),
	(r'^cv/',			include('cv.urls')),

	(r'^$', 'django.views.generic.simple.redirect_to', {'url': 'http://jebif.fr'}),
)

