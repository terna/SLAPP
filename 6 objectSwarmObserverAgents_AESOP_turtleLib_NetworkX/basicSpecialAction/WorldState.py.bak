#WorldState.py
from Tools import *

class WorldState(object):
    def __init__(self):
        # the environment
        self.generalMovingProb=1
        print "World state has been created."

    # ",**d" in the parameter lists of the methods is a place holder
    # in case we use, calling the method, a dictionary as last parameter

    # set generalMovingProb
    def setGeneralMovingProb(self,**d):
        if d.has_key("setGeneralMovingProb"):
            self.generalMovingProb=d["setGeneralMovingProb"]
            print "general moving probability now set to",\
                  self.generalMovingProb, "in world state"
        else:
            print "*********** key 'generalMovingProb' is not defined"
            self.generalMovingProb=1

    # get generalMovingProb
    def getGeneralMovingProb(self):
        return self.generalMovingProb
