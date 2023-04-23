from collections import deque
# Adding or Popping items from either end of a Queue has O(1) Complexity
# List - Where inserting and removing items from the front of the list has O(N) complexity.
my_log = deque(maxlen=4)
my_log.append(1)
my_log.append(2)
my_log.append(3)
my_log.append(4)
print('Old Log: ', my_log)
my_log.append(5)
print('New Log: ', my_log)