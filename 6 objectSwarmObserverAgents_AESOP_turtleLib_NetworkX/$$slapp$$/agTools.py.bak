import commonVar as common

class SuperAgent(object):

    # add an operating set
    def setAnOperatingSet(self,aSet):
        self.agOperatingSets.append(aSet)

    # create the list of all the sets (with the original one too)
    # in which we can find the agent
    def setContainers(self):
        self.containers=self.getOperatingSetList()+[self.getAgentType(),\
                                                    "all"]
    # set the agentList here
    def setAgentList(self,agentList):
        self.agentList=agentList

    # get operating set list
    def getOperatingSetList(self):
        return self.agOperatingSets

    # get last executed method
    def getLastExecutedMethod(self):
        return self.lastExecutedMethod

    # reset values
    def setNewCycleValues(self):
        pass # here is only reported for future uses
             # or to be redefined in Agent.py of a specific project

    # get operating agent type
    def getAgentType(self):
        return self.agType

    #OBSOLETE methods

    # methods for Tk graphic applications
    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setGraphicItem(self, grI):
        self.graphicItem=grI

    def getGraphicItem(self):
        return self.graphicItem

    def getAgentType(self):
        return self.agType
