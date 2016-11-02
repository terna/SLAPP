#NewAgent.py
from Tools import *
from agTools import *
from Agent import *

class OtherAgent(Agent):
    def __init__(self, number,myWorldState,
                 xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=""):

        Agent.__init__(self, number,myWorldState,
                     xPos, yPos, lX =-20,rX=19, bY=-20,tY=19, agType=agType)
        # it is anyway possible to initilize the environment directly,
        # commenting the call above to the super class and uncommenting
        # the rows below


        """
        # the environment
        self.agOperatingSets=[]
        self.number = number
        self.lX = lX
        self.rX = rX
        self.bY = bY
        self.tY = tY
        if myWorldState != 0:
           self.myWorldState = myWorldState
        self.agType=agType
        # the agent
        self.xPos = xPos
        self.yPos = yPos
        print "agent", self.agType, "#", self.number, \
     	      "has been created at", self.xPos, ",", self.yPos

        # it is possible to avoid the assignment above sending init
        # order to the superclass
        """


    # sleeping
    def sleep(self,**d):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "happy to sleep!"

    # movement
    def randomMovement(self,**k):
        print "I'm %s agent # %d: " % (self.agType,self.number),
        print "absolutely not moving!!!"
