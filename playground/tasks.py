from __future__ import absolute_import
import time
import random
import datetime
from celery import shared_task
from celery.utils.log import get_task_logger
from playground.models import Result
from playground.models import Detector

__author__ = 'e.rossi'


logger = get_task_logger(__name__)

@shared_task(name='playground.tasks.add', serializer='json')
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task(name='playground.tasks.slow_add', serializer='json')
def slow_add(x, y):
    try:
        d = random.randint(1, 30)
        time.sleep(d)
        logger.info('Adding {0} + {1} with delay {2}'.format(x, y, d))
        result = Result()
        result.content = "Meh... done I think"
        result.value = x + y
        result.detector = Detector.objects.get(id=1)
        result.creation_date = datetime.datetime.now()
        result.save()
        return result.value
    except Exception as exc:
        slow_add.retry(exc=exc, countdown=10)


@shared_task(name='playground.tasks.mul', serializer='json')
def mul(x, y):
    return x * y


@shared_task(name='playground.tasks.xsum', serializer='json')
def xsum(numbers):
    return sum(numbers)
