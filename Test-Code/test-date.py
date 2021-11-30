import datetime
from datetime import datetime
from dateutil.parser import parse
import re

get_date_obj = parse('2021-10-04T05:23:12Z')
print(get_date_obj)
print(get_date_obj + datetime.timedelta(seconds=60))

testStr = 'Value'
if not testStr:
    print('Empty')
else:
    print('Not Empty')

_testList = [{'tcName':'WINNF.FT.C.HBT.1', 'hbtIntCnt':0},
                        {'tcName':'WINNF.FT.C.HBT.3', 'hbtIntCnt':2},
                          {'tcName':'WINNF.FT.C.HBT.4', 'hbtIntCnt': 4},
                          {'tcName':'WINNF.FT.C.HBT.5', 'hbtIntCnt': 0},
                          {'tcName':'WINNF.FT.C.HBT.6', 'hbtIntCnt': 2},
                          {'tcName':'WINNF.FT.C.HBT.7', 'hbtIntCnt': 2},
                          {'tcName':'WINNF.FT.C.HBT.9', 'hbtIntCnt': 0},
                          {'tcName':'WINNF.FT.C.HBT.10', 'hbtIntCnt': 1}]

for test in _testList:
    if test['tcName'] in ('WINNF.FT.C.HBT.5', 'WINNF.FT.C.HBT.9'):
        print('Yes')
    else:
        print('Hello')

str = r'2021-10-05T00:35:16.114Z - INFO - LAST HBT RESPONSE THAT SET TRANSMIT_EXPIRE_TIME WAS AT:  2021-10-05 00:34:30.666178'
pattern = r'\d+-\d+-\d+\s\d+:\d+:\d+'
value = re.findall(pattern, str)
print(value[0])
datetime_object = datetime.strptime(value[0], '%m/%d/%y %H:%M:%S')
print(type(datetime_object))
print(datetime_object)  # printed in default format