import FileAccessClass
import CaptureData
import ClassWriter
import Boost
import MakeMontage
import KillCollector

def main():
    # capture = CaptureData.CaptureData()
    # capture.vidToData("C:\Users\psalmas\Videos\COD_WWII\My Great Game - WWII_May2018_2.26 - 2018-06-15 19-50-06.mp4")

    # file = open("testData.txt")
    # fileOut = open("trainPure3.txt",'w')
    # numLines = sum(1 for line in open("testData.txt"))
    # print numLines
    # for i in range(0,numLines):
    #     strLine = file.readline()
    #     #strLine.strip('\n')
    #     feats = strLine.split(' ')
    #     label = feats[len(feats)-1]
    #     label.rstrip()
    #     print label
    #     if(label == "1\n"):
    #         fileOut.write(strLine)
    #         #fileOut.write('\n')

    #fA = FileAccessClass.FileAccess("dummy.txt")
    #numLines = len(fA.getData())
    #for i in range(0,numLines):
     #   print fA.getData()[i].getLabel()
    # capture = CaptureData.CaptureData()
    # capture.run()
    #boost = Boost.Boost("trainData.txt")
    # boost = Boost.Boost("trainPure2.txt")
    # boost = Boost.Boost("train2.txt",True)
    # print "using thresh of ", boost.thresh
    # for i in range(0,50):
    #      print "ROUND ",i
    #      boost.run()
    #      print("train2:",'\t',"testData:",'\t',"trainData2:")
    #      print(boost.calcError("train2.txt"),'\t',boost.calcError("testData.txt"),'\t',boost.calcError("trainData2.txt"))
    #      if i == 40 or i == 50 or i == 60 or i == 75 or i == 90 or i == 100:
    #          writeClass = ClassWriter.ClassWriter(boost.C,boost.Alph)
    #          writeClass.write(str(i))


    # #boost.run2()
    # #boost.calcError("trainData.txt")
    # #boost.calcError("testData.txt")
    # #boost.calcError("testData2.txt")
    #
    # print len(boost.C)

    # writeClass = ClassWriter.ClassWriter(boost.C,boost.Alph)
    # writeClass.write()

    # testTage = MakeMontage.MakeMontage("killClass2.txt")
    # testTage.getKillPos("C:\Users\psalmas\Videos\COD_WWII\My Great Game - WWII_May2018_2.21 - 2018-06-15 17-18-03.mp4")

    # killTest = KillCollector.KillCollector("killClass35.txt")    #load the pretrained classifier (from boosting)
    # killTest.getKillPos("C:\Users\psalmas\Videos\COD_WWII\My Great Game - WWII_May2018_2.21 - 2018-06-15 17-18-03.mp4")
    # killTest.stepKills("35")

    videoList = ["C:\Users\psalmas\Videos\COD_WWII\My Great Game - WWII_May2018_2.21 - 2018-06-15 17-18-03.mp4"]
    montageTest = MakeMontage.MakeMontage("killClass35.txt",videoList)
    montageTest.run()


if __name__ == "__main__":
        main()
        #print "test"
