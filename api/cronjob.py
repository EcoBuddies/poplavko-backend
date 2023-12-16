from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='python3 /home/pi/Desktop/SmartHome/api/cronjob.py')
job.minute.every(1)
cron.write()