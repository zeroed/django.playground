import re
from django.db import connection
from playground.agents.mock import Mock as MockAgent
from playground.agents.alpha import Alpha as AlphaAgent
from foobar.settings import ERROR_KEY

__author__ = 'eddie'


def get_task_id_from_uuid(uuid):
    """
    Get the database_id of a task, given the UUID
    https://docs.djangoproject.com/en/1.6/topics/db/sql/#connections-and-cursors
    http://initd.org/psycopg/docs/usage.html#the-problem-with-the-query-parameters

    :param uuid:
    :return: [id, uuid]
    """
    cursor = connection.cursor()
    sql = "SELECT id, task_id FROM djcelery_taskstate WHERE task_id = %s;"
    data = (uuid, )
    cursor.execute(sql, data)
    return cursor.fetchone()


def get_latest_task_list():
    """
    Get the database_id list for all the tasks
    mapped as {'id':00, 'uuid':010101}
    :return:
    """
    cursor = connection.cursor()
    sql = "SELECT id, task_id FROM djcelery_taskstate ORDER BY tstamp DESC"
    data = ()
    cursor.execute(sql, data)
    result_map = []
    for task in cursor.fetchall():
        result_map.append({'id': str(task[0]), 'uuid': str(task[1])})
    return result_map


def sanitize_string(string_to_sanitize):
    """
    Remove everything but letters and underscores
    :param string_to_sanitize:
    :return: cleaned string
    """
    return re.sub("\W", "", string_to_sanitize)


def get_agent_by_name(agent_name):
    """

    :param agent_name:
    :return: A subclass of Base from the implemented agents...
    """
    return {
        'mock': MockAgent,
        'alpha': AlphaAgent,
        }.get(str(agent_name).lower(), None)


def get_celery_worker_status():
    """
    Get a dictionary of stats.
    If there is the ERROR_KEY, there is a problem and Jobs shouldn't run
    :return:
    """
    try:
        from celery.task.control import inspect
        stats = inspect().stats()
        if not stats:
            stats = {ERROR_KEY: 'No running Celery workers were found.'}
    except IOError as e:
        from errno import errorcode
        msg = "Error connecting to the backend: " + str(e)
        if len(e.args) > 0 and errorcode.get(e.args[0]) == 'ECONNREFUSED':
            msg += ' Check that the RabbitMQ server is running.'
        stats = {ERROR_KEY: msg}
    except ImportError as e:
        stats = {ERROR_KEY: str(e)}
    return stats


def can_run():
    """
    Looks into the status dictionary then return a Bool
    :return: True if there are not "known" problems
    """
    return False if ERROR_KEY in get_celery_worker_status() else True
