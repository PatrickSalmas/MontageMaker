import cv2
import KillCollector

class CaptureData():

    def displayBox(self,frame,x,y):
        for i in range(x,x+25):
            for j in range(y,y+35):
                frame[i,j] = [0,0,0]

    def displayBound(self,frame,x1,x2):
        for i in range(x1,x2):
            frame[i,415] = [0,0,0]


    def writeData(self,fileOut,frame,x,y,label):
        for i in range(x,x+25):
            for j in range(y,y+35):
                #pixel = fram
                fileOut.write(str(frame[i,j][0]))
                fileOut.write(" ")
                fileOut.write(str(frame[i,j][1]))
                fileOut.write(" ")
                fileOut.write(str(frame[i,j][2]))
                fileOut.write(" ")

        fileOut.write(label)
        fileOut.write('\n')

    def frameToData(self,vidFile,count):
        vid = cv2.VideoCapture(vidFile)
        vid.set(1,count)
        fileOut = open("vidData.txt",'w+')
        if(count % 500 == 0):
            print count
        ret, frame = vid.read()
        self.writeData(fileOut,frame,435,415,"Null")

    def getBestOffSet(self,frame):
        killCol = KillCollector.KillCollector("killClass35.txt")
        bestX = 0
        bestSum = 0
        for i in range(385,410):
            pixArr = killCol.extractData(frame,i,415,25,35)
            sum = killCol.checkKill(pixArr)
            if(sum >= bestSum):
                # print "new ",bestX," with sum of ",bestSum
                bestSum = sum
                bestX = i

        print bestX," with sum of ",bestSum

    def run(self):
        vidFile = "C:\Users\psalmas\Videos\COD_WWII\My Great Game - WWII_May2018_2.23 - 2018-06-15 18-48-47.mp4"
        vid = cv2.VideoCapture(vidFile)
        vid.set(1,2000)
        fileOut = open("dataCollect1.txt",'w')
        kCount = 0
        nCount = 0

        tester = KillCollector.KillCollector("killClass35.txt")   #TEMP
        while True:
            ret, frame = vid.read()

            cin = raw_input()

            # print vid.get(1)
            # pixArr = tester.extractData(frame,415,415,25,35)  #TEMP
            # tester.checkKill(pixArr)
            self.getBestOffSet(frame)

            if kCount == 7 and nCount == 3: return
            if cin == "k" and kCount != 7:
                self.writeData(fileOut,frame,435,415,"1")
                vid.read()
                kCount += 1
                print "kCount: ",kCount
            elif cin == "n" and nCount != 3:
                self.writeData(fileOut,frame,435,415,"-1")
                vid.read()
                nCount += 1
                print "nCount: ",nCount
            elif cin == "d":
                # self.displayBox(frame,435,415)
                self.displayBound(frame,390,410)
                vid.read()
            elif cin == "s":
                vid.set(1,vid.get(1)+150)
            elif cin == "ss":
                vid.set(1,vid.get(1)+1000)

            if vid.get(1) % 100 == 0: print(vid.get(1))

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
