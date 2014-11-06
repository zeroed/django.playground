import random
import datetime
import time
from celery import shared_task
from django.db import transaction
from playground.jobs.base import Base
from playground.models import Detector as DetectorModel
from playground.models import Result as ResultModel

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
        http://docs.celeryproject.org/en/latest/reference/celery.result.html#celery.result.AsyncResult
        :return: An AsyncResult
        """
        resulting_task = task.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
        Mock.logger.info("The detector {0} has this task (class: {1}) in charge: {2}".format(
            Mock.name(),
            resulting_task.__class__.__name__,
            resulting_task)
        )
        return resulting_task

    @staticmethod
    def calculate_result(x, y):
        return x + y

@shared_task(name='playground.jobs.mock.task', serializer='json')
def task(x, y):
    """

    :param x:
    :param y:

    :return: The playground RESULT object.
    """
    try:
        delay = random.randint(1, 30)
        time.sleep(delay)
        message = 'Adding {0} + {1} with delay {2}'.format(x, y, delay)
        Mock.logger.info(message)
        with transaction.atomic():
            mock = DetectorModel.get_agent_mock()
            result = ResultModel.objects.create(
                content=message,
                value=Mock.calculate_result(x, y),
                detector=mock,
                created_at=datetime.datetime.utcnow(),
                duration=delay
            )
            mock = DetectorModel.update_last_running_time_and_counter(mock.name)
        Mock.logger.info("The detector is up to date: {0}".format(mock))
        return result

    except Exception as exc:
        task.retry(exc=exc, countdown=10)
