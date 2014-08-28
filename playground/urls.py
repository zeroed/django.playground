from django.conf.urls import patterns, include, url
from playground import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foobar.core.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
    url(r'^test_schedule/$', views.test_schedule, name='test_schedule'),
    url(r'^run_schedule/$', views.run_schedule, name='run_schedule'),

    # url(r'^startjob/$', 'playground.core.startjob'),
    # url(r'^showjob/$', 'playground.core.showjob'),
    # url(r'^rmjob/$', 'playground.core.rmjob'),
)
