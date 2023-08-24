# Print without separator
print('ACME', 1, 3, 4)
# Print with separator
print('ACME', 1, 2, 3, sep=',')
# Print with separator
print('ACME', 1, 2, 3, sep=',', end='!!\n')

# str join only concatentes the string data type, but whereas print

row = ('ACME', 1, 2, 4)
#print(','.join(row))
# We need to perform for loop.
print(','.join(str(x) for x in row))
# Instead of doing this, we can do it in a simpler way.
print(*row, sep=',')