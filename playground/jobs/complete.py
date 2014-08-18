from time import sleep

from celery import task, current_task
from celery.result import AsyncResult

from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import simplejson as json
from django.conf.urls import patterns, url

__author__ = 'e.rossi'


@task()
def do_work():
    """ Get some rest, asynchronously, and update the state all the time """
    for i in range(100):
        sleep(0.1)
        current_task.update_state(state='PROGRESS',
            meta={'current': i, 'total': 100})


def poll_state(request):
    """ A view to report the progress to the user """
    if 'job' in request.GET:
        job_id = request.GET['job']
    else:
        return HttpResponse('No job id given.')

    job = AsyncResult(job_id)
    data = job.result or job.state
    return HttpResponse(json.dumps(data), mimetype='application/json')


def init_work(request):
    """ A view to start a background job and redirect to the status page """
    job = do_work.delay()
    return HttpResponseRedirect(reverse('poll_state') + '?job=' + job.id)


urlpatterns = patterns('webapp.modules.asynctasks.progress_bar_demo',
    url(r'^init_work$', init_work),
    url(r'^poll_state$', poll_state, name="poll_state"),
)