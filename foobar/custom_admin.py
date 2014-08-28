#
# http://stackoverflow.com/questions/12321130/how-to-override-django-admins-views/12322030#12322030
#
from django.contrib.admin import AdminSite
from django.views.decorators.cache import never_cache
from django.http import HttpResponse

__author__ = 'eddie'


class CustomAdminSite(AdminSite):
    @never_cache
    def custom(self, request, extra_context=None):
        html = "<html><body>Hello Playground Admin </body></html>"
        return HttpResponse(html)

# admin_site = MyAdminSite()
custom_admin_site = CustomAdminSite(name='customadmin')
