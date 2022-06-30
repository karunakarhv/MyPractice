for i in range(100):
    with open('{}-test.csv'.format(i), 'w') as f:
        f.write('test-{}'.format(i))