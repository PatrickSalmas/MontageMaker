import FileAccessClass

class Classifier():
    type = ""
    x = -1
    y = -1
    feat = -1
    weights = []
    data = []
    error = 1
    R = 0
    G = 0
    B = 0

    stepCount = 30  #this var is truly a range

    def __init__(self,feat,weights,data,R,G,B,bool):
        #self.feat = feat/3    #part of sol. 2.0
        self.feat = feat
        self.weights = weights
        self.data = data
        self.R = R
        self.G = G
        self.B = B
        if bool:
            #self.calcError()   # used for ver. 2.0
            self.calcError2()


    def getType(self): return self.type
    def getFeat(self): return self.feat
    #def getError(self):

    def calcError2(self):
        total = 0.0
        errors = 0.0
        for i in range(0,len(self.data.getData())):
            vec = self.data.getData()[i].getFeats()
            label = self.data.getData()[i].getLabel()

            if(self.feat >= len(vec) or self.feat+1 >= len(vec) or self.feat+2 >= len(vec)):
                self.error = 1.0
                return

            if(abs(self.R - int(vec[self.feat])) <= self.stepCount and abs(self.G - int(vec[self.feat+1])) <= self.stepCount and abs(self.B - int(vec[self.feat+2])) <= self.stepCount):
                if(label == "-1"):
                    errors += 1 * self.weights[i]
            elif(label == "1"):
                errors += 1 * self.weights[i]

            total += 1 * self.weights[i]

        self.error = errors/total


    #used for ver. 2.0
    def calcError(self):
       total = 0.0
       errors = 0.0
       j = 1
       j = j * self.feat * 3
       for i in range(0,len(self.data.getData())):
           vec = self.data.getData()[i].getFeats()
           label = self.data.getData()[i].getLabel()

#           if(abs(int(self.R) - int(vec[j])) <= 15 & abs(int(self.G) - int(vec[j+1])) <= 15 & abs(int(self.B) - int(vec[j+2])) <= 15 & str(label)=="-1"):
           if(abs(self.R - int(vec[j])) <= self.stepCount and abs(self.G - int(vec[j+1])) <= self.stepCount and abs(self.B - int(vec[j+2])) <= self.stepCount):
               if(label == "-1"):
                    errors += 1 * self.weights[i]
           elif(label == "1"):
               errors += 1 * self.weights[i]

#           elif(abs(self.R - int(vec[j])) > 15 & abs(self.G - int(vec[j+1])) > 15 & abs(self.B - int(vec[j+2])) > 15 & label=="1"):
           #print i
           total += 1 * self.weights[i]
       #print total
       self.error = errors/total


    def getError(self):
        return self.error


    def getHx(self,index,dataIn):  #need to pass data from set in which we are calcing error, NOT self.data
        label = dataIn.getData()[index].getLabel()
        r = dataIn.getData()[index].getFeats()[self.feat]               #ver 2.0 multiplies the index by 3
        g = dataIn.getData()[index].getFeats()[self.feat+1]             #ver 3.0 DOES NOT multiply index by 3 (current)
        b = dataIn.getData()[index].getFeats()[self.feat+2]
        if(abs(self.R - int(r)) <= self.stepCount and abs(self.G - int(g)) <= self.stepCount and abs(self.B - int(b)) <= self.stepCount):
            return 1
        else:
            return -1


