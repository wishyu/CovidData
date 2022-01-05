from CapstoneData import CovidData
import FTPfunc
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=16, minute=40)
def scheduled_job():
    print("4:00")
    a = CovidData()
    FTPfunc.download_file()
    a.UpdateLocalReportData()
    a.ShowCovidData()
    FTPfunc.upload_file()
    print('Tweet Me')
sched.start()