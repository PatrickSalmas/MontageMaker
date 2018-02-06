import cv2

import BoardClass
import FrameClass

# First version of getClips (only gets clips of triple kills
# and above for now)
def getKillsPos(inVideo):
    #inVideo = cv2.VideoCapture(videoPath)
    #inVideo.set(1,20400)
    killBoard = BoardClass.Board()
    killListPos = []   #frame position of each kill

    kCount = 0     # counts kills

    horizOffSet = 11

    offSet = 21
    animTime = 33  # number of frames kill/points are in single
                   # position


    while True:
        ret, frameIn = inVideo.read()
        #if inVideo.get(1) == 9000: break
        if not ret:
            print("Finished input video!")
            break

        frame = FrameClass.Frame(frameIn)
        #frame.displayMap(frameIn,"white25Map.txt",0,horizOffSet)
       # frame.displayMap(frameIn,"grey25Map.txt",0,horizOffSet)
        #frame.displayMap(frameIn,"whiteKillMap.txt",0,horizOffSet)
        #frame.displayMap(frameIn,"greyKillMap.txt",0,horizOffSet)

        timer = killBoard.getClearTime()
        if timer > 0:
            killBoard.ticClearTime()
            #print killBoard.getClearTime()

        if timer == 0:
            if frame.checkKillLocs(0):
                killBoard.setClearTime(1)  #set for 1 kill
                if not frame.check25Points(inVideo,inVideo.get(1),0):
                    killListPos.append(inVideo.get(1))
                    kCount+=1
                    print("Kill at frame " + str(inVideo.get(1)))
        if timer > 0 and timer <= (1*animTime):
            if frame.checkKillLocs(1):
                killBoard.setClearTime(2)
                if not frame.check25Points(inVideo,inVideo.get(1),1):
                    killListPos.append(inVideo.get(1))
                    kCount+=1
                    print("Kill at frame " + str(inVideo.get(1)))
        if timer > 0 and timer <= (2*animTime):
            if frame.checkKillLocs(2):
                killBoard.setClearTime(3)
                if not frame.check25Points(inVideo,inVideo.get(1),2):
                    killListPos.append(inVideo.get(1))
                    kCount+=1
                    print("Kill at frame " + str(inVideo.get(1)))
        if timer > 0 and timer <= (3*animTime):
            if frame.checkKillLocs(3):
                killBoard.setClearTime(4)
                if not frame.check25Points(inVideo,inVideo.get(1),3):
                    killListPos.append(inVideo.get(1))
                    kCount+=1
                    print("Kill at frame " + str(inVideo.get(1)))
        if timer > 0 and timer <= (4*animTime):
            if frame.checkKillLocs(4):
                killBoard.setClearTime(5)
                if not frame.check25Points(inVideo,inVideo.get(1),4):
                    killListPos.append(inVideo.get(1))
                    kCount+=1
                    print("Kill at frame " + str(inVideo.get(1)))

        #cv2.imshow('frame',frameIn)
        #if cv2.waitKey(0) & 0xFF == ord('q'):
            #break

        if inVideo.get(1) % 500 == 0: print(inVideo.get(1))

    return killListPos


def createVideo(killListPos,inVideo,outVideo):
    print "Creating Video"
    bufferPre = 40
    bufferPost = 15    # buffer time, before and after clips
    killTally = 0
    for i in range(0,len(killListPos)-1):
        if killListPos[i+1] - killListPos[i] <= 225:
            if killTally == 0: killTally = 2
            else: killTally += 1
            print killTally
        elif killTally >= 3:
            start = int(killListPos[i-killTally+1] - bufferPre)
            end = int(killListPos[i] + bufferPost)
            print "found clip from " + str(start) + " to " + str(end)
            recordClip(inVideo,outVideo,start,end)
            killTally = 0
        else:
            killTally = 0

    if killTally >= 3:
        i = len(killListPos)-1
        start = int(killListPos[i-killTally+1] - bufferPre)
        end = int(killListPos[i] + bufferPost)
        print "found clip from " + str(start) + " to " + str(end)
        recordClip(inVideo,outVideo,start,end)



def recordClip(inVideo,outVideo,start,end):
    inVideo.set(1,start)
    for i in range(start,end):
        ret, frameIn = inVideo.read()
        if not ret: break
        outVideo.write(frameIn)


def main():
    # list of local file for testing montage creation
    videoList = ["C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1 - 2017-09-02 13-35-40.mp4"]
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.1 - 2017-09-02 14-31-07.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.2 - 2017-09-02 14-52-58.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.3 - 2017-09-02 15-29-46.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.4 - 2017-09-02 10-39-41.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.5 - 2017-09-02 10-53-57.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.6 - 2017-09-02 11-08-06.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.7 - 2017-09-02 12-06-15.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.8 - 2017-09-02 12-45-53.mp4",
                 #"C:\Users\psalmas\Videos\COD_WWII\My Great Game - WW_1.9 - 2017-09-02 13-42-34.mp4"]
    firstVid = cv2.VideoCapture(videoList[0])   #basing specs of outVid on firstVid in list
    fourcc = int(firstVid.get(6))
    fps = int(firstVid.get(5))
    width = int(firstVid.get(3))
    height = int(firstVid.get(4))
    outVideo = cv2.VideoWriter("montageTest.mp4",fourcc,fps,(width,height))

    for i in range(0,len(videoList)):
        print "STARTING VIDEO: " + str(i)
        inVideo = cv2.VideoCapture(videoList[i])
        killListPos = getKillsPos(inVideo)
        createVideo(killListPos,inVideo,outVideo)
        inVideo.release()

    outVideo.release()
if __name__ == "__main__":
    main()
