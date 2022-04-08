from crontab import CronTab

cron = CronTab(user='karunakar.venkatesh')
job = cron.new(command='python3 /home/karunakar.venkatesh/MyPractice/Test-Code/Crontab/example1.py')
job.minute.every(1)

cron.write()