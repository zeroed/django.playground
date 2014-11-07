from datetime import datetime
from playground.agents.base import Base
from playground.jobs.mock import Mock as MockJob
import logging

__author__ = 'e.rossi'


class Mock(Base):
    """
        Sample mock Agent
    """

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def __init__(self):
        super().__init__()
        self.name = "Mock"
        self.description = "Mock agent"
        Mock.logger.info("{0} initialized... {1}".format(self.name, self))

    def run(self):
        """
        Run a count Job
        :return:
        """
        Mock.logger.info("{0} start working... ".format(self.name, self))
        self.run_date = datetime.now()
        result = MockJob.run()
        Mock.logger.info("{0} worked on {1}. ".format(self.name, result))
        return result

    @staticmethod
    def name():
        return "Mock"
