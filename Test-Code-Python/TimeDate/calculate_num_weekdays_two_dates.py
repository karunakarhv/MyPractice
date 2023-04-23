# Calculate the number of weekdays between two dates
# Problem
# We want to calculate the number of weekdays(working days),
# as opposed to calendar days that fall between two dates.

from dateutil import rrule
import datetime

def workdays(start, end, holidays=0, days_off=None):
    if days_off is None:
        days_off = 5, 6 #default to: saturdays and sundays
    workdays = [x for x in range(7) if x not in days_off]
    days = rrule.rrule(rrule.DAILY, dtstart=start, until=end, byweekday=workdays)
    return days.count() - holidays

if __name__ == '__main__':
    testdates = [(datetime.date(2022, 1, 26), datetime.date(2022, 4, 15), 0),
                 (datetime.date(2003, 2, 28), datetime.date(2003, 3, 3), 1)]
    def test(testdates, days_off=None):
        for s, e, h in testdates:
            print('Total Workdays from {} to {} is {} with {} holidays'
                  .format(s, e, workdays(s, e, h, days_off), h))
    test(testdates)