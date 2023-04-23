from decimal import Decimal
import requests
from datetime import datetime, date, timedelta
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt
import numpy as np

urlLatest = 'https://theforexapi.com/api/latest'

def getLastSevenDays():
    dateDict = requests.get(url=urlLatest)
    dateList = (dateDict.json())['date'].split('-')
    intDateList = [int(i) for i in dateList]
    c = CurrencyRates()
    dataList = []
    # Last 7 Days
    for i in range(7):
        data = ()
        dateTime =  date(intDateList[0], intDateList[1], intDateList[2]) - timedelta(days=i)
        data = data + (f'{dateTime.year}-{dateTime.month}-{dateTime.day}',)
        data = data + (c.convert('AUD', 'INR', amount=1, date_obj=datetime(dateTime.year, dateTime.month, dateTime.day)),)
        dataList.append(data)
    
    return dataList

def stemPlot(dataList):
    plt.style.use('_mpl-gallery')
    x, y = zip(*dataList)
    plt.title('AUD to INR Fx rates')
    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Currency rate')
    plt.show()

if __name__ == '__main__':
    dataList = getLastSevenDays()
    stemPlot(dataList)