from datetime import datetime


def timeDiff(dateTime1, dateTime2):
    """Finds the difference between two datetime instances.

    Args:
        dateTime1 (datetime): Start Time
        dateTime2 (datetime): End Time

    Raises:
        TypeError: dateTime1 and dateTime2 must be an instance of datetime.

    Returns:
        datetime: an instance of datetime difference
    """
    if dateTime1 and not isinstance(dateTime1, datetime) or \
            dateTime2 and not isinstance(dateTime2, datetime):
        raise TypeError("dateTime1 and dateTime2 must be an instance of datetime!")
    return dateTime1 - dateTime2

startTime = '18:20:50'
endTime = '18:23:30'

dt1 = datetime.strptime(startTime, '%H:%M:%S')
dt2 = datetime.strptime(endTime, '%H:%M:%S')

print(timeDiff(dt2, dt1))

