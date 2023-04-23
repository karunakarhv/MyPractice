import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test")
parser.add_argument("-q", "--quit")
parser.add_argument("-l", "--logs")
args = parser.parse_args()
# help(args)
print(type(args.quit))
print(args.logs)
print(args.test)
#     print(args.test)
# else:
#     print('Nothing')
testCaseName =  "WINNF.FT.C.REG.10"
currentTime = datetime.utcnow().replace(microsecond=0).isoformat()
print(testCaseName+'_'+currentTime+'.'+'log')

test = False
if test is not None:
    print('deactivate')