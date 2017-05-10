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

def createTheAgent(self,line,num,agType):
                #explictly pass self, here we use a function

                if len(line.split())==1: # weak control, can be improved
                 anAgent = Agent(num, self.worldState,
                          random.randint(self.leftX,self.rightX),
                          random.randint(self.bottomY,self.topY),
                          self.leftX,self.rightX,self.bottomY,self.topY,agType=agType)
                 self.agentList.append(anAgent)

                else:
                 print("Error in file "+agType+".txt")
                 os.sys.exit(1)

def createTheAgent_Class(self,line,num,agType,agClass):
                #explictly pass self, here we use a function

                # check if the file having the content of agClass and extension
                # .py exists

                common.agClassVerified=False
                if not common.agClassVerified:
                    try:
                        exec("import "+agClass)
                        common.agClassVerified=True
                    except:
                        print("Missing file "+agClass+".py")
                        os.sys.exit(1)


                # first step in exec:
                # access the files of the classes to create the instances
                # N.B. to simplify the structure of SLAPP, the name of the
                # class and the name of the file containing it, have to be the same.
                if len(line.split())==1: # weak control, can be improved
                  try:
                    space={'num':num, 'sW': self.worldState, \
                           'random':random, 'leftX': self.leftX, 'rightX': self.rightX, \
                           'bottomY': self.bottomY, 'topY': self.topY, 'agType': agType}
                    exec("from "+agClass+" import *;"+\
                         "anAgent = "+agClass+"(num, sW,"+\
                         "random.randint(leftX,rightX),"+\
                         "random.randint(bottomY,topY),"+\
                         "leftX,rightX,bottomY,topY,agType=agType)", space)
                    anAgent=space['anAgent']
                    self.agentList.append(anAgent)
                  except:
                    print("Argument error creating an instance of class",agClass)
                    os.sys.exit(1)


def otherSubSteps(subStep, address):
            return False
