import cv2

import DataClass

class FileAccess():
    fileName = ""
    data = []       #list of Data objects from DataClass
    vecSize = 0

    def __init__(self,fileName):
        self.data = []
        self.fileName = fileName
        self.loadData()
        # self.vecSize = len(self.data[0].getFeats())/3   #part of ver. 2.0
        self.vecSize = len(self.data[0].getFeats())


    def loadData(self):
        file = open(self.fileName,"r")
        numLines = sum(1 for line in open(self.fileName))
        #numLines = open(self.fileName,"r")
        for i in range(0,numLines):
            strLine = file.readline()
            strLine = strLine.strip('\n')
            feats = strLine.split(' ')
            label = feats[len(feats)-1]
            feats = feats[0:len(feats)-2]
            dataObj = DataClass.Data(feats,label)
            self.data.append(dataObj)
            #print "Appending data"

    def getData(self):
        return self.data

    def getVecSize(self):
        return self.vecSize






