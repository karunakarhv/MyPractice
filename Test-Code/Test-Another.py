def isListOrTuple(obj):
    return isinstance(obj, (list, tuple))

test = []
testAnother = ()
test_test = 1

print('List - {}'.format(isListOrTuple(test)))
print('Tuple - {}'.format(isListOrTuple(testAnother)))
print('List - {}'.format(isListOrTuple(test_test)))

test = [1,2,3]
test.pop()
for i in test:
    print i
resultDict = {}
resultDict['total250us'] = 10
print('Total transmission (250us res) : {:.4f}s'
      .format(resultDict['total250us'] / 1000.0))

simpleDict = {'a': 1, 'b': 2}
for test in simpleDict:
    print(test)

testCaseScenarios = {
    
    'tc1': { 'ulTraffic':'5m',
             'expectedTimeRange':[1, 6]
        },
    
    'tc2': { 'ulTraffic':'50k',
             'expectedTimeRange':[10, 300]
        },
    
    'tc3': { 'ulTraffic':'5k',
             'expectedTimeRange':[200, 1000]
        }
}

for testCase in testCaseScenarios.values():
    print(testCase['ulTraffic'])
    print(testCase['expectedTimeRange'])

from datetime import datetime
s1 = '23:33:06'
s2 = '23:39:47' # for example
FMT = '%H:%M:%S'
tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta)
