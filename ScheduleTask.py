from CapstoneData import CovidData
import FTPfunc
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=22, minute=50)
def scheduled_job():
    FTPfunc.download_file()
    a = CovidData()
    a.UpdateLocalReportData()
    a.ShowCovidData()
    FTPfunc.upload_file()
    print('Tweet Me')