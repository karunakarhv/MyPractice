
import json

with open('response.json', 'r') as f:
    data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
test = set()
for id in data:
    for items in id['Sales']:
        test.add(items['Location']['Name'])

for i in test:
    print(i)