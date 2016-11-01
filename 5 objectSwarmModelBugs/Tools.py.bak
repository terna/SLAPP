import random
import os


# applying a method to a collection of instances
def askEachAgentIn(collection,method,**k):
    """ collection, method, dict. of the parameters (may be empty)"""

    for a in collection:
            method(a,**k)


# applying a method to an instance of a class
def askAgent(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    method(agent,**k)


# extracting a step and rotating a list
def extractAStepAndRotate(aList):
        if len(aList)==0:
            print "Error: action list is empty"
            os.sys.exit(0)

        aSubList=aList.pop(0)
        if type(aSubList)!=list:
            print "Error: the elements of the action list need to be a list"
            os.sys.exit(0)
        aList.append(aSubList)

        return aSubList[:] # with [:] we return the elements
                           # of aSubList, not the address

# extracting a subStep
def extractASubStep(aSubList):
        if len(aSubList)>0: return aSubList.pop(0)
        else: return []

# insert an element in next sub-step (first position)
def insertASubStepElementInNextStep_firstPosition(aList,what):
    aList[0].insert(0,what)

# insert an element in nest sub-step (last position)
def insertASubStepElementInNextStep_lastPosition(aList,what):
    aList[0].append(what)
