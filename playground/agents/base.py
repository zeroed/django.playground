from datetime import datetime

__author__ = 'e.rossi'

class Base:

    def __init__(self):
        """
        Base Agent
        """
        self.instantiation_date = datetime.now()
        self.run_date = None
        self.name = "Base"
        self.description = "Base description"

    def run(self):
        """
        Mock base method.
        :return: False
        """
        self.run_date = datetime.now()
        return False

    def __str__(self):
        return 'Agent {name}, "{description}" - run date: {last_run}'.format(
            name=self.name,
            description=self.description,
            last_run=self.run_date
        )
