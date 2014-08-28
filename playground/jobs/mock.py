import random
from playground.jobs.sample import Sample
from celery import shared_task
from playground.tasks import slow_add

__author__ = 'eddie'


class Mock(Sample):
    """
    Mock Job Detector
    """

    @staticmethod
    def name():
        return "Mock"

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
