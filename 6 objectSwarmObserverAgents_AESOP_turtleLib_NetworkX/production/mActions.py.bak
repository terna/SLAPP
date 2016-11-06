from Tools import *
from Agent import *
import os
import random
import commonVar as common

def do0(address):
            self=address # if necessary
            askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)

def do1(address):
            self=address # if necessary

            # keep safe the original list
            address.agentListCopy=address.agentList[:]
            # never in the same order (please comment if you want to keep
            # always the same sequence
            random.shuffle(address.agentListCopy)

def createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType):
                #explicitly pass self, here we use a function

                # recipes
                if len(line.split())==1:
                 anAgent = Agent(num, self.worldState, agType=agType)
                 self.agentList.append(anAgent)
                 anAgent.setAgentList(self.agentList)

                # factories
                elif len(line.split())==4:
                 anAgent = Agent(num, self.worldState,
                                 int(line.split()[1]),
                                 int(line.split()[2]),    agType=agType,
                                 sector=int(line.split()[3]))

                 self.agentList.append(anAgent)
                 anAgent.setAgentList(self.agentList)

                else:
                 print "Error in file "+agType+".txt"
                 os.sys.exit(1)

def addAFactory(address):

    if random.random() < 0.5:
        # with a given probability, create a new factory cloning
        # an existing one, randomly chosen (can also be a clone)

        factoryTmpList=[]
        # agentList contains also recipes
        for i in range(len(address.agentList)):
            if address.agentList[i].agType == 'factories':
                 factoryTmpList.append(address.agentList[i])
        #print factoryTmpList
        random.shuffle(factoryTmpList)
        toBeCloned=factoryTmpList[0]
        #print toBeCloned.number

        # cloning (the agent constructor interacts with the graph)

        common.clonedN+=1
        anAgent = Agent(toBeCloned.number*100+common.clonedN,
                        address.worldState,
                        toBeCloned.xPos+modPosition(),
                        toBeCloned.yPos+modPosition(),
                        agType=toBeCloned.agType,
                        sector=toBeCloned.sector)
        address.agentList.append(anAgent)
        anAgent.setAgentList(address.agentList)
        if common.verbose: print "Created factory #",anAgent.number,\
                                 "in sector",anAgent.sector

def removeAFactory(address):

    if random.random() < 0.2: # with a given probability, removesone of the factories
        factoryTmpList=[]

        # agentList contains also recipes
        for i in range(len(address.agentList)):
            if address.agentList[i].agType == 'factories':
                 factoryTmpList.append(address.agentList[i])
        #print factoryTmpList
        if factoryTmpList != []:
          random.shuffle(factoryTmpList)
          toBeRemoved=factoryTmpList[0]

          if common.verbose: print "Removed factory #",toBeRemoved.number,\
                                 "from sector",toBeRemoved.sector

          toBeRemoved.removeItself()

def modPosition():
    if random.randint(0,1)==0:return random.randint(-8,-6)
    else:                     return random.randint( 6, 8)

def otherSubSteps(subStep, address):

            if subStep == "addAFactory":
              addAFactory(address)
              return True

            if subStep == "removeAFactory":
              removeAFactory(address)
              return True

            else: return False
