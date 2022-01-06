from CapstoneData import CovidData
import FTPfunc
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=17, minute=40)
def scheduled_job():
    # Daily Report and Record Update @ 4:40pm
    print("Updating Covid Data File and Posting to Twitter")
    a = CovidData()
    FTPfunc.download_file()
    a.UpdateLocalReportData()
    a.ShowCovidData() # Returns dict for twitter posting, add custom module
    FTPfunc.upload_file()
    print("Tweet Me, api for tweeting")
# @sched.scheduled_job('cron', hour=17, minute=45, day_of_week="sat")
# def scheduled_job():
#     # Weekly Report @ 4:45 Saturday
#     print("Weekly Report and Posting to Twitter")
#     a = CovidData()
#     FTPfunc.download_file()
#     toPrint = a.Weekly() # Returns string for twitter posting, add custom module
#     print(toPrint)
# @sched.scheduled_job('cron', day ="last sat", hour=17, minute=50, day_of_week="sat")
# def scheduled_job():
#     # Monthly Report @ 4:50 Saturday
#     print("Monthly Report and Posting to Twitter")
#     a = CovidData()
#     FTPfunc.download_file()
#     toPrint = a.Monthly() # Returns string for twitter posting, add custom module
#     print(toPrint)
sched.start()