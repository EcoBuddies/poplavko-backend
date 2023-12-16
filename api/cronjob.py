from crontab import CronTab

cron = CronTab(user='root')
job = cron.new(command='python3 api/xml-parser.py')

job.minute.every(1)

cron.write_to_user(user='root')

jobs = cron.jobs()

for job in jobs:
    if job.command == 'python3 api/xml-parser.py':
        print("Job found:", job)