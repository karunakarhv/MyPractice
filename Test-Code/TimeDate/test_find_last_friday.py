# Finding last Friday
# Problem
# We want to find the date of last friday and print it in a specified format

import datetime, calendar

def oneWay():
    lastFriday = datetime.date.today()
    oneDay = datetime.timedelta(days=1)
    while lastFriday.weekday() != calendar.FRIDAY:
        lastFriday = lastFriday - oneDay
    print(lastFriday.strftime('%A, %d-%b-%Y'))

def otherWay():
    today = datetime.date.today()
    targetDay = calendar.FRIDAY
    thisDay = today.weekday()
    deltaToTarget = (thisDay - targetDay) % 7
    lastFriday = today - datetime.timedelta(days=deltaToTarget)
    print(lastFriday.strftime('%A, %d-%b-%Y'))

otherWay()