#ModelSwarm.py
import Tools
from Agent import *
import commonVar as common
common.worldStateExist=True
try: from WorldState import *
except: common.worldStateExist=False
from ActionGroup import *
import random
import os
from mActions import *
from turtle import *

# structure for adding and eliminating tasks
common.addTasks={}
common.elimTasks={}

# in this module, a few of the try/except structures are not cotrolled
# for debug

# these try/except constucts, indeed, are not intended to control user
# errors, but a regular flow of inputs

# other try/execpt structures are instead controlled for debug


task="0 0".split()

class ModelSwarm:
    def __init__(self, nAgents, worldXSize, worldYSize, project0):
        global task, project
        project=project0

        # the environment
        task="0 0".split() #in case of repeated execution without restarting the shell
        self.ff="" #in case of repeated execution without restarting the shell
        self.nAgents = nAgents # bland ones
        self.agentList = []

        self.worldXSize= worldXSize
        self.worldYSize= worldYSize

        # types of the agents
        agTypeFile=open(project+"/agTypeFile.txt","r")
        self.types=agTypeFile.read().split()
        agTypeFile.close()
        #print self.types

        # classes of the agents
        self.classes={}
        try:
            agClassFile=open(project+"/agClassFile.txt","r")
            items=agClassFile.read().split()
            agClassFile.close()
            for i in range(0,len(items),2):
                self.classes[items[i]]=items[i+1]

        except:
        # all the types have class Agent
            for i in range(len(self.types)):
                self.classes[self.types[i]]="Agent"


        # check consistency between types and classes
        if len(self.types) != len(self.classes):
            print 'Mismatch in number of types and classes.'
            os.sys.exit(1)
        for i in range(len(self.types)):
            if not self.classes.has_key(self.types[i]):
                print 'Type', self.types[i], 'has no class.'
                os.sys.exit(1)

        print '\nAgents and their classes'
        for i in range(len(self.classes)):
            print 'agents', self.types[i],'have class',\
                  self.classes[self.types[i]]
        print "'bland' agents, if any, have always class Agent\n"

        # operating sets of the agents
        try:
            agOperatingSetFile=open(project+"/agOperatingSets.txt","r")
            self.operatingSets=agOperatingSetFile.read().split()
        except:
            print 'Warning: operating sets not found.'
            agOperatingSetFile = False
            self.operatingSets=[]
        if agOperatingSetFile: agOperatingSetFile.close()
        #print self.operatingSets


        dictExe={}
        dictExe["project"]=project
        execfile("./$$slapp$$/convert_xls_txt.py",dictExe)

    # objects
    def buildObjects(self):

        try: self.verbose=common.verbose
        except: self.verbose=False

        if common.worldStateExist:
            self.worldState = WorldState()
        else:
            self.worldState=0

        leftX =int(-self.worldXSize/2)
        rightX=int(self.worldXSize-1 -self.worldXSize/2)
        bottomY =int(-self.worldYSize/2)
        topY=int(self.worldYSize-1 -self.worldYSize/2)

        # internal agents (bland ones)
        for i in range(self.nAgents):
            anAgent = Agent(i, self.worldState,
                    random.randint(leftX,rightX),
                    random.randint(bottomY,topY), leftX,rightX,
                    bottomY,topY,agType="bland")
            self.agentList.append(anAgent)
        print

        # external agents, RELATED TO THE SPECIFIC project
        files=os.listdir(project)

        for agType in self.types:
          # extended txt (.txtx)
          if agType+".txtx" in files:
             dictExe={}
             dictExe["project"]=project
             dictExe["fileName"]=agType
             execfile("./$$slapp$$/convert_txtx_txt.py",dictExe)

        # update for new .txt file created above
        files=os.listdir(project)

        for agType in self.types:
            if not agType+".txt" in files: print "No", agType,\
               "agents: lacking the specific file", agType+".txt"

        for opSet in self.operatingSets:
            if not opSet+".txt" in files: print "No", opSet,\
               "agents: lacking the specific file", opSet+".txt"
        print

        # crating the agents
        for agType in self.types:

         if agType+".txt" in files:
           f=open(project+"/"+agType+".txt","r")
           for line in f:
            if line.split() != []:
               num=int(line.split()[0])
               if self.verbose and not common.IPython:
                    print "creating "+agType+": agent #", num
                    # this output locks IPython when we have large number
                    # of agents
               #print line.split()

               # a set of specialized creation function for each model
               # are in mActions.py in the model folder

               if self.classes[agType]=="Agent":
                 createTheAgent(self,line,num,leftX,rightX,bottomY,topY,agType)
                 #explictly pass self, here we use a function

               else:
                 # using ad hoc classes
                 createTheAgent_Class(self,line,num,leftX,rightX,bottomY,topY,\
                        agType,self.classes[agType]) # the last is the class


           f.close()

        for opSet in self.operatingSets:
         if opSet+".txt" in files:
           f=open(project+"/"+opSet+".txt","r")
           for line in f:
               if line.split() != []:
                num=int(line.split()[0])
                for anAgent in self.agentList:
                    if anAgent.number == num:
                        anAgent.setAnOperatingSet(opSet)
                        print "including agent #", num, \
                              "into the operating set", opSet
           f.close()

        if self.operatingSets != []:
         for anAgent in self.agentList:
            anAgent.setContainers()

        if self.agentList != []:
         for anAgent in self.agentList:
            anAgent.setAgentList(self.agentList)


        print


    # actions
    def buildActions(self):

        modelActions=open(project+"/modelActions.txt")
        mList=modelActions.read().split()
        modelActions.close()

        self.actionList = mList
        #print self.actionList

        # look at basic case schedule, where "move" represents an example of mandatory
        # action (in our case generating also a dynamic "jump" action) and
        # "read_script" represents an external source of actions

        # without reading an external schedule (anyway, in the case
        # above, if you do not put a schedule.txt or a schedule.xls file in
        # program folder), the "read_script" step simply has no effect)

        # basic actionGroup

        self.actionGroup0 = ActionGroup ("reset")
        self.actionGroup0.do = do0 # do is a variable linking a method

        self.actionGroup1 = ActionGroup ("move")
        self.actionGroup1.do = do1 # do is a variable linking a method

        # to create other actionGroup ..,
        #self.actionGroup2 = ActionGroup (self.actionList[?])
        #self.actionGroup2.do = do2 # do is a variable linking a method
        # etc.

        # this actionGroup is the schedule, which is generalized
        # so it is not moved in the actions.py specific to the project
        # the task number is huge (100), considering it to be the last one
        # the name is identified as the last one, with -1
        self.actionGroup100 = ActionGroup ("read_script") # the last
        def do100(address, cycle):
            global task

            while True:
                if task[0]=="#":
                    if int(task[1]) > cycle: break

                ## check for added tasks
                if addedTask(cycle): task=getAddedTask(cycle)
                ## regular schedule
                else: task=read_s(self.ff)
                #print "***", task

                ## check for eliminated tasks
                if elimTask(cycle):
                    task=getElimTask(task,cycle)
                    #print '---', task

                if task[0]=="#":
                    if int(task[1]) > cycle: break
                if task[0]=="0": break

                #if task[0] is all or an agent type
                if check(task[0],self.types,address.operatingSets):
                    # keep safe the original list
                    localList=[]
                    for ag in address.agentList:
                        if   task[0]=="all": localList.append(ag)
                        elif task[0]==ag.getAgentType(): localList.append(ag)

                    # never in the same order (please comment if you want to keep
                    # always the same sequence
                    random.shuffle(localList)
                    # apply method only to a part of the list, or, which is the
                    # same, with the given probability to each element of the list
                    self.share=0
                    try:    self.share = float(task[1]) # does task[1] contains
                                                        # a int or float number?
                    except: pass

                    if self.share > 0:
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(len(tmpList)):
                            if random.random() <= self.share:
                                localList.append(tmpList[i])

                    if self.share < 0: # in case, an abs. number of agent *(-1)
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(int(-self.share)):
                            random.shuffle(tmpList)
                            if tmpList != []:
                                localList.append(tmpList.pop(0))

                    # apply
                    if len(localList)>0:
                        self.applyFromSchedule(localList,task)

                #if task[0] is an opSet
                if task[0] in address.operatingSets:
                    # keep safe the original list
                    localList=[]
                    for ag in address.agentList:
                        if task[0] in ag.getOperatingSetList():
                            localList.append(ag)
                    if localList==[]:
                        print "Warning, no agents in operating set", task[0]
                    # never in the same order (please comment if you want to keep
                    # always the same sequence
                    random.shuffle(localList)
                    # apply method only to a share of the list
                    self.share=0
                    try:    self.share = float(task[1])   # does task[1] contains
                                                          # an int or float number?
                    except: pass


                    if self.share > 0:
                        tmpList=localList[:]
                        del localList[:]
                        for i in range(len(tmpList)):
                            if random.random() <= self.share:
                                localList.append(tmpList[i])

                    if self.share < 0: # in case, an abs. number of agent *(-1)
                        tmpList=localList[:]
                        #print "*********************", tmpList
                        del localList[:]
                        for i in range(int(-self.share)):
                            random.shuffle(tmpList)
                            if tmpList != []:
                                localList.append(tmpList.pop(0))
                        #print "*********************", localList

                    # apply
                    if len(localList)>0:
                        self.applyFromSchedule(localList,task)

                if task[0]=='WorldState':
                    #self.share=0
                    if address.worldState==0:
                        print "WorldState.py is missing, you cannot use WorldState here."
                        os.sys.exit(1)
                    localList=[address.worldState] #apply from schedule works on a list
                    self.applyFromSchedule(localList,task)

        self.actionGroup100.do = do100 # do is a variable linking a method





    # run a step
    def step(self,cycle):
            global task

            step=self.actionList[:]

            while len(step)>0:
                subStep=extractASubStep(step)
                #print "*****************", subStep
                found=False

                if subStep == "reset":
                        found=True
                        self.actionGroup0.do(self)
                if subStep == "move":
                        found=True
                        self.actionGroup1.do(self)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable


                # external schedule, in pos. -1
                if subStep == "read_script":
                        found=True
                        if self.ff=="":
                           #create the dictionary of methods probability. if any
                           try:
                             schedule=open(project+"/schedule.txt","r")
                             common.methodProbs={}
                             for line in schedule:
                               lineSplit=line.split()
                               if len(lineSplit)==3 and lineSplit[1].find('.')>0:
                                  if  float(lineSplit[1]) > 0:
                                    common.methodProbs[lineSplit[2]]=float(lineSplit[1])
                             if common.methodProbs != {}:
                                 print "methodProbabilities =", common.methodProbs
                             schedule.close()
                           except: pass

                           try: self.ff=open(project+"/schedule.txt","r")
                           except: pass
                        self.actionGroup100.do(self,cycle)
                    # self here is the model env.
                    # not added automatically
                    # being do a variable

                # other steps
                if not found:
                 found=otherSubSteps(subStep, self)

                if not found: print "Warning: step %s not found in Model" % subStep



    # from external schedule (script)
    def applyFromSchedule(self,localList,task):


        if task[0]=='WorldState':

            # computational use

            #localList contains a unique worldState instance
            if task[1]=="computationalUse" or task[1]=="specialUse":
                #localList contains a unique worldState instance
                if common.debug: exec "localList[0]."+task[2]+"()"
                else:
                  try: exec "localList[0]."+task[2]+"()"
                  except: print task[2], "undefined in WorldState"

            # using WorldState to set/get values

            else:
                try:  aValue = float(task[1]) # does task[1] contains a number?                                             # a number?
                except:
                    print "After WorldState, in schedule.xls we wait: "+\
                          "'computationalUse' or 'specialUse' or "+\
                          "a number.", task[1],"found."
                    os.sys.exit(1)
                if task[2] != "":
                    d={}
                    d[task[2]]=float(task[1])
                    #localList contains a unique worldState instance
                    if common.debug: exec "localList[0]."+task[2]+"(**d)"
                    else:
                      try: exec "localList[0]."+task[2]+"(**d)"
                      except: print task[2], "undefined in WorldState"
                else:
                    print "Unable to handle a missing task in WorldState schedule."
                    os.sys.exit(1)

        #if task[0] is 'all' or a type of agent
        if check(task[0],self.types,self.operatingSets):
            if self.share!=0:
               # NOTE *** the ask with Agent.method in the form
               # "askEachAgentInCollection(localList,Agent"+"."+task[2]+")" is
               # still operating for old calls in mActions.py modules nut it is
               # deprecated here, confusing the execution in presence of
               # subclasses of Agent
               if common.debug: exec "askEachAgentInCollection(localList,task[2])"
               else:
                try: exec "askEachAgentInCollection(localList,task[2])"
                except:
                    print "Warning, method", task[2],"does not exist"
            else:
               # see NOTE *** above
               if common.debug: exec "askEachAgentInCollection(localList,task[1])"
               else:
                try: exec "askEachAgentInCollection(localList,task[1])"
                except:
                    print "Warning, method", task[1],"does not exist"

        #if task[0] is an opSet
        if task[0] in self.operatingSets:
            if self.share!=0:
               # see NOTE *** above
               if common.debug: exec "askEachAgentInCollection(localList,task[2])"
               else:
                try: exec "askEachAgentInCollection(localList,task[2])"
                except:
                    print "Warning, method", task[2],"does not exist"
            else:
               # see NOTE *** above
               if common.debug: exec "askEachAgentInCollection(localList,task[1])"
               else:
                try: exec "askEachAgentInCollection(localList,task[1])"
                except:
                    print "Warning, method", task[1],"does not exist"



    # agent list
    def getAgentList(self):
        return self.agentList

    # file address
    def getFile(self):
        return self.ff

# tools, read_s
def read_s(f):
    if f != "":
        try:
            task=f.readline()
            if task=='':task='0 0'
        except:
            task='0 0'
    else: task='0 0'

    return task.split()

# check if it is an agent
def check(s,aList,opSets):
    found=False
    if s.find("all")==0  : found=True
    if s.find("bland")==0: found=True
    for name in aList:
        if s.find(name)==0:found=True

    # agent not found (maybe 'dummy' has been set as a fictitious
    # agent name, to eliminate a task due to the action made by
    # an agent)
    if not found and not s in opSets and s != '#' and not s.find("WorldState")==0:
        print "agent", s, 'does not exist'

    return found


## look for tasks to be added
def addedTask(t):
    if common.addTasks.has_key(t):
       if common.addTasks[t] == []: return False
       else:                        return True
    else:                           return False


## find tasks to be added
def getAddedTask(t):
    # returning the first item and removing it
    return common.addTasks[t].pop(0).split()

## look for tasks to be eliminated
def elimTask(t):
    if common.elimTasks.has_key(t):
       if common.elimTasks[t] == []: return False
       else:                         return True
    else:                            return False

## find tasks to be Eliminated
def getElimTask(task,t):
    found=False
    i=-1
    for killTask in common.elimTasks[t]:
        i+=1
        if task[0]==killTask.split()[0] and \
           task[1]==killTask.split()[1]:
           if len(killTask.split())==3:
               if task[2]==killTask.split()[2]: found=True
           else:                                found=True

    if found:
        common.elimTasks[t].pop(i)
        print task[0],'modified to dummy in:', task
        task[0]='dummy'

    return task
