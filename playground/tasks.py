from __future__ import absolute_import
from celery import shared_task
from celery.utils.log import get_task_logger
import time

__author__ = 'e.rossi'


logger = get_task_logger(__name__)

@shared_task(name='tasks.add', serializer='json')
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task(name='tasks.slow_add', serializer='json')
def slow_add(x, y):
    d = 30
    time.sleep(d)
    logger.info('Adding {0} + {1} with delay {2}'.format(x, y, d))
    return x + y


@shared_task(serializer='json')
def mul(x, y):
    return x * y


@shared_task(serializer='json')
def xsum(numbers):
    return sum(numbers)
