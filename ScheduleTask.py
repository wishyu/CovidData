from CapstoneData import CovidData
import FTPfunc

a = CovidData()
# a.UpdateLocalReportData()
# a.GetSetCovidData(0)
# a.ShowCovidData()
# a.PopulateTimeline()
# FTPfunc.upload_file()
FTPfunc.download_file()
a.Weekly()