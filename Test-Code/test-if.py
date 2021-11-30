verify = [None, True, False]

for idx in verify:
    if not idx and idx is not None:
        print('check')
    else:
        print('not check')