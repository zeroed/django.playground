from tempfile import mkstemp
from os import fdopen, unlink, kill
from subprocess import Popen
import signal
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
# import scripts

# Create your core here.


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
    now = datetime.now()
    html = "<html><body>Run your schedule now {time}.</body></html>".format(time=now)
    return HttpResponse(html)

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
