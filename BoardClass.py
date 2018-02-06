class Board():
    timeToClear = 0   # Based on the most recent kill,
                      # how long it will take the board to
                      # clear

    def setClearTime(self,num):
        self.timeToClear = 0 + (num * 36)

    def getClearTime(self):
        return self.timeToClear

    def ticClearTime(self):
        self.timeToClear -= 1


