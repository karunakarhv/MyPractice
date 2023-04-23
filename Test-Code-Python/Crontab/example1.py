from datetime import datetime
myFile = open('/home/karunakar.venkatesh/MyPractice/Test-Code/Crontab/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))