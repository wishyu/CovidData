from CapstoneData import CovidData
import FTPfunc
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='0-6', hour=15, minute=30)
def scheduled_job():
    a = CovidData()
    FTPfunc.download_file()
    a.UpdateLocalReportData()
    a.ShowCovidData()
    FTPfunc.upload_file()
    print('This job is run every weekday at 5pm.')

sched.start()