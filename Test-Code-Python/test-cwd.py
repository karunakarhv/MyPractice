import os

print os.getcwd()
print os.path.basename(__file__)
print os.path.abspath(__file__)
value = os.path.dirname(__file__) + '/../../test.py'
print value
