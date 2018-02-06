from __future__ import division
import cv2

#Draws a box around given area  (FOR VISUALIZATION)
def boxArea(frame,x1,x2,y1,y2):
    for x in range(x1,x2):
        frame[x,y1] = [0,0,0]
        frame[x,y2] = [0,0,0]
    for y in range(y1,y2):
        frame[x1,y] = [0,0,0]
        frame[x2,y] = [0,0,0]

# Determines if given pixel is a shade of white
def isWhite(pix):
    if pix[0] > 155 and pix[1] > 155 and pix[2] > 155:
        return True
    return False

# Determines if given pixel is a shade of gray
def isGrey(pixel):
    if pixel[0] > 55 and pixel[0] < 180:
        if pixel[1] > 55 and pixel[1] < 180:
            if pixel[2] > 55 and pixel[2] < 180:
                return True
    return False

# Extracts the white pixels from an area given by x,x2,y, and y2
def extractWhiteCoors(frame,fileOut,x1,x2,y1,y2):
    for x in range(x1,x2):
        for y in range(y1,y2):
            if isWhite(frame[x,y]):
                fileOut.write(str(x) + " " + str(y)+"\n")
                #frame[x,y] = [0,0,0]

    fileOut.write("\n")


# Extracts the grey pixels (edging) from "Kill"
def extractGreyCoors(frame,fileOut,x1,x2,y1,y2):
    for x in range(x1,x2):
        for y in range(y1,y2):
            if isGrey(frame[x,y]):
                fileOut.write(str(x) + " " + str(y)+"\n")
                #frame[x,y] = [0,0,0]


    fileOut.write("\n")



    # Creates a pixel map for based on the input file using
# a specified threshold percentage
def writeMap(fileIn,fileOut,thresh):
    numLines = sum(1 for line in open(fileIn))
    numTakes = sum(1 for line in open(fileIn) if line.rstrip())
    numTakes = numLines - numTakes

    print(str(numLines) + " number of lines")
    print(str(numLines-numTakes) + " number of takes")
    fi = open(fileIn,"r+")

    fileOut = open(fileOut,'w')

    hashMap = {}
    for i in range(0,numLines):
        if i % 20 == 0: print(i)
        lineI = fi.readline()
        if lineI in hashMap: continue
        matches = 0
        fi2 = open(fileIn,"r+")
        for j in range (0,numLines):
            lineJ = fi2.readline()
            if lineI == lineJ:
                matches+=1

        matchRate = matches/numTakes
        if matchRate > thresh:
            fileOut.write(str(lineI))
            print(matchRate)

        hashMap.update({lineI: "checked"})

def displayMap(frame,fileIn,offset,offSetHoriz):
    numLines = sum(1 for line in open(fileIn))
    fi = open(fileIn,"r+")
    for i in range(0,numLines-1):
        strLine = fi.readline()
        if strLine == "\n": continue
        coors = strLine.split(' ')
        x = int(coors[0]) - offset
        y = int(coors[1].rstrip()) + offSetHoriz
        #x = coors[0]
        #y = coors[1].rstrip()
        #print(str(x)+ " " + str(y))

        frame[x,y] = [0,0,0]

def main():
    # write maps for +25
    #writeMap('grey25Hits.txt','grey25Map.txt',.70)
    #writeMap('white25Hits.txt','white25Map.txt',.75)

    #Produced even better results (maybe do even better)!
    #writeMap('greyKillHits.txt','greyKillMap.txt',.70)
    #writeMap('whiteKillHits.txt','whiteKillMap.txt',.75)

    #Produced good results, going to test w/ thresh vals above
    #writeMap('greyKillHits.txt','greyKillMap.txt',.75)
    #writeMap('whiteKillHits.txt','whiteKillMap.txt',.80)

    #return

    video = cv2.VideoCapture("shotty1.4.mp4")
    #print video.get(5)
    video.set(1,2600)

    whiteKillHits = open('whiteKillHits.txt','a')
    greyKillHits = open('greyKillHits.txt','a')

    whiteGlideKillHits = open('whiteGlideKillHits.txt','a')
    greyGlideKillHits = open('greyGlideKillHits.txt','a')

    whiteHPKillHits = open('whiteHPKillHits.txt','a')
    greyHPKillHits = open('greyHPKillHits.txt','a')

    white25Hits = open('white25Hits.txt','a');
    grey25Hits = open('grey25Hits.txt','a');

    while True:
        ret, frame = video.read()
        if not ret: break

        #boxArea(frame,438,455,437,466)   #kill area
        #boxArea(frame,438,455,405,434)
        #boxArea(frame,438,456,462,504)   #points area (kill confirmed)
        #boxArea(frame,438,456,475,515)    #point area (general)


        #displayMap(frame,"white25Map.txt",0,19)  #maps looks good
        #displayMap(frame,"grey25Map.txt",0,19)   #could do better if needed

        #displayMap(frame,"whiteKillMap.txt",0,0)
        #displayMap(frame,"greyKillMap.txt",0,0)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cin = raw_input()

        if cin == "k":
            for i in range(0,24):
                extractWhiteCoors(frame,whiteKillHits,438,455,437,466)
                extractGreyCoors(frame,greyKillHits,438,455,437,466)
                video.read()
        elif cin == "kb":
            for i in range(0,24):
                extractWhiteCoors(frame,whiteKillHits,438,455,437,466)
                extractGreyCoors(frame,greyKillHits,438,455,437,466)
                extractWhiteCoors(frame,whiteGlideKillHits,438,455,405,434)
                extractGreyCoors(frame,greyGlideKillHits,438,455,405,434)
                video.read()
        elif cin == "kh":
            for i in range(0,24):
                extractWhiteCoors(frame,whiteKillHits,438,455,437,466)
                extractGreyCoors(frame,greyKillHits,438,455,437,466)
                extractWhiteCoors(frame,whiteHPKillHits,438,455,405,434)
                extractGreyCoors(frame,greyHPKillHits,438,455,405,434)
                video.read()
        elif cin == "25":
            for i in range(0,24):
                extractWhiteCoors(frame,white25Hits,438,456,475,515)
                extractGreyCoors(frame,grey25Hits,438,456,475,515)
                video.read()



        if video.get(1) % 100 == 0: print(video.get(1))

if __name__ == "__main__":
    main()
