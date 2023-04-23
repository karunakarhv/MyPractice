import string
import csv
import random

def createCsvFile():
    f = open("test-template-1.csv", "w")
    writer = csv.DictWriter(
        f, fieldnames=["EmployeeCode", "ShiftType", "Hours", "Type"])
    writer.writeheader()
    letters = string.ascii_uppercase
    typeList = ['Balance', 'Accrual', 'Deduction']
    for ind in range(0, 100000):
        empCode = random.randint(10000, 99999)
        shiftType = ''.join(random.choice(letters) for i in range(3))
        randomHours = random.uniform(1.0, 100.0)
        randomType = random.choice(typeList)
        test_dict = {
                    'EmployeeCode': empCode,
                    'ShiftType': shiftType,
                    'Hours': randomHours,
                    'Type': randomType
        }

        writer.writerow(test_dict)

    f.close()

def deleteEmptyRow():
    with open('test-template-1.csv') as input, open('test-template.csv', 'w', newline='') as output:
     writer = csv.writer(output)
     for row in csv.reader(input):
         if any(field.strip() for field in row):
             writer.writerow(row)

deleteEmptyRow()