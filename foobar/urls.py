from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foobar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^startjob/$', 'foobar.playground.views.startjob'),
    url(r'^showjob/$',  'foobar.playground.views.showjob'),
    url(r'^rmjob/$',    'foobar.playground.views.rmjob'),
)

