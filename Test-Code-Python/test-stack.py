stack = []
dec = 2

def zero(func=None): #your code here
    global dec
    stack.append(0)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def one(func=None): #your code here
    global dec
    stack.append(1)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def two(func=None): #your code here
    global dec
    stack.append(2)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def three(func=None): #your code here
    global dec
    stack.append(3)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def four(func=None): #your code here
    global dec
    stack.append(4)
    print(stack)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def five(func=None): #your code here
    global dec
    stack.append(5)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def six(func=None): #your code here
    global dec
    stack.append(6)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def seven(func=None): #your code here
    global dec
    stack.append(7)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def eight(func=None): #your code here
    global dec
    stack.append(8)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def nine(func=None): #your code here
    global dec
    stack.append(9)
    print(stack)
    if dec == 0:
        return calculate()
    else:
        dec = dec - 1

def plus(func=None): #your code here
    global dec
    stack.append('+')
    print(stack)
    dec = dec - 1

def minus(func=None): #your code here
    global dec
    stack.append('-')
    dec = dec - 1

def times(func=None): #your code here
    global dec
    stack.append('*')
    dec = dec - 1

def divided_by(func=None): #your code here
    global dec
    stack.append('//')
    dec = dec - 1

def calculate():
    global dec
    value1 = stack.pop()
    operator = stack.pop()
    value2 = stack.pop()
    dec = 2
    if operator == '*':
        return value1 * value2
    elif operator == '+':
        return value1 + value2
    elif operator == '//':
        return value1//value2
    else:
        return value1 - value2

print(seven(times(five())))
print(four(plus(nine())))