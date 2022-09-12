my_list = {
    'Output': [{'name':'karun', 'emp':3},{'name':'adithi', 'emp':1},{'name':'anshu', 'emp':2}],
    'Status': 0,
    'ErrorMessages': ['Processed successfully.']
}

print(my_list['Output'])

for index in my_list['Output']:
    if index['name'] == "karun":
        print(index)

strValue = "2022-09-06T12:55:18"

print(strValue.split('T'))