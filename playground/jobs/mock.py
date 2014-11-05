import random
import datetime
import time
from celery import shared_task
from django.db import transaction
from playground.jobs.base import Base
from playground.models import Detector, Result

from celery.utils.log import get_task_logger

__author__ = 'eddie'


class Mock(Base):
    """
    Mock Job Detector
    """
    logger = get_task_logger(__name__)

    @staticmethod
    def name():
        return "Mock"

    @staticmethod
    def initialize():
        return True

    @staticmethod
    def run():
        """
        Just count and sleep
        :return: True
        """

        # result = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
        result = task.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
        print(result.state)
        #result['detector'] = Mock.name()
        return result


@shared_task(name='playground.jobs.mock.task', serializer='json')
def task(x, y):
    """

    :param x:
    :param y:
    """
    try:
        delay = random.randint(1, 30)
        time.sleep(delay)
        message = 'Adding {0} + {1} with delay {2}'.format(x, y, delay)
        Mock.logger.info(message)
        with transaction.atomic():
            mock = Detector.get_agent_mock()
            result = Result.objects.create(
                content=message,
                value=(x + y),
                detector=mock,
                created_at=datetime.datetime.utcnow(),
                duration=delay
            )
            mock = Detector.update_last_running_time_and_counter(mock.name)
        Mock.logger.info("The detector is up to date: {0}".format(mock))
        return result.value

    except Exception as exc:
        task.retry(exc=exc, countdown=10)
