# Running a command repeatedly
# Problem
# We need to run a command repeatedly, with arbitrary periodicity

import datetime
import time

def get_time_now(inc=5):
    print('Time now ', datetime.datetime.now())
    time.sleep(inc)

if __name__ == '__main__':
    i = 0
    while i < 5:
        i = i + 1
        get_time_now()