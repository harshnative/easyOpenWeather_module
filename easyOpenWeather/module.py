import requests
from tabulate import tabulate
import json
import os
""" this is using the open weather api """

class WeatherDataClass():
    """
methods - setCityName(cityName)    ->    used to set cityName   #IMP
          getCityName()            ->    used to get cityName

          setApiKey(apiKey)        ->    used to set apiKey     #IMP
          getApiKey()              ->    used to get apiKey

          setStringKey()           ->    used to set custom api url
          getStringKey()           ->    used to get api url

          setList(listPass)        ->    used to query list for which data will be pulled   #IMP
                                         List can contain following queries - 
                                         1. temp        -> for temperature in kelvin
                                         2. tempInC     -> for temperature in celcius
                                         3. tempInF     -> for temperature in f
                                         4. tempMin     -> for min temp - unit is decided from above
                                         5. tempMax     -> for max temp - unit is decided from above
                                         6. pressure
                                         7. humidity
                                         8. wind speed
                                         9. wind direction 
                                         10.description  

          getInfo()                ->    for getting result in dictionary form
                                         please set apiKey , cityName , List before using this function

          printData()              ->    for printing the data directly into tabular form
                                         please set apiKey , cityName , List before using this function

    """

    # building up constructor to set the defualt value's
    def __init__(self):
        self.apiKey = None
        self.cityName = None
        self.stringKey = "https://api.openweathermap.org/data/2.5/weather?q="
        self.data = None
        self.jsonData = None
        self.resultDict = {}
        self.listPass = None
        self.oneTimeRun = False

    
    # getters and setters for custom string key
    def setStringKey(self , stringKey):
        """https://api.openweathermap.org/data/2.5/weather?q="""
        self.stringKey = stringKey

    def getStringKey(self):
        return self.stringKey


    # getters and setters for cityName for which the weather data will be pulled
    def setCityName(self , cityName):
        self.cityName = str(cityName)

    def getCityName(self):
        return self.cityName

    
    # getter and setters for api key
    def setApiKey(self, apiKey):
        self.apiKey = str(apiKey)
    
    def getApiKey(self):
        return self.apiKey


    # function to make the final url which will be used to make request
    def makeUrl(self): 
        if((self.cityName or self.apiKey) == None):
            raise NotImplementedError("Please set cityName and apiKey")
        
        self.stringKey = self.stringKey + self.cityName + "&appid=" + self.apiKey


    # function to get the weather data from the open weather server
    def getDataFromWeb(self):
        try:
            self.data = requests.get(self.stringKey).text
        except Exception as e:
            errorString = "Some error occured while getting data from web , make sure apiKey and cityName were correct and use correct string key if changed ."+" Here is Exception Raised during process : " + str(e)
            raise RuntimeError(str(errorString))
        

    # function to convert the data from the web to json format
    def loadDataIntoJson(self):
        if self.data == None:
            raise RuntimeError("self.data is still None in loadDataIntoJson method")
        else:
            self.jsonData = json.loads(self.data)


    # function to convert the temp from k to c
    def convTempToC(self , tempInKPass):
        return (tempInKPass - 273)
    

    # function to convert the temp from c to f
    def convTempToF(self , tempInCPass):
        return (( tempInCPass * (9/5) ) + 32)

    
    # function to set list of commands
    def setList(self , passList):
        self.listPass = list(passList)

    # function to extract info according to commands in listPassed
    def extractInfo(self):

        if(self.listPass == None):
            raise RuntimeError("Please pass some commands for extracting info")
        
        else:  
            # getting temp in k
            try:
                tempInK = float(self.jsonData["main"]["temp"])
            except Exception as e:
                raise RuntimeError("could not get temperature" , str(e))
                
            # getting temp MAX in k
            try:
                tempInKMax = float(self.jsonData["main"]["temp_max"])
            except Exception:
                raise RuntimeError("could not get max temperature")

            # getting temp MIN in k
            try:
                tempInKMin = float(self.jsonData["main"]["temp_min"])
            except Exception:
                raise RuntimeError("could not get min temperature")
                

            # adding temperature's to result dict according to command's
            if("temp" in self.listPass):
                self.resultDict["temp"] = round(tempInK , 2)

                if("tempMin" in self.listPass):
                    self.resultDict["tempMin"] = round(tempInKMin , 2)
                    
                if("tempMax" in self.listPass):
                    self.resultDict["tempMax"] = round(tempInKMax , 2)
                
            # if asked in c
            elif("tempInC" in self.listPass):

                tempInC = self.convTempToC(tempInK)
                self.resultDict["tempInC"] = round(tempInC , 2)

                if("tempMin" in self.listPass):
                    tempInCMin = self.convTempToC(tempInKMin)
                    self.resultDict["tempMin"] = round(tempInCMin , 2)
                    
                if("tempMax" in self.listPass):
                    tempInCMax = self.convTempToC(tempInKMax)
                    self.resultDict["tempMax"] = round(tempInCMax , 2)
                
            # if asked in f
            elif("tempInF" in self.listPass):

                tempInC = self.convTempToC(tempInK)
                tempInF = self.convTempToF(tempInC)
                self.resultDict["tempInC"] = round(tempInF , 2)

                if("tempMin" in self.listPass):
                    tempInCMin = self.convTempToC(tempInKMin)
                    tempInFMin = self.convTempToF(tempInCMin)
                    self.resultDict["tempMin"] = round(tempInFMin , 2)
                    
                if("tempMax" in self.listPass):
                    tempInCMax = self.convTempToC(tempInKMax)
                    tempInFMax = self.convTempToF(tempInCMax)
                    self.resultDict["tempMax"] = round(tempInFMax , 2)
                

            # for pressure
            if("pressure" in self.listPass):
                pressure = self.jsonData["main"]["pressure"]
                self.resultDict["pressure"] = pressure

            # for humidity
            if("humidity" in self.listPass):
                humidity = self.jsonData["main"]["humidity"]
                self.resultDict["humidity"] = humidity

            # for windSpeed
            if("windSpeed" in self.listPass):
                windSpeed = self.jsonData["wind"]["speed"]
                self.resultDict["windSpeed"] = windSpeed
            
            # for windDirection
            if("windDirection" in self.listPass):
                windDirection = self.jsonData["wind"]["deg"]
                self.resultDict["windDirection"] = windDirection

            # for clouds
            if("clouds" in self.listPass):
                clouds = self.jsonData["clouds"]["all"]
                self.resultDict["clouds"] = clouds

            # for discription
            if("description" in self.listPass):
                description = self.jsonData["weather"][0]["description"]
                self.resultDict["description"] = description


    # function to return the result in the form of dictionary 
    def getInfo(self):
        self.makeUrl()
        self.getDataFromWeb()
        self.loadDataIntoJson()
        self.extractInfo()
        self.oneTimeRun = True
        return self.resultDict


    # function to print the weather details in the form of a table
    def printData(self):

        try:
            dictGetted = self.getInfo()
        except Exception as e:
            if(self.oneTimeRun == True):
                raise RuntimeError("Please don't use getInfo() before printData(), it is already included")
            else:
                raise Exception(str(e))

        tabulateList = []

        for i,j in dictGetted.items():
            tempList = []
            tempList.append(str(i))
            tempList.append(str(j))
            tabulateList.append(tempList)
    
        print(tabulate(tabulateList, headers=['Weather Query', 'Data Received']))
        


# just for testing purpose
if __name__ == "__main__":
    obj = WeatherDataClass()

    obj.setCityName("london")
    obj.setApiKey("fe82651e607e46db61dba45e39aa7e17")
    
    listPass = ["tempInC" , "tempMin" , "tempMax" , "pressure" , "humidity" , "windSpeed" , "windDirection" , "clouds" , "description"]

    obj.setList(listPass)
    obj.getInfo()
    obj.printData()