class Data():
    feats = []
    label = ""

    def __init__(self,feats,label):
        self.feats = feats
        self.label = label


    def getFeats(self):
        return self.feats

    def getFeat(self,feat):
        return self.feats[feat]

    def getLabel(self):
        return self.label
