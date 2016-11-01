#Bug.py
import random

class Bug:
    def __init__(self, number, xPos, yPos, worldXSize = 80, worldYSize = 80):
        # the environment
        self.number = number
        self.worldXSize = worldXSize
        self.worldYSize = worldYSize
        # the bug
        self.xPos = xPos
        self.yPos = yPos
        print "Bug number ", self.number, \
     	      " has been created at ", self.xPos, ", ", self.yPos

    # the action
    def randomWalk(self):
        self.xPos += randomMove()
        self.yPos += randomMove()
        self.xPos = (self.xPos + self.worldXSize) % self.worldXSize
        self.yPos = (self.yPos + self.worldYSize) % self.worldYSize
    # report
    def reportPosition(self):
        print "Bug number ", self.number, " moved to X = ", \
               self.xPos, " Y = ", self.yPos

    # methods for Tk graphic applications
    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setGraphicItem(self, grI):
        self.graphicItem=grI

    def getGraphicItem(self):
        return self.graphicItem

# returns -1, 0, 1  with equal probability
def randomMove():
    return random.randint(-1, 1)
