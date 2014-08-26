import random
import time
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from datetime import datetime
from celery.utils.log import get_task_logger
from playground.forms import RunTaskForm
from playground.tasks import slow_add
from django.http import Http404
from django.template import TemplateDoesNotExist
from playground.custom import get_task_id_from_uuid

# import tempfile import mkstemp
# from os import fdopen, unlink, kill
# from subprocess import Popen
# import signal
# import scripts

# Create your core here.
logger = get_task_logger(__name__)

def index(request):
    """

    :param request:
    :return:
    """
    html = "<html><body>Hello Python</body></html>"
    return HttpResponse(html)


def test(request):
    """

    :param request:
    :return:
    """
    now = datetime.now()
    html = "<html><body>It is now {time}.</body></html>".format(time=now)
    return HttpResponse(html)


def test_schedule(request):
    print("test_schedule")
    try:
        context_params = {}
        if request.method == 'POST':
            form = RunTaskForm(request.POST)
            print("received a POST form")
            print(form)
            number_of_tasks = int(form.cleaned_data['number_of_tasks'])
            if form.is_valid() and int(number_of_tasks) > 0 and number_of_tasks < 6:
                tasks = uuids = persisted_ids = []
                for counter in range(number_of_tasks):
                    task = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=0)
                    time.sleep(1)
                    db_object = get_task_id_from_uuid(task.id)
                    tasks.append(tasks)
                    uuids.append(tasks.id)
                    persisted_ids.append(db_object[0])
                    print('\n---------\n%s:%s:%s\n-------\n' % (task.id, db_object, task.state))
                context_params = {
                    'uuids': uuids,
                    'persisted_task_ids': persisted_ids
                }
            else:
                print("Form errors %s " % form.errors)
        context = RequestContext(request, context_params)
        template = loader.get_template('playground/test_schedule.html')
        return HttpResponse(template.render(context))
    except TemplateDoesNotExist:
        raise Http404()


# def showjob(request):
#     """
#     Show the last result of the running job.
#     :param request:
#     """
#     if not request.session in ['job']:
#         return HttpResponse('Not running a job. <a href="/startjob/">Start a new one?</a>')
#     else:
#         filename = request.session['jobfile']
#         results = open(filename)
#         lines = results.readlines()
#         try:
#             return HttpResponse('{0}<p><a href=\"/rmjob/\">Terminate?</a>'.format(lines[-1]))
#         except:
#             return HttpResponse('No results yet. <p><a href="/rmjob/">Terminate?</a>')
#     return response
#
#
# def rmjob(request):
#     """
#     Terminate the runining job.
#     """
#     if request.session in ['job']:
#         job = request.session['job']
#         filename = request.session['jobfile']
#         try:
#             # unix only
#             kill(job, signal.SIGKILL)
#             unlink(filename)
#         except OSError as e:
#             # probably the job has finished already
#             print(e)
#             pass
#         del request.session['job']
#         del request.session['jobfile']
#     # start a new one
#     return HttpResponseRedirect('/startjob/')
#
#
# def startjob(request):
#     """
#     Start a new long running process unless already started.
#     """
#     if not request.session.has_key('job'):
#         # create a temporary file to save the resuls
#         outfd, outname = mkstemp()
#         request.session['jobfile'] = outname
#         outfile = fdopen(outfd, 'a+')
#         proc = Popen("python myjob.py", shell = True, stdout = outfile)
#         # remember pid to terminate the job later
#         request.session['job'] = proc.pid
#     return HttpResponse('A <a href="/showjob/">new job</a> has started.')
