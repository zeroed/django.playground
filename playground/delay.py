from playground.tasks import slow_add, add
import random

__author__ = 'e.rossi'

for counter in range(7):
    result = slow_add.delay(random.randint(10, 100), random.randint(10, 100))
    print(result)
