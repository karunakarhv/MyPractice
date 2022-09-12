from deepdiff import DeepDiff

permitted_modifications = ['date', 'location']
t1 = {1:1, 'date':2, 3:3, 'employee1':{'date':'', 'location':'BLR', 'test':''}, 'employee2':{'date':'', 'location':'HYD', 'test':'karun'}}
t3 = {1:1, 'date':3, 3:3, 'employee1':{'date':'', 'location':'HYD', 'test':'karun'}}

def test_deepdiff():
    diff = DeepDiff(t1, t3, ignore_order=True, view="tree")
    print(diff)
    success = True
    if 'dictionary_item_added' in diff:
        print(diff['dictionary_item_added'])
    if 'dictionary_item_removed' in diff:
        print(diff['dictionary_item_removed'])
    if 'values_changed' in diff:
            print('inside permitted modifications')
            for index in permitted_modifications:
                for change in diff['values_changed']:
                    print(change)
                    if index in change.up.t2:
                        print(index)
                        print(change.up.t1)
                        print(change.up.t2)
                        print('Value is permitted')
                        success = success and True
    print('Success ', success)
    # No Changes
    if not diff:
        print('Empty')

expected = {1:1, 2:2, 3:3}
actual = {1:1, 2:3, 3:3}

def deepDiff():
    changes = DeepDiff(expected, actual)
    print('Type {}'.format(type(changes)))
    print('Changes {}'.format(changes))

deepDiff()