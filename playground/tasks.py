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
        detector_in_charge = Detector.get_mock()
        computation_result = detector_in_charge.do_something(x, y, d)
        result = Result.objects.create(
            content='Adding {0} + {1} with delay {2}'.format(x, y, d),
            value=computation_result,
            detector=detector_in_charge,
            created_at=datetime.datetime.utcnow(),
            duration=d
        )
        return result.value
    except Exception as exc:
        slow_add.retry(exc=exc, countdown=10)


@shared_task(name='playground.tasks.mul', serializer='json')
def mul(x, y):
    return x * y


@shared_task(name='playground.tasks.xsum', serializer='json')
def xsum(numbers):
    return sum(numbers)
