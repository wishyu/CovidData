import json
import os
import os.path
import datetime
import http.client


payload = ''
headers = {}
conn = http.client.HTTPSConnection("disease.sh")

def GetWorldometersPH() -> dict:
    conn.request("GET", "/v3/covid-19/countries/PH", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def GetVaccinePH(lastdays:str) -> dict:
    conn.request("GET", "/v3/covid-19/vaccine/coverage/countries/PH?lastdays=" + str(lastdays) + "&fullData=true", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

class CovidData():
    def __init__(self):
        self.__data = None
    def SetData(self, setData):
        self.__data = setData
    def ResetCurrentData(self):
        self.__data = None
    def GetOnlineData(self):
        self.__data = GetWorldometersPH()
        for i in ("updated","country","countryInfo","population","continent"):
            del self.__data[i]
    def ShowCovidData(self) -> dict:
        print("Cases: "+str(self.__data["cases"]))
        print("Cases Today: "+str(self.__data["todayCases"]))
        print("Deaths: "+str(self.__data["deaths"]))
        print("Deaths Today: "+str(self.__data["todayDeaths"]))
        print("Recovered: "+str(self.__data["recovered"]))
        print("Recovered Today: "+str(self.__data["todayRecovered"]))
        print("Active Cases: "+str(self.__data["active"]))
        print("Critical Cases: "+str(self.__data["critical"]))
        print("Tests: "+str(self.__data["tests"]))
        return self.__data
    def UpdateLocalReportData(self):
        self.GetOnlineData()
        DailyCOVIDDATA = self.__data
        updated = str(datetime.datetime.now().date())
        ListingToday = {updated: DailyCOVIDDATA}
        LocalTimelineCovidFile = "/tmp/" + os.environ.get("COVID_TIMELINE_FILE")
        if os.path.exists(LocalTimelineCovidFile):
            # File exist
            with open(LocalTimelineCovidFile, "r+", encoding='utf-8') as file:
                ListingPrev:dict = json.load(file)
                print(type(ListingPrev))
                if updated not in ListingPrev:
                    ListingPrev.update(ListingToday)
                else:
                    self.SetData(ListingPrev[updated])
                file.seek(0)
                json.dump(ListingPrev, file, ensure_ascii=False, indent=4)
                file.close()
        else:
            # File does not exist
            with open(LocalTimelineCovidFile, "w", encoding='utf-8') as file:
                ListingPrev = ListingToday
                json.dump(ListingToday, file, ensure_ascii=False, indent=4)
                file.close()
    def GetReportData(self, daysdelta:int) -> dict:
        # Returns mutltiple days COVIDDATA
        daterange = str(datetime.datetime.now().date() - datetime.timedelta(days=daysdelta))
        LocalTimelineCovidFile = "/tmp/" + os.environ.get("COVID_TIMELINE_FILE")
        listing:dict = None       
        if os.path.exists(LocalTimelineCovidFile):
            # File exist
            with open(LocalTimelineCovidFile, "r", encoding='utf-8') as file:
                listing = json.load(file)
                file.close()
        else:
            print("No Records Found")
            return
        if daterange in listing:
            returnlisting:dict = None
            for i in reversed(range(0,daysdelta)):
                datefind = str(datetime.datetime.now().date() - datetime.timedelta(days=i))
                if returnlisting and datefind in listing:
                    returnlisting.update({datefind:listing[datefind]})
                elif datefind in listing:
                    returnlisting = {datefind:listing[datefind]}
            return returnlisting
        else:
            print("Record insufficient")
    def GetSetCovidData(self, daysdelta:int) -> dict:
        # Returns single day COVIDDATA
        daterange = str(datetime.datetime.now().date() - datetime.timedelta(days=daysdelta))
        LocalTimelineCovidFile = "/tmp/" + os.environ.get("COVID_TIMELINE_FILE")
        listing:dict = None
        if os.path.exists(LocalTimelineCovidFile):
            # File exist
            with open(LocalTimelineCovidFile, "r", encoding='utf-8') as file:
                listing = json.load(file)
                file.close()
        else:
            return
        if daterange in listing:
            print(str(daterange) + " DATA FOUND")
            self.SetData(listing[daterange])
            return listing[daterange]
        else:
            print(str(daterange) + " DATA NOT FOUND")
            self.ResetCurrentData()
            return None
    def GetReport(self, duration:int) -> dict:
        Lisiting = self.GetReportData(duration)
        sumNewCases = 0
        sumNewDeath = 0
        sumNewRecov = 0
        for i in Lisiting:
            self.SetData(Lisiting[i])
            sumNewCases += self.__data["todayCases"]
            sumNewDeath += self.__data["todayDeaths"]
            sumNewRecov += self.__data["todayRecovered"]
        report = "Report shows data from " + str(list(Lisiting.keys())[0]) + " to " + str(list(Lisiting.keys())[-1])
        report += "\nNew Cases: " + str(sumNewCases) + "\nNew Death: " + str(sumNewDeath) + "\nNew Recovered: " + str(sumNewRecov)
        reportdict = {"totalCases": sumNewCases, "totalDeath": sumNewDeath,"sumNewRecov": sumNewRecov,"reportstr":report}
        return reportdict
    def Monthly(self) -> str:
        report = self.GetReport(30)
        toReturn = "Monthly Report:\n" + report["reportstr"]
        print(toReturn)
        return toReturn
    def Weekly(self) -> str:
        report = self.GetReport(7)
        toReturn = "Weekly Report:\n" + report["reportstr"]
        print(toReturn)
        return toReturn