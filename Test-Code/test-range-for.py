
def func(n):
    for i in range(1, n+1):
        print(i)

def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if (i%3 == 0) and (i%5 == 0):
            print('FizzBuzz')
        elif (i%3 == 0) and not(i%5==0):
            print('Fizz')
        elif (i%5 == 0) and not(i%3==0):
            print('Buzz')
        elif not((i%3 == 0) and (i%5==0)):
            print(i)


#fizzBuzz(15)

test = [x for x in 'strhow']
print(test)

def winner(erica, bob):
    # Write your code here
    scoringTable = {'E':1, 'M':3, 'H':5}
    ericaList = [x for x in erica]
    bobList = [x for x in bob]
    scoreErica = 0
    scoreBob = 0
    for x in ericaList:
        scoreErica += scoringTable[x]
    for x in bobList:
        scoreBob += scoringTable[x]
    if scoreErica > scoreBob:
        return "Erica"
    elif scoreErica < scoreBob:
        return "Bob"
    else:
        #scoreErica == scoreBob
        return "Tie"

print(winner('E', 'E'))

# Function to Find the first repeated word in a string
from collections import Counter

def firstRepeat(input):

    # first split given string separated by space
    # into words
    words = input.split(' ')

    # now convert list of words into dictionary
    dict = Counter(words)
    print(dict)

    # traverse list of words and check which first word
    # has frequency > 1
    for key in words:
        if dict[key]>1:
            print (key)
            return
firstRepeat('He had had requested something')