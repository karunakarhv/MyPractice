from datetime import datetime, timedelta
import re
# str = r'2021-10-05T00:35:16.114Z - INFO - LAST HBT RESPONSE THAT SET TRANSMIT_EXPIRE_TIME WAS AT:  2021-10-05 00:34:30.666178'
# pattern = r'\d+-\d+-\d+\s\d+:\d+:\d+'
# value = re.findall(pattern, str)
# print(value[0])
# datetime_object = datetime.strptime(value[0], '%Y-%m-%d %H:%M:%S')
# print(type(datetime_object))
# print(datetime_object)  # printed in default format
# timeIncreased = datetime_object + timedelta(0, 60)
# print(timeIncreased)

output = '"transmitExpireTime": "2021-10-06T04:56:28Z"'
pattern = r'\d+-\d+-\d+T\d+:\d+:\d+Z'
transmitExpire = re.findall(pattern, output)[0]
dt = datetime.strptime('2021-10-12 21:40:06', '%Y-%m-%d %H:%M:%S')
dt1 = datetime.strptime('2021-10-12 21:41:06', '%Y-%m-%d %H:%M:%S')
if dt1 < dt:
    print('Lesser')
else:
    print('Greater')