from datetime import datetime
import logging

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
        self.last_result = None

    def run(self):
        """
        Mock base method.
        :return: False
        """
        self.run_date = datetime.now()
        return False

    def print_last_result(self):
        if self.last_result :
            self.last_result
        else:
            "There is no result here"

    def __str__(self):
        return 'Agent {name}, "{description}" - run date: {last_run}'.format(
            name=self.name,
            description=self.description,
            last_run=self.run_date
        )

    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""
    @staticmethod
    def name(self):
        raise NotImplementedError("Should have implemented this")
