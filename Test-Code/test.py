import json
import ast
import re
import sys
data = 'M-^A/{"RebootCause":"Warm-restart","Type":"Connect"}M-^I^T{"Type":"Heartbeat"}M-^A3{"State":"LTE","Type":"NetworkServiceStatusChange"}M-^I^T{"Type":"Heartbeat"}M-^A:{"State":"No service","Type":"NetworkServiceStatusChange"}M-^I^T{"Type":"Heartbeat"}M-^I^T{"Type":"Heartbeat"}M-^A3{"State":"LTE","Type":"NetworkServiceStatusChange"}M-^A3{"State":"LTE","Type":"NetworkServiceStatusChange"}M-^I^T{"Type":"Heartbeat"}M-^A1{"State":"Establishing PDN","Type":"StateChange"}M-^A0{"State":"PDN Established","Type":"StateChange"}M-^I^T{"Type":"Heartbeat"}M-^I^T{"Type":"Heartbeat"}M-^I^T{"Type":"Heartbeat"}[2]-  Exit 56                 curl --no-buffer --insecure --cert /tmp/tmp.AVi1FkonHA --key /tmp/tmp.EZP2f8QIj1 -H @/tmp/tmp.ZFQ9os2t5u --silent --output /tmp/ws.js https://192.168.11.1:35560/notification'


def replace(text):
    chars_to_replace = ['M-', '^A/', '^A*', '^A0', '^A3', '^A:', '^I^T', '^A1']
    for char in chars_to_replace:
        if char in text:
            text = text.replace(char, "")
    return text

# catOutput = data.replace('M-', '')
# catOutput = catOutput.replace('^A/', '')
# catOutput = catOutput.replace('^I^T', '')
# catOutput = catOutput.replace('^A*', '')
# catOutput = catOutput.replace('^A3', '')
# catOutput = catOutput.replace('^A0', '')
# catOutput = catOutput.replace('^A:', '')
# catOutput = catOutput.replace('}', '}\n')

catOutput = replace(data)
catOutput = catOutput.replace('}', '}\n')
#print(catOutput)

# print(output)
dictList = [d.strip() for d in catOutput.splitlines()]
dictList.pop()
#print repr(dictList)
data = [json.loads(i) for i in dictList]
for idx in data:
    for key, val in idx.items():
        print(val)
# #print(catOutput)
# test = json.dumps([catOutput])
# test = json.loads(test)
# print(type(test))
# print(test)

dictList = ['{"RebootCause":"Warm-restart","Type":"Connect"}',
'{"State":"LTE","Type":"NetworkServiceStatusChange"}',
'{"Type":"Heartbeat"}',
'{"State":"Establishing PDN","Type":"StateChange"}     ',
'{"State":"PDN Established","Type":"StateChange"}',
'{"Type":"Heartbeat"}',
'{"State":"No service","Type":"NetworkServiceStatusChange"}',
'{"Type":"Heartbeat"}',
'{"State":"LTE",     "Type":"NetworkServiceStatusChange"}',
'{"State":"Establishing PDN","Type":"StateChange"}',
'{"State":"LTE","Type":"NetworkServiceStatusChange"}',
'{"Type":"Heartbeat"}',
'{"State":     "PDN Established","Type":"StateChange"}',
'{"Type":"Heartbeat"}',
'{"Type":"Heartbeat"}',
'{"Type":"Heartbeat"}',
'{"Type":"Heartbeat"}',
'[2]   Exit 56                 curl --no-buffer --insecure -cert /tmp/tmp.lf28T7YaFU --key /tmp/tmp.BUy3R2oLJp -H @/tmp/tmp.3u3aWZkS7 --silent --output /tmp/ws.js https://192.168.11.1:3556/notification',
'[3]-  Done curl --no-buffer --insecure --cert /tmp/tmp.lf28T7YaFU --key /tmp/tmp.BUy3R2oLJp -H @/tmp/tmp.3u3aWZkS7 --silent --output /tmp/ws.js https://192.168.11.1:3556/notificati     on'
]

for i in range(len(dictList)):
    if dictList[i].startswith('['):
        dictList[i] = ''

dictList = [x for x in dictList if x]
print(dictList)