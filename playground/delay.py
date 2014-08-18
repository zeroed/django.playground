from playground.tasks import slow_add, add

__author__ = 'e.rossi'

for counter in range(3):
    # result = slow_add.apply_async((10, 1))
    result = slow_add.delay(10, 1)
    print(result)
    # print(result.ready())
    # print(result.get(timeout=1))