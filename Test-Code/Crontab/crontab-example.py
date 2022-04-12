from crontab import CronTab

cron = CronTab(user='karunakar.venkatesh')
job1 = cron.new(command='python3 /home/karunakar.venkatesh/MyPractice/Test-Code/Crontab/example1.py')
job1.minute.every(1)

job2 = cron.new(command='python3 /home/karunakar.venkatesh/MyPractice/Test-Code/Crontab/example1.py')
job2.hour.every(2)

for item in cron:
    print(item)

cron.write()