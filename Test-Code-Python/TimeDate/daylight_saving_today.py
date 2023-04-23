# Checking whether Daylight saving time is currently in effect
#
# Problem - We want to know whether daylight saving time is in effect
# in your local time zone today

import time

def is_dst():
    return bool(time.localtime().tm_isdst)

if __name__ == '__main__':
    print('Is daylight saving today {}'.format('yes' if is_dst() else 'no'))
