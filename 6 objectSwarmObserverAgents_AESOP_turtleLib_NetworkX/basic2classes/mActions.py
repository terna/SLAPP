from Tools import *
from Agent import *
import os

def do0(address):
            self=address # if necessary
            askEachAgentInCollection(address.agentList, Agent.setNewCycleValues)

def do1(address):
            self=address # if necessary
            # set in each call to the group
            self.actionGroup1.setName("move")
            # set in each call to the group

            # keep safe the original list
            address.agentListCopy=address.agentList[:]
            # never in the same order (please comment if you want to keep
            # always the same sequence
            random.shuffle(address.agentListCopy)
            # move with a jump, to have to transfer a parameter
            # the format is: collection, method, parameters by name
            # ask each agent, without parameters
            # the potential jump is the same for all the agents

            # alternatively, we can pass the method as a str
            # (new way from v.1.36)
            askEachAgentInCollectionAndExecLocalCode \
                     (address.agentListCopy,"randomMovement",
                                        jump=random.uniform(0,5))

            # or as an unbound method (the way used for v. <1.36)

            #askEachAgentInCollectionAndExecLocalCode \
            #         (address.agentListCopy,Agent.randomMovement,
            #                            jump=random.uniform(0,5))

            # the str way is preferred for agents subclassing Agent class
            # the other one is maintained for compatibility with
            # previous mActions.py files

def createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType):
                #explictly pass self, here we use a function
                #print "leftX,rightX,bottomY,topY", leftX,rightX,bottomY,topY

                if len(line.split())==1:
                 anAgent = Agent(num, self.worldState,
                          random.randint(leftX,rightX),
                          random.randint(bottomY,topY),
                          leftX,rightX,bottomY,topY,agType=agType)
                 self.agentList.append(anAgent)

                else:
                 print "Error in file "+agType+".txt"
                 os.sys.exit(1)

def createTheAgent_Class(self,line,num,leftX,rightX,bottomY,topY,agType,agClass):
                #explictly pass self, here we use a function
                #print "leftX,rightX,bottomY,topY", leftX,rightX,bottomY,topY


                # loading classes with repetition (but only creating agents)
                try: exec("from "+agClass+" import *")
                except:
                    print "Class", agClass, "not found."
                    os.sys.exit(1)

                if len(line.split())==1:
                  try:
                    exec("anAgent = "+agClass+"(num, self.worldState,"+\
                          "random.randint(leftX,rightX),"+\
                          "random.randint(bottomY,topY),"+\
                          "leftX,rightX,bottomY,topY,agType=agType)")
                    self.agentList.append(anAgent)
                  except:
                    print "Argument error creating an instance of class",agClass
                    os.sys.exit(1)

                else:
                 print "Error in file "+agType+".txt"
                 os.sys.exit(1)


def otherSubSteps(subStep, address):
            return False
