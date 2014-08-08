import sys
from time import sleep

__author__ = 'e.rossi'

class Job:
    """
        This class contains some simple Job
    """

    @staticmethod
    def do_count():
        """
        Just count and sleep
        :return: True
        """
        i = 0
        while i < 1000:
            print('myjob:', i)
            i += 1
            sleep(0.1)
            sys.stdout.flush()
        return True