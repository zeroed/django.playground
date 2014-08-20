from django.conf import settings
from playground.tasks import slow_add, add
import random

__author__ = 'e.rossi'

for counter in range(7):
    result = slow_add.apply_async((random.randint(10, 100), random.randint(10, 100)), countdown=2)
    print(result)
    if result.ready():
        print("Task has run")
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
