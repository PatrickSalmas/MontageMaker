class Board():
    timeToClear = 0   # Based on the most recent kill,
                      # how long it will take the board to
                      # clear
    killTime = 36

    def setClearTime(self,num):
        self.timeToClear = 0 + (num * self.killTime)

    def getClearTime(self):
        return self.timeToClear

    def ticClearTime(self):
        if self.timeToClear > 0:
            self.timeToClear -= 1


