import json


class DataClass:
    def __init__(self):
        self.globalData = {"message":"Hello from Flask!", "ok":"true"}
        self.fileData = {} 

    def loadJson(self, filename):
        with open(filename) as json_file:
                self.fileData = json.load(json_file)

    def getJsonFromFile(self, filename):
        self.loadJson(filename)
        return self.fileData

                

