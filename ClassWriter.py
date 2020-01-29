

class ClassWriter():

    C = []
    Alph = []

    def __init__(self,C,Alph):
        self.C = C
        self.Alph = Alph


    def write(self,type):
        fileName = "killClass"+type+".txt"
        # fileOut = open("killClass50.txt",'w+')   #writing to file named "killClass2.txt" for ver. 3.0  (killClass.txt for ver. 2.0)
        fileOut = open(fileName,"w+")
        for i in range(0,len(self.C)):
            fileOut.write(str(self.C[i].R))
            fileOut.write(" ")
            fileOut.write(str(self.C[i].G))
            fileOut.write(" ")
            fileOut.write(str(self.C[i].B))
            fileOut.write(" ")
            fileOut.write(str(self.C[i].feat))
            fileOut.write(" ")
            fileOut.write(str(self.Alph[i]))
            fileOut.write('\n')
