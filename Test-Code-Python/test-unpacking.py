p = (4, 5)
x, y = p
print('Unpacking tuple: ', x, y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print('Unpacking List: ', name, shares, price, date)

# Split String to characters
testStr = 'ANSHU'
a, b, c, d, e = testStr
print('String to Characters ', a, b, c, d, e)

# Unpacking Elements from Iterables of Arbitrary Length
record = ('Dave', 'dave@example.com', '777-777-7777', '888-888-8888')
*name_email, phone_numbers = record
print(name_email, phone_numbers)