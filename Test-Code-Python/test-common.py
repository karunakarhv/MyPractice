list_1 = ['NonAttend', 'DefaultGradeMax', 'EventManager', 'HideRosterEndTime', 'ColorCode', 'Rate', 'PayRate', 'MinAge', 'LastEdit', 'DefaultProfile', 'DefaultStartTime', 'DefaultEndTime', 'DefaultRateCalcMethod', 'ExportCode', 'DefaultGradeMin']
list_2 = ['GuidKey', 'DefaultPayRate', 'ModifiedAt', 'DefaultHourlyRate', 'FirstName', 'LastEdit', 'DefaultLocation', 'Name', 'DefaultEndTime', 'DefaultRole', 'DefaultStartTime', 'PayrollCode']

# Common Elements between the two lists
common_elements = []
uncommon_elements = []
for index in list_2:
    for innerLoop in list_1:
        if index == innerLoop:
            common_elements.insert(-1,innerLoop)
        else:
            uncommon_elements.insert(-1, index)

# print(f'Common Elements {common_elements}')
print(f'Common Elements {set(list_2).intersection(list_1)}')
print(f'Difference between two lists {set(list_2).difference(list_1)}')
print(f'Difference between two lists {set(list_1).difference(list_2)}')