import random
import string

letters = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters #+ string.whitespace
# + string.punctuation
for j in range(1):
    shiftType = ''.join(random.choice(letters) for i in range(31))
    print(shiftType)


testStr = 'Test1234567000000000'


def randomDigits(digits):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return random.randint(lower, upper)

# print(randomDigits(6))