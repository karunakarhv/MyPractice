import csv

with open(r'C:\Users\karunakarv\Downloads\Event_import_template.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row)
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        line_count += 1
    print(f'Processed {line_count} lines.')
