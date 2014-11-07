from django.conf.urls import patterns, include, url
from django.contrib import admin
from foobar import custom_admin
from foobar.custom_admin import custom_admin_site

admin.autodiscover()

custom_admin.site = custom_admin_site
admin_site = custom_admin.site

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'foobar.core.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^custom_admin/', include(custom_admin.site.urls)),
    url(r'^playground/', include('playground.urls')),
)
