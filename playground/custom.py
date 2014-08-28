from django.db import connection

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
    result = cursor.fetchone()
    # print('\n======\n%s || %s || %s\n=========\n' % (sql, data, result))
    return result
