import datetime
import time
from datetime import timedelta

# given epoch time
# epoch_time = [
#     1653006360,
#     1653006401,
#     1653006632,
#               1653007230,
# 1653007830,
# 1653008431,
# 1653009030,
# 1653009630]

# for epochTime in epoch_time:
#     # using the datetime.fromtimestamp() function
#     date_time = datetime.datetime.fromtimestamp(epochTime)
#     # printing the value
#     print("Given epoch time:", epochTime)
#     print("Converted Datetime:", date_time )

for N in range(1, 91):
    time.sleep(1)
    print(int((datetime.datetime.now() - timedelta(days=N)).timestamp()*1000))