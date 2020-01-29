import cv2

import BoardClass
import Boost
import FileAccessClass
import KillCollector

class MakeMontage():
    # killClass = 0
    killCol = 0
    videoList = 0
    maxKillDiff = 225

    def __init__(self,fileName,videoList):
        # self.killClass = Boost.Boost(fileName,False)
        self.killCol = KillCollector.KillCollector(fileName)
        self.videoList = videoList

    def appendVideo(self,killList,inVideo,outVideo):
        print "Appending video"
        bufferPre = 100
        bufferPost = 50
        killTally = 0
        for i in range(0,len(killList)-1):
            print killList[i]
            if killList[i+1] - killList[i] <= self.maxKillDiff:
                if killTally == 0: killTally = 2
                else: killTally += 1
                print killTally
            elif killTally >= 3:
                start = int(killList[i-killTally] - bufferPre)
                end = int(killList[i] + bufferPost)
                print "found clip from ",str(start)," to ",str(end)
                self.recordClip(inVideo,outVideo,start,end)
                killTally = 0
            else:
                killTally = 0

        if killTally >= 3:
            i = len(killList)
            start = int(killList[i-killTally] - bufferPre)
            end = int(killList[i] + bufferPost)
            print "found clip from ",str(start)," to ",str(end)
            self.recordClip(inVideo,outVideo,start,end)

    def recordClip(self,inVideo,outVideo,start,end):
        inVideo.set(1,start)
        for i in range(start,end):
            ret, frameIn = inVideo.read()
            if not ret: break
            outVideo.write(frameIn)


    def run(self):
        firstVid = cv2.VideoCapture(self.videoList[0])
        fourcc = int(firstVid.get(6))
        fps = int(firstVid.get(5))
        width = int(firstVid.get(3))
        height = int(firstVid.get(4))
        outVideo = cv2.VideoWriter("montageTest2.0.mp4",fourcc,fps,(width,height))


        for i in range(0,len(self.videoList)):
            inVideo = cv2.VideoCapture(self.videoList[i])
            self.killCol.getKillPos(self.videoList[i])
            killArr = self.killCol.killList
            self.appendVideo(killArr,inVideo,outVideo)
            inVideo.release()

        outVideo.release()
