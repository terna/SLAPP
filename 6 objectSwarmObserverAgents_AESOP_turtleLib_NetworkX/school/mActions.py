from Tools import *
from Agent import *
import os

def do0(address):
            self=address # if necessary
            askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)
            askEachAgentInCollection(address.agentList, Agent.clear)

def do1(address):
            self=address # if necessary

            # keep safe the original list
            address.agentListCopy=address.agentList[:]
            # clear messages
            askEachAgentInCollection(address.agentListCopy, Agent.clear)
            # never in the same order (please comment if you want to keep
            # always the same sequence
            random.shuffle(address.agentListCopy)

def createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType):
                #explicitly pass self, here we use a function
                if len(line.split())==5 and line.split()[1] != 'brown':
                 anAgent = Agent(num, self.worldState,
                          int(line.split()[2]),
                          int(line.split()[3]),
                          leftX,rightX,bottomY,topY,agType=agType)
                 self.agentList.append(anAgent)
                 anAgent.setColorAndGender(line.split()[1],line.split()[4])

                elif len(line.split())==4 and line.split()[1] == 'brown':
                 anAgent = Agent(num, self.worldState,
                          int(line.split()[2]),
                          int(line.split()[3]),
                          leftX,rightX,bottomY,topY,agType=agType)
                 #not added to agentList
                 anAgent.setColorAndGender(line.split()[1],"") #brown, no gender,
                                                               # it is a desk
                else:
                 print "Error in file "+agType+".txt"
                 os.sys.exit(1)

def otherSubSteps(subStep, address):
            return False
