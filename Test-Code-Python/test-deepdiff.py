from deepdiff import DeepDiff

permitted_modifications = ['historyId', 'processDate']
t1 = {'statusCode': 200, 'body': [{'fileName': '203_202303.0_1.PDF', 'period': {'start': '2022-07-18', 'end': '2022-07-31'}, 'metadata': {'instanceId': '26804d2c-5578-4bc5-b193-5e3fc872bb0b', 'taskId': '4dad4413-e494-400c-9828-c178b0a72f28', 'historyId': '65608cdc-b012-469f-b9df-65c0e6d37def', 'payrollCode': '203', 'date': '2022-08-03'}, 'processDate': 1668976337381, 'status': 1}]}
t3 = {'statusCode': 200, 'body': [{'fileName': '203_202303.0_1.PDF', 'period': {'start': '2022-07-18', 'end': '2022-07-31'}, 'metadata': {'instanceId': '26804d2c-5578-4bc5-b193-5e3fc872bb0b', 'taskId': '4dad4413-e494-400c-9828-c178b0a72f28', 'historyId': 'f612fec4-d4dc-4349-acc0-f7f7068722f7', 'payrollCode': '203', 'date': '2022-08-03'}, 'processDate': 1669148878481, 'status': 1, 'test':1}]}

def test_deepdiff():
    diff = DeepDiff(t1, t3, ignore_order=True, view="tree")
    print(diff)
    success = True
    if 'dictionary_item_added' in diff:
        print('Added {}'.format(diff['dictionary_item_added']))
        success = False
        return success
    if 'dictionary_item_removed' in diff:
        print('Removed {}'.format(diff['dictionary_item_removed']))
        success = False
        return success
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

test_deepdiff()