from __future__ import absolute_import
import random
import datetime
import time
from celery import shared_task
from celery.utils.log import get_task_logger

__author__ = 'e.rossi'

"""
Result API
http://celery.readthedocs.org/en/latest/reference/celery.result.html

Keeping Results
http://celery.readthedocs.org/en/latest/getting-started/first-steps-with-celery.html#keeping-results
"""

logger = get_task_logger(__name__)

@shared_task(name='playground.tasks.add', serializer='json')
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task(name='playground.tasks.slow_add', serializer='json')
def slow_add(x, y):
    try:
        delay = random.randint(1, 30)
        time.sleep(delay)
        message = 'Adding {0} + {1} with delay {2}'.format(x, y, delay)
        logger.info(message)
        return dict(
            content=message,
            value=x + y,
            detector=None,
            created_at=datetime.datetime.utcnow(),
            duration=delay
        )
    except Exception as exc:
        slow_add.retry(exc=exc, countdown=10)


@shared_task(name='playground.tasks.mul', serializer='json')
def mul(x, y):
    return x * y


@shared_task(name='playground.tasks.xsum', serializer='json')
def xsum(numbers):
    return sum(numbers)
