from playground.tasks import slow_add, add
import random

__author__ = 'e.rossi'


def run(*args):
    """
    Launch me with RUNSCRIP
    Relevant docs: http://django-extensions.readthedocs.org/en/latest/runscript.html

    :param args:
    :return:
    """
    for counter in range(force_to_one(args)):
        result = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
        print(result)
        if result.ready():
            print("Task has run : %s" % result)
            if result.successful():
                print("Result was: %s" % result.result)
            else:
                if isinstance(result.result, Exception):
                    print("Task failed due to raising an exception")
                    raise result.result
                else:
                    print("Task failed without raising exception")
        else:
            print("Task has not yet run")

def force_to_one(something):
    try:
        return int(something[0])
    except (ValueError, IndexError):
        return 1
