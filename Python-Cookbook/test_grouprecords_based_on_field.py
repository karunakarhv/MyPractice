rows = [
    {'address': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'date': '2021-01-01'},
    {'address': '456 Elm St', 'city': 'Othertown', 'state': 'NY', 'date': '2021-01-02'},
    {'address': '789 Oak St', 'city': 'Anytown', 'state': 'CA', 'date': '2021-01-03'},
    {'address': '101 Pine St', 'city': 'Sometown', 'state': 'TX', 'date': '2021-01-04'},
    {'address': '202 Maple St', 'city': 'Othertown', 'state': 'NY', 'date': '2021-01-05'},
    {'address': '303 Cedar St', 'city': 'Anytown', 'state': 'CA', 'date': '1986-01-07'},
    {'address': '404 Birch St', 'city': 'Sometown', 'state': 'TX', 'date': '1986-01-07'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date', 'state')):
    print(date)
    for i in items:
        print(' ', i)