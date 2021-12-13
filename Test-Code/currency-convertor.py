from decimal import Decimal
import requests
from datetime import datetime, date, timedelta
from forex_python.converter import CurrencyRates

urlLatest = 'https://theforexapi.com/api/latest'

def getLastSevenDays():
    dateDict = requests.get(url=urlLatest)
    dateList = (dateDict.json())['date'].split('-')
    intDateList = [int(i) for i in dateList]
    c = CurrencyRates()
    # Last 7 Days
    for i in range(7):
        dateTime =  date(intDateList[0], intDateList[1], intDateList[2]) - timedelta(days=i)
        print(c.convert('AUD', 'INR', amount=1, date_obj=datetime(dateTime.year, dateTime.month, dateTime.day)))

if __name__ == '__main__':
    getLastSevenDays()