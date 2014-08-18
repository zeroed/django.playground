from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

__author__ = 'e.rossi'

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foobar.settings')

app = Celery('foobar')

# app = Celery('tasks', backend='amqp', broker='amqp://')
# app = Celery('tasks', backend='redis://localhost', broker='amqp://')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
#app.config_from_object('django.conf:settings')
app.config_from_object('foobar.celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# Start Celery
# \pythonWorkspace\foobar> celery -A foobar worker -l info
# \pythonWorkspace\foobar> python ./manage.py celeryd -l info