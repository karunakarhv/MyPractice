import csv
emailId = "hftestqa"
emailCompany = "gmail.com"

with open('test.csv', mode='w', newline='') as f:
    csv_writer = csv.writer(f)
    for i in range(1, 15001):
        temp = emailId + "+" + str(i) + "@"+ emailCompany
        csv_writer.writerow([temp])