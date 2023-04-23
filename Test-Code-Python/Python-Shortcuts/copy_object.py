# Copying an object
# We want to copy an object. However, when you assign an object, pass it as
# as an argument or return it as a result. Python uses a reference to the original
# object, without making a copy

import copy
existing_list = [1, 2, 3, 4]
new_list = copy.copy(existing_list)
# new_list = existing_list
new_list.append(5)
print(new_list, existing_list)