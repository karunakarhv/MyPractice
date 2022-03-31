# Calculating Yesterday and Tomorrow
# Problem
# We want to get today's date, then calculate yesterdays and tomorrow's

import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print('Today - {}'.format(today))
print('Yesterday - {}'.format(yesterday))
print('Tomorrow - {}'.format(tomorrow))