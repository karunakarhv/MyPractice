import os

# Specify the directory path
directory_path = 'C:\Src\camel-esb\esb-data-import\src\\test\java\com\humanforce\esb\dataimport\processor'

# List all files in the directory
file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Print the list of files
for file in file_list:
    print(file.replace('Test',''))
