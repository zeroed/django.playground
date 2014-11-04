import random
from playground.jobs.base import Base
from celery import shared_task
from playground.tasks import slow_add

__author__ = 'eddie'


class Alpha(Base):
    """
    Alpha Job Detector
    """

    @staticmethod
    def name():
        return "Alpha"

    @staticmethod
    def initialize():
        return True

    @staticmethod
    @shared_task(name='playground.tasks.slow_add', serializer='json')
    def run():
        """
        Just count and sleep
        :return: True
        """
        return slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
