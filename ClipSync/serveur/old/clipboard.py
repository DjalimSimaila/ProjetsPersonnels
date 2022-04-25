import os
import ast
import time
import datetime # date a l'americaine "y/m/d"



############################################
#                                          #     
#             ClipBoard class              #
#                                          #
############################################


class ClipBoard:
    def __init__(self, user : str):
        self.user = user
        self.clip , self.dateTable , self.deviceTable = self.loadData() 
        self.latestId = self.getClipsize()

    def loadData(self) -> dict:
        if not os.path.isfile(f'./{self.user}.clip'):
            data = {}
            data["deviceTable"] = {}
            data["dateTable"] = {}
            data["clipboard"] = {}
            os.system(f'touch ./{self.user}.clip')
            os.system(f'echo "{str(data)}" >> ./{self.user}.clip')
        dataFile = open(f'./{self.user}.clip','r')
        dataSting = dataFile.read()
        data = ast.literal_eval(dataSting)
        dataFile.close()
        return data['clipboard'],data['dateTable'],data['deviceTable']

    def getClipsize(self) -> int:
        return len(self.clip.keys()) -1

    def getLatestValue(self) -> str:
        if self.latestId == -1:
            return False
        value = {}
        #value[self.latestId] = self.clip[self.latestId]
        return self.clip[self.latestId]["value"]

    def getByDate(self,date)-> dict:
        dictValue = {}
        for id in self.dateTable[date]:
            dictValue[id] = self.clip[id]
        return dictValue

    def getByDevice(self,hostname):
        dictValue = {}
        for id in self.deviceTable[hostname]:
            dictValue[id] = self.clip[id]
        return dictValue

    def getById(self,id):
        return self.clip[id]

    def getAll(self):
        return True, self.clip

    def setNewValue(self, value,hostname) -> bool:
        currentDate = str(datetime.datetime.now().date())
        try:
            if currentDate not in self.dateTable:
                self.dateTable[currentDate] = []
            if hostname not in self.deviceTable:
                self.deviceTable[hostname] = []

            self.clip[self.latestId+1] = {"value" : value, "time" : time.time(), "hostname" : hostname}
            self.deviceTable[hostname].append(self.latestId+1)
            self.dateTable[currentDate].append(self.latestId+1)
            self.latestId += 1
            self.writefile()
            return True
        except:
            return False

    def writefile(self):
        fileData = {}
        fileData["clipboard"] = self.clip
        fileData["dateTable"] = self.dateTable
        fileData["deviceTable"] = self.deviceTable
        if os.path.isfile(f'./{self.user}.bak'):
            os.system(f"rm -f ./{self.user}.bak")
        else:
            os.system(f"cp ./{self.user}.clip {self.user}.bak")
        os.system(f"rm -f ./{self.user}.clip")
        dataFile = open(f'{self.user}.clip','w')
        dataFile.write(str(fileData))
        dataFile.close()
        return True
