import cv2

import BoardClass
import Boost
import CaptureData


class KillCollector():
    killClass = 0
    frameList = 0
    killList = 0

    vertOffSet = 0

    def __init__(self,fileName):
        self.killClass = Boost.Boost(fileName,False)   #load pre-trained, boosted kill classifier
        self.frameList = []
        self.killList = []

    def extractData(self,frame,x,y,xOff,yOff):
        retArr = []
        for i in range(x,x+xOff):
            for j in range(y,y+yOff):
                retArr.append(float(frame[i,j][0]))
                retArr.append(float(frame[i,j][1]))
                retArr.append(float(frame[i,j][2]))

        return retArr


    def checkKill(self,pixArr):
        sum = 0
        rangeCheck = self.killClass.C[0].stepCount
        for t in range(0,len(self.killClass.C)):
            r = pixArr[self.killClass.C[t].feat]
            g = pixArr[self.killClass.C[t].feat+1]
            b = pixArr[self.killClass.C[t].feat+2]
            hx = 0
            if(abs(self.killClass.C[t].R - int(r)) <= rangeCheck and abs(self.killClass.C[t].G - int(g)) <= rangeCheck and abs(self.killClass.C[t].B - int(b) <= rangeCheck)):
                hx = 1
            else:
                hx = -1
            val = float(self.killClass.Alph[t])*hx
            sum += val

        # print sum
        if(sum > 0): return True
        else: return False
        # return sum        #TEEEMMMMPPP


    def getKillPos(self,videoPath):
        self.killList = []
        inVideo = cv2.VideoCapture(videoPath)
        inVideo.set(1,0)

        killBoard = BoardClass.Board()
        kCount = 0

        while True:
            if int(inVideo.get(1)) % 50 == 0:
                print "finished frame ",inVideo.get(1)

            ret, frameIn = inVideo.read()

            # if inVideo.get(1) >= 18000:
            #     return

            if not ret:
                print("Finished input video")
                return

            # cin = raw_input()

            timer = killBoard.getClearTime()
            if timer > 0:
                killBoard.ticClearTime()
            if timer == 0:
                pixArr = self.extractData(frameIn,435,415,25,35)
                # pixArr = self.extractData(frameIn,415,415,25,35)
                if self.checkKill(pixArr):
                    print '\t',"Kill at frame ",inVideo.get(1)
                    self.frameList.append(frameIn)
                    self.killList.append(inVideo.get(1))
                    killBoard.setClearTime(1)
            else:
                if timer <= killBoard.killTime*1:
                    pixArr = self.extractData(frameIn,413,415,25,35)
                    if self.checkKill(pixArr):
                        print '\t',"Kill at frame ",inVideo.get(1)," in 2nd row!"
                        self.frameList.append(frameIn)           #MAY WANT TO REMOVE THIS
                        self.killList.append(inVideo.get(1))
                        killBoard.setClearTime(2)
                if timer <= killBoard.killTime*2:
                    pixArr = self.extractData(frameIn,392,415,25,35)
                    if self.checkKill(pixArr):
                        print '\t',"Kill at frame ",inVideo.get(1)," in 3nd row!"
                        self.frameList.append(frameIn)
                        self.killList.append(inVideo.get(1))
                        killBoard.setClearTime(3)

            killBoard.ticClearTime()




            # inVideo.set(1,inVideo.get(1)+4)


    def stepKills(self,type):
        fileName = "correctiveData" + type + ".txt"
        fileOut = open(fileName,"a+")
        cap = CaptureData.CaptureData()
        for i in range(0,len(self.frameList)):
            frame = self.frameList[i]

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            cin = raw_input()
            if cin == "n":
                cap.writeData(fileOut,frame,435,415,"-1")
                cv2.destroyAllWindows()
                continue








