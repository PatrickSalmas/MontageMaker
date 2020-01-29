from __future__ import division
import cv2

class Frame():
    def __init__(self,frame):
        self.frame = frame


    # Wider range of white accepted
    def isWhiteLooser(self,pix):
        if pix[0] > 155 and pix[1] > 155 and pix[2] > 155:
            return True
        return False

    # Wider range of grey accepted
    def isGreyLooser(self,pixel):              # lower bound is usually 70
        if pixel[0] > 70 and pixel[0] < 160:   # testing with 65
            if pixel[1] > 70 and pixel[1] < 160:
                if pixel[2] > 70 and pixel[2] < 160:
                    return True
        return False



    # Checks the appropriate pixel map for the specified color.
    # If more than 95% of pixels are of specified color, return true
    # else return false
    def percentageColor(self,frame,color,fileName,offset,offSetHoriz):
        numLines = sum(1 for line in open(fileName))
        file = open(fileName,"r")
        hits = 0
        totalPix = 0
        for i in range(0,numLines-1):
            strLine = file.readline()
            if strLine == "\n": continue
            coors = strLine.split(' ')
            x = int(coors[0]) - offset
            y = int(coors[1].rstrip()) - offSetHoriz
            if color == "white":
                #if isWhite(frame[x,y]): hits+=1
                if self.isWhiteLooser(frame[x,y]): hits+=1
            if color == "grey":
                #if isGrey(frame[x,y]): hits+=1
                if self.isGreyLooser(frame[x,y]): hits+=1
            totalPix+=1
        #if offSetHoriz > 0:
            #print (str(float(hits/totalPix)) + " of " + str(color))
        return float(hits/totalPix)


    # if at least 90% of pixels from whitePix are white,
    # return true, otherwise return false
    def isKill(self,offset,offSetHoriz):
        fileWhite = "whiteKillMap.txt"
        fileGrey = "greyKillMap.txt"

        #print
        if self.percentageColor(self.frame,"white",fileWhite,offset,offSetHoriz) >= .75: #previously .80
            if self.percentageColor(self.frame,"grey",fileGrey,offset,offSetHoriz) >= .45: #previously .50
                return True
        else: return False


    #Checks kill location spots by specified row
    def checkKillLocs(self,row):
        vertOffSet = 21
        vertPos = (vertOffSet*row)
        if self.isKill(vertPos,0) or self.isKill(vertPos,19):
            return True

    def is25Points(self,frameIn,offset,offSetHoriz):
        fileWhite25 = "white25Map.txt"
        fileGrey25 = "grey25Map.txt"

        if self.percentageColor(frameIn,"white",fileWhite25,offset,offSetHoriz) >= .80:
            if self.percentageColor(frameIn,"grey",fileGrey25,offset,offSetHoriz) >= .60:
                return True
        else: return False

    # checks to see if addressed kill has value of +25 (checks next 15 frames)
    # if found to have +25, return true
    def check25Points(self,inVideo,frameNum,row):
        vertOffSet = 21
        vertPos = (vertOffSet*row)
        inVideo.set(1,frameNum)
        for i in range(0,15):
            ret, frameIn = inVideo.read()
            if not ret: break
            #print inVideo.get(1)
            if self.is25Points(frameIn,vertPos,0) or self.is25Points(frameIn,vertPos,11):
                #print "PASSING"
                inVideo.set(1,frameNum)
                return True

        inVideo.set(1,frameNum)
        return False


    def drawBox(self):
        for x in range(435,460):
            self.frame[x,415] = [0,0,0]
            self.frame[x,450] = [0,0,0]
        for y in range(415,450):
            self.frame[435,y] = [0,0,0]
            self.frame[460,y] = [0,0,0]


    def displayMap(self,frame,fileIn,offset,offSetHoriz):
        numLines = sum(1 for line in open(fileIn))
        fi = open(fileIn,"r+")
        for i in range(0,numLines-1):
            strLine = fi.readline()
            if strLine == "\n": continue
            coors = strLine.split(' ')
            x = int(coors[0]) - offset
            y = int(coors[1].rstrip()) - offSetHoriz

            frame[x,y] = [0,0,0]
