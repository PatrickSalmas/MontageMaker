import ClassifierClass
import FileAccessClass
from math import log
from math import e
from math import pow
import sys

class Boost():

    stepCount = 10
    thresh = .1

    D = []
    C = []
    errMap = []
    W = []
    Alph = []
    trainFile = ""
    testFile = ""
    data = ""
    testData = ""
    pickedFeats = {}
    calcs = {}

    def __init__(self,trainFile,bool):
        if bool:
            self.trainFile = trainFile
            self.data = FileAccessClass.FileAccess(self.trainFile)
            self.initD()
        else:
            self.buildCSet(trainFile)

#    def __init__(self,classFile,bool):
 #       self.buildCSet(classFile)



    def initD(self):
        weight = 1.0/len(self.data.getData())
        for i in range(0,len(self.data.getData())):
            self.D.append(weight)
            self.W.append(0.0)

    def diffCheck(self,r,g,b):
        if(abs(r-g) > 50 or abs(r-b) > 50 or abs(g-b) > 50):
            return False
        return True

    def getBestH(self):
        bestErr = 1.0
        bestH = 0

        #bestClass = ClassifierClass.Classifier(1,self.W)
        for i in range(0,self.data.getVecSize(),3):    #added 3-step for ver. 3.0
            if(i%100 == 0):
                print '\t',"finished pixel ",i         #is actually referring to position in feature vector (num pix * 3 (RGB))
            for r in range(0,255,self.stepCount):
                for g in range(0,255,self.stepCount):
                    for b in range(0,255,self.stepCount):
                        if(self.diffCheck(r,g,b) == False): continue
                        #if(str(r)+" "+str(g)+" "+str(b)+" "+str(i) in self.calcs):
                         #   ht = self.calcs[str(r)+" "+str(g)+" "+str(b)+" "+str(i)]
                        #else:
                        ht = ClassifierClass.Classifier(i,self.D,self.data,r,g,b,True)
                         #   self.calcs[str(r)+" "+str(g)+" "+str(b)+" "+str(i)] = ht
                        #print ht.getError()," ",r," ",g," ",b
                        if(ht.getError() < bestErr and ht.getFeat() not in self.pickedFeats):
                            bestErr = ht.getError()
                            bestH = ht
                            print "Found new best with error: ",bestErr," and RGB ",ht.R," ",ht.G," ",ht.B," and pix ",bestH.getFeat()

        return bestH

    #Called in the case that the best classifiers for a particular training set has already been calculated
    def buildCSet(self,classFile):
        file = open(classFile,"r")
        numLines = sum(1 for line in open(classFile))
        for i in range(0,numLines):
            strLine = file.readline()
            traits = strLine.split()
            ht = ClassifierClass.Classifier(int(traits[3]),self.D,self.data,int(traits[0]),int(traits[1]),int(traits[2]),False)
            self.C.append(ht)
            self.Alph.append(traits[4])
#            print i," R: ",ht.R," G: ",ht.G," B: ",ht.B," feat: ",ht.feat," and alph: ",traits[4]



    def run2(self):
         for i in range(540,self.data.getVecSize()):
         #for i in range(400,self.data.getVecSize()):
         #for i in range(540,545):
            #if(i%100 == 0):
            print " --- ","finished pixel ",i," --- "
            for r in range(0,255,self.stepCount):
                for g in range(0,255,self.stepCount):
                    for b in range(0,255,self.stepCount):
                        if(self.diffCheck(r,g,b) == False): continue
                        ht = ClassifierClass.Classifier(i,self.D,self.data,r,g,b,True)
                        if(ht.getError() < .35):
                            print '\t',ht.getError()
                        if(ht.getError() < self.thresh):
                         #   self.C.append(ht)
                          #  err = ht.getError()
                          #  alpha = (1 - err) / err
                          #  alpha = 0.5*log(alpha)
                          #  self.Alph.append(alpha)
                          #  print "Pixel ",ht.getFeat()," err --> ",ht.getError()

                            #print "Possible ht w/ val ",ht.getError()," at pixel ", i
                            #if(ht.getFeat() in self.pickedFeats and ht.getError() < self.pickedFeats[ht.getFeat()]):
                            if(len(self.C) == 0):
                                self.C.append(ht)
                                err = ht.getError()
                                alpha = (1 - err) / err
                                alpha = 0.5*log(alpha)
                                self.Alph.append(alpha)
                                print "Pixel ",ht.getFeat()," err --> ",ht.getError()
                                continue

                            top = self.C[len(self.C)-1]
                            if(ht.getError() < top.getError() and ht.getFeat() == top.getFeat()):
                                #self.pickedFeats[ht.getFeat()] = ht.getError()
                                popped = self.C.pop()
                                self.Alph.pop()
                                self.C.append(ht)
                                err = ht.getError()
                                alpha = (1 - err) / err
                                alpha = 0.5*log(alpha)
                                self.Alph.append(alpha)
                                print "Pixel ",ht.getFeat()," err --> ",ht.getError()
#                                print '\t'," Popping ",popped.getFeat()," and pushing ",ht.getFeat()
                            #elif(ht.getFeat() not in self.pickedFeats):
                            elif(ht.getFeat() != top.getFeat()):
                                #self.pickedFeats[ht.getFeat()] = ht.getError()
                                self.C.append(ht)
                                err = ht.getError()
                                alpha = (1 - err) / err
                                alpha = 0.5*log(alpha)
                                self.Alph.append(alpha)
                                print "Pixel ",ht.getFeat()," err --> ",ht.getError()
                     #           print "Pixel ",ht.getFeat()," err --> ",ht.getError()

         #for val in self.pickedFeats.itervalues():
          #   self.C.append(val)
           #  err = val
            # alpha = (1 - err) / err
             #if(alpha == 0):
             #   alpha =
            # print "attempting to log value ", alpha
            # alpha = 0.5*log(alpha)
            # self.Alph.append(alpha)

    def run(self):
        best = self.getBestH()
        self.pickedFeats[best.getFeat()] = 1
        print "picked pixel ",best.getFeat()," and error ",best.getError(), " and ",best.R,"-",best.G,"-",best.B
        self.C.append(best)
        err = best.getError()
        if(err == 0): alpha = sys.maxint
        else: alpha = (1 - err) / err
        alpha = 0.5*log(alpha)
        self.Alph.append(alpha)

        for i in range(0,len(self.data.getData())):
            exp = (alpha*-1)*int(self.data.getData()[i].getLabel())*best.getHx(i,self.data)
            self.W[i] = self.D[i]*pow(e,exp)

        z = 0.0
        for i in range(0,len(self.W)):
            z += self.W[i]

        for i in range(0,len(self.data.getData())):
            val = self.W[i]/z
            self.D[i] = val


    #Need to make new trainError that doesn't call .getHx(i)
    #def trainError2(self):
     #   total = 0.0
      #  errors = 0.0
       # for i in range(0,len(self.data.getData())):
            #file = open("killClass.txt","r")
            #numLines = sum(1 for line in open(self.fileName))
       #     sum = 0.0
      #      for t in range(0,len(self.C)):
             #   val =


    def calcError(self,fileName):
        dataTest = FileAccessClass.FileAccess(fileName)
        print "Error file is ",len(dataTest.getData())
        total = 0.0
        errors = 0.0
        for i in range(0,len(dataTest.getData())):
            sum = 0.0
            for t in range(0,len(self.C)):
                val = self.Alph[t]*self.C[t].getHx(i,dataTest)
                sum += val

            label = int(dataTest.getData()[i].getLabel())

            #print sum," and ",label
            #if(label < 0):
               # print "label is less than 0"
            if(sum < 0 and label > 0):
                errors += 1
            elif(sum > 0 and label < 0):
                errors += 1

            total += 1

        print "Error: ",errors/total



