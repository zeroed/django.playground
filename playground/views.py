import time
from datetime import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.conf import settings
from django.utils.html import escape
import logging
from playground.models import Detector
from playground.forms import RunDetectorTaskForm
from playground.custom import \
    get_task_id_from_uuid, \
    get_agent_by_name, \
    can_run, \
    get_celery_worker_status, \
    get_latest_task_list

logger = logging.getLogger(__name__)


def index(request):
    """

    :param request:
    :return:
    """
    html = "<html><body>Hello Playground %s </body></html>" % settings.VERSION
    return HttpResponse(html)


def test(request):
    """

    :param request:
    :return:
    """
    now = datetime.now()
    html = "<html><body>It is now {time}.</body></html>".format(time=now)
    return HttpResponse(html)


def run_schedule(request):
    try:
        context_params = {}
        if request.method == 'GET':
            context_params = {
                'latest_task_list': get_latest_task_list()
            }
        elif request.method == 'POST':
            logger.info("POST to run_schedule")
            form = RunDetectorTaskForm(request.POST)
            logger.info("Received form:\n{0}".format(form))
            detector_name = escape(form.cleaned_data['detector_name'])
            logger.info("POST to run_schedule for {0}".format(detector_name))
            logger.info("check if {0} is into {1}... {2}".format(detector_name, Detector.get_registered_agent_names(), detector_name in Detector.get_registered_agent_names()))
            if form.is_valid() \
                    and detector_name \
                    and len(detector_name) > 0 \
                    and detector_name in Detector.get_registered_agent_names():

                agent = get_agent_by_name(detector_name)
                message = "Retrieved agent {0}".format(agent.name())
                logger.info(message)
                if can_run():
                    task = agent().run()
                    # Silly but it seems this is necessary to find the object on the DB
                    time.sleep(1)
                    db_object = get_task_id_from_uuid(task.id)
                    logger.info('\n---------\n%s:%s:%s\n-------\n' % (task.id, db_object, task.state))
                    context_params = {
                        'uuid': task.id,
                        'persisted_task_id': db_object[0],
                        'errors': "",
                        'message': message,
                        'latest_task_list': get_latest_task_list()
                    }
                else:
                    context_params = {
                        'uuid': None,
                        'persisted_task_id': None,
                        'errors': 'System errors',
                        'message' : get_celery_worker_status(),
                        'latest_task_list': get_latest_task_list()
                    }
            else:
                context_params = {
                    'uuid': None,
                    'persisted_task_id': None,
                    'errors': form.errors,
                    'message' : "There are some error into the form",
                    'latest_task_list': get_latest_task_list()
                }
                logger.error("Form errors %s " % form.errors)
        context = RequestContext(request, context_params)
        template = loader.get_template('playground/test_schedule.html')
        return HttpResponse(template.render(context))
    except TemplateDoesNotExist:
        raise Http404()
