from datetime import datetime
from playground.agents.base import Base
from playground.jobs.sample import Job

__author__ = 'e.rossi'

class Mock(Base):
    """
        Sample mock Agent
    """
    def __init__(self):
        super().__init__()
        self.name = "mock"
        self.description = "Mock agent"

    def run(self):
        """
        Run a count Job
        :return:
        """
        self.run_date = datetime.now()
        return Job.do_count()