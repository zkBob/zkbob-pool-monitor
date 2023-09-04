from typing import Callable

from time import time, sleep

# Based on
# - https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds/49801719#49801719
def every(task: Callable, delay: int) -> None:
    first_time = True
    next_time = time() + delay
    while True:
        if not first_time:
            sleep(max(0, next_time - time()))
        else:
            first_time = False
        task()
        next_time += (time() - next_time) // delay * delay + delay
