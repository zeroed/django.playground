__author__ = 'e.rossi'


class Base:
    """
        This class contains the skeleton Job
    """

    @staticmethod
    def name():
        return "Base"

    @staticmethod
    def initialize():
        return True

    @staticmethod
    def run():
        return True
