from CapstoneData import CovidData
import FTPfunc
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=16, minute=20)
def scheduled_job():
    FTPfunc.download_file()
    a = CovidData()
    a.UpdateLocalReportData()
    a.ShowCovidData()
    FTPfunc.upload_file()
    print('Tweet Me')