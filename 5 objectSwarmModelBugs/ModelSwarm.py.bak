#ModelSwarm.py
from Tools import *
from Bug import *
from ActionGroup import *



class ModelSwarm:
    def __init__(self, nBugs, nCycles, worldXSize = 80, worldYSize = 80):
        # the environment
        self.nBugs = nBugs
        self.bugList = []

        self.nCycles = nCycles
        self.worldXSize= worldXSize
        self.worldYSize= worldYSize
        self.conclude=False
        self.t=-1 # time will start with a 0 value in the first step

    # objects
    def buildObjects(self):
        for i in range(self.nBugs):
            aBug = Bug(i, random.randint(0,self.worldXSize-1), 
                    random.randint(0,self.worldYSize-1), self.worldXSize,
                    self.worldYSize)
            self.bugList.append(aBug)
        print

    # actions
    def buildActions(self):

        self.actionGroup1 = ActionGroup ("move")
        def do1(address, nCycles, actionList):

            # keep safe the original list
            address.bugListCopy=address.bugList[:]
            # never in the same order (please comment if you want to keep
            # always the same sequence
            random.shuffle(address.bugListCopy)
            # move with a jump, to have to transfer a parameter
            # the format is: collection, method, parameters by name

            # ask each agent, without parameters
            # askEachAgentIn(address.bugListCopy,Bug.randomWalk)

            # ask indivually each agent, with a parameter
            for anAgent in address.bugListCopy:
                    askAgent(anAgent,Bug.randomWalk,
                                        jump=random.uniform(0,5))

            self.t+=1 #the clock running
            if self.t+1==nCycles:
                 insertASubStepElementInNextStep_firstPosition(actionList,"end")

        self.actionGroup1.do = do1 # do is a variable linking a method
    
        self.actionGroup2a = ActionGroup ("talk all")
        def do2a(address):
            
            # ask each agent, without parameters

            print "Time = ", self.t, "ask all agents to report position"
            askEachAgentIn(address.bugList,Bug.reportPosition)
                     
        self.actionGroup2a.do = do2a # do is a variable linking a method
    
        self.actionGroup2b = ActionGroup ("talk one")
        def do2b(address):
            # ask a single agent, without parameters
            print "Time = ",self.t,"ask first agent to report position"
            askAgent(address.bugList[0],Bug.reportPosition)
                     
        self.actionGroup2b.do = do2b # do is a variable linking a method

        self.actionGroup3 = ActionGroup ("end")
        def do3(address):
            self.conclude=True
        self.actionGroup3.do = do3 # do is a variable linking a method

        # schedule
        self.actionList = [["move"], ["talk all"], \
                           ["move"], ["talk one"], \
                           ["move"], ["talk one"]]


    # run
    def run(self):

        while not self.conclude:
            step=extractAStepAndRotate(self.actionList)

            while len(step)>0:
                subStep=extractASubStep(step)


                if subStep == "move":
                    self.actionGroup1.do(self, self.nCycles, self.actionList)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable
 
                if subStep == "talk all":
                    self.actionGroup2a.do(self)

                if subStep == "talk one":
                    self.actionGroup2b.do(self)

                if subStep == "end":
                    self.actionGroup3.do(self)
