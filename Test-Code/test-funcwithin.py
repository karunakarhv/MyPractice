import time

def func_name(a, b, c):
    print(a, b, c)

stepsDict = {
    '0': [func_name, [0, 1, 2], 0],
    '1': [func_name, [0, 1, 2], 2],
    '2': [func_name, [0, 1, 2], 0],
    '3': [func_name, [0, 1, 2], 5],
}
def runFunc(func, args, delay):
    func(args[0], args[1], args[2])
    if delay > 0:
        time.sleep(delay)

for _, value in stepsDict.items():
    runFunc(value[0], value[1], value[2])

