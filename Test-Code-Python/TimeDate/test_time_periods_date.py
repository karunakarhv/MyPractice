# Calculating the time periods in a date range

# Problem
# Given two dates, we want to calculate the number of weeks between them.

from dateutil import rrule
from datetime import date

def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

if __name__ == '__main__':
    starts = [date(2005, 1, 4), date(2005, 1, 6)]
    end = date(2005, 1, 10)
    for s in starts:
        days = rrule.rrule(rrule.DAILY, dtstart=s, until=end).count()
        print('{} days show as {} weeks'.format(days, weeks_between(s, end)))