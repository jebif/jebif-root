from django.conf import settings
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

ROOT_URL = settings.ROOT_URL

class RequireLoginMiddleware(object):
    """ Come from http://www.djangosnippets.org/snippets/136/

    Require Login middleware. If enabled, each Django-powered page will
    require authentication.

    If an anonymous user requests a page, he/she is redirected to the login
    page set by REQUIRE_LOGIN_PATH or /accounts/login/ by default.
    """
    def __init__(self):
        self.require_login_path = getattr(settings, 'REQUIRE_LOGIN_PATH', '/%scv/accounts/login/'%ROOT_URL)

    def process_request(self, request):
        if request.user.is_anonymous() \
            and not '/media/' in request.path \
            and not '/admin/' in request.path \
            and not '/admin_media/' in request.path \
            and not '/media_admin/' in request.path \
            and not '/accounts/' in request.path \
            and not '/licence_required/' in request.path \
            and not '/modify_password/' in request.path \
            and not '/membership/' in request.path \
            and not '/election/' in request.path \
            and request.path != self.require_login_path:
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))

_SUPPORTED_TRANSFORMS = ['PUT', 'DELETE']
_MIDDLEWARE_KEY = '_method'

class HttpMethodsMiddleware(object):
    """ Come from http://www.djangosnippets.org/snippets/174/

    This middleware allows developers to "fake" browser support for HTTP
    methods. Even though most modern browsers only support GET and POST,
    the HTTP standard defines others. In the context of REST, PUT and DELETE
    are used for client interaction with the server.
    """
    def process_request(self, request):
        if request.POST and _MIDDLEWARE_KEY in request.POST:
            if request.POST[_MIDDLEWARE_KEY].upper() in _SUPPORTED_TRANSFORMS:
                try:
                    request.method = request.POST[_MIDDLEWARE_KEY].upper()
                except:
                    request.META['REQUEST_METHOD'] = request.REQUEST[_MIDDLEWARE_KEY].upper()
                if request.method == 'PUT':
                    request.PUT = request.POST
        return None

class TerminalLogging(object):
    def process_response(self, request, response):
        from sys import stdout
        from django.db import connection
        if stdout.isatty():
            for query in connection.queries :
                print "\033[1;31m[%s]\033[0m \033[1m%s\033[0m" % (query['time'],
                    " ".join(query['sql'].split()))
            print len(connection.queries)
        return response

