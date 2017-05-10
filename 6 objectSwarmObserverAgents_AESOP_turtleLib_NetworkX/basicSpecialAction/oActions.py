from Tools import *
from Agent import *

def do1b(address):
    pass

def do2a(address,cycle):
            self=address # if necessary

            # ask each agent, without parameters

            print("Time = ", cycle, "ask all agents to report position")
            askEachAgentInCollection(address.modelSwarm.getAgentList(),Agent.reportPosition)


def do2b(address,cycle):
            self=address # if necessary

            # ask a single agent, without parameters
            print("Time = ",cycle,"ask first agent to report position")
            if address.modelSwarm.getAgentList() != []:
                askAgent(address.modelSwarm.getAgentList()[0],\
                         Agent.reportPosition)

def otherSubSteps(subStep, address):
            return False


# an example of special action code, to be activated if the time
# (cycle) is equal to ...
# to pass variables to the function, simply use the common area
def makeSpecialAction():

    if common.cycle == 1:
        print("doing a special action at time =", common.cycle)

    if common.cycle == 2:
        print("doing a special action at time =", common.cycle)

    # etc.
