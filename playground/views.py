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
from playground.custom import get_task_id_from_uuid, get_agent_by_name

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


# DELETE_ME
# def test_schedule(request):
#     try:
#         context_params = {}
#         if request.method == 'POST':
#             form = RunTestTaskForm(request.POST)
#             number_of_tasks = int(form.cleaned_data['number_of_tasks'])
#             if form.is_valid() and int(number_of_tasks) > 0 and number_of_tasks < 6:
#                 tasks = uuids = persisted_ids = []
#                 for counter in range(number_of_tasks):
#                     task = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=0)
#                     time.sleep(1)
#                     db_object = get_task_id_from_uuid(task.id)
#                     tasks.append(tasks)
#                     uuids.append(tasks.id)
#                     persisted_ids.append(db_object[0])
#                     print('\n---------\n%s:%s:%s\n-------\n' % (task.id, db_object, task.state))
#                 context_params = {
#                     'uuids': uuids,
#                     'persisted_task_ids': persisted_ids
#                 }
#             else:
#                 print("Form errors %s " % form.errors)
#         context = RequestContext(request, context_params)
#         template = loader.get_template('playground/test_schedule.html')
#         return HttpResponse(template.render(context))
#     except TemplateDoesNotExist:
#         raise Http404()


def run_schedule(request):
    try:
        context_params = {}
        if request.method == 'POST':
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
                logger.warn("Retrieved agent {0}".format(agent))
                task = agent().run()

                # Silly but it seems this is necessary to find the object on the DB
                time.sleep(1)

                db_object = get_task_id_from_uuid(task.id)
                logger.info('\n---------\n%s:%s:%s\n-------\n' % (task.id, db_object, task.state))
                context_params = {
                    'uuid': task.id,
                    'persisted_task_id': db_object[0]
                }
            else:
                logger.error("Form errors %s " % form.errors)
        context = RequestContext(request, context_params)
        template = loader.get_template('playground/test_schedule.html')
        return HttpResponse(template.render(context))
    except TemplateDoesNotExist:
        raise Http404()
