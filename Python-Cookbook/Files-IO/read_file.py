"""Reading File in text mode
"""
with open(file='somefile.txt', mode='rt') as f:
    # Reading the entire file as a single string
    print(f.read())

# Read the file line by line
with open(file='somefile.txt', mode='rt') as f:
    # Reading the entire file as a single string
    i = 1
    for line in f:
        print('Line {} {}'.format(i, line))
        i = i + 1

# with statement allows to close the file automatically when the with block ends.
