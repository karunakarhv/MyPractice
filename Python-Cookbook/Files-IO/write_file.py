# Write text to file
with open(file='somefilewrite.txt', mode='wt') as f:
    # Writing to file
    f.write('Test write')

# Append to existing text to file
with open(file='somefilewrite.txt', mode='at') as f:
    # Writing to file
    f.write('\nTest write append')

# Printing to a file
with open(file='somefilewrite.txt', mode='at') as f:
    print('\nHello world!', file=f)
