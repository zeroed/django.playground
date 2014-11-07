#
# http://stackoverflow.com/questions/12321130/how-to-override-django-admins-views/12322030#12322030
#
from django.contrib.admin import AdminSite
from django.views.decorators.cache import never_cache
from django.http import HttpResponse
from django.utils.text import capfirst

__author__ = 'eddie'


class CustomAdminSiteMixin(object):
    """Mixin for AdminSite to allow registering custom admin views."""

    index_template = []

    def __init__(self, *args, **kwargs):
        self.custom_views = []
        return super(CustomAdminSiteMixin, self).__init__(*args, **kwargs)

    def index(self, request, extra_context=None):
        """Make sure our list of custom views is on the index page."""
        if not extra_context:
            extra_context = {}
        custom_list = []
        for path, view, name, urlname, visible in self.custom_views:
            if visible is True:
                if name:
                    custom_list.append((path, name))
                else:
                    custom_list.append((path, capfirst(view.__name__)))

        # Sort views alphabetically.
        custom_list.sort(key=lambda x: x[1])
        extra_context.update({
            'custom_list': custom_list
        })
        return super(CustomAdminSiteMixin, self).index(request, extra_context)

    @never_cache
    def custom(self, request, extra_context=None):
        html = "<html><body>Hello Playground Admin </body></html>"
        return HttpResponse(html)


class CustomAdminSite(CustomAdminSiteMixin, AdminSite):
    """
    A Django AdminSite with the CustomAdminSiteMixin to allow registering custom
    views not connected to models.

    https://github.com/jsocol/django-adminplus/blob/master/adminplus/sites.py
    """

# admin_site = MyAdminSite()
custom_admin_site = CustomAdminSite(name='customadmin')
