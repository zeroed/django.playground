from datetime import datetime
from playground.agents.base import Base
from playground.jobs.alpha import Alpha as AlphaJob
import logging

__author__ = 'e.rossi'

class Alpha(Base):
    """
        Sample Alpha Agent
    """

    # Get an instance of a logger
    logger = logging.getLogger(__name__)

    def __init__(self):
        super().__init__()
        self.name = "alpha"
        self.description = "Alpha agent"

    def run(self):
        """
        Run a count Job
        :return:
        """
        self.run_date = datetime.now()
        return AlphaJob.run()

    @staticmethod
    def name():
        return "Alpha"
