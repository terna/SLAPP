#Agent.py
from Tools import *
from agTools import *
import graphicDisplayGlobalVarAndFunctions as gvf
import commonVar as common

class Agent(SuperAgent):
    def __init__(self, number,myWorldState,
                 xPos=0, yPos=0, lX =-20,rX=19, bY=-20,tY=19, agType="",
                 sector=0):

        # the environment

        self.agOperatingSets=[]
        self.number = number

        if agType == 'recipes':
            self.content=[]
            self.canMove=False
            self.maxLength=common.maxLenght
            self.maxSector=common.maxSector
            self.factoryInWhichRecipeIs=None

        if agType == 'factories':
            self.sector=sector
            self.recipeWaitingList=[]
            common.orderedListOfNodes.append(self)
            #use to keep the order
            #in output (ex. adjacency matrix)

        self.myWorldState = myWorldState
        self.agType=agType

        # the graph
        if gvf.getGraph() == 0: gvf.createGraph()

        # the agent
        if self.agType == "factories":
         if common.verbose: print "agent of type", self.agType, \
               "#", self.number, "has been created at", xPos, ",", yPos, \
        	      ' in production sector ', self.sector

         common.g.add_node(self)
         common.g.node[self]['sector']=sector
         gvf.colors[self]="LightGray"
         # colors at http://www.w3schools.com/html/html_colornames.asp
         gvf.pos[self]=(xPos,yPos)
         common.g_labels[self]=str(number)
         # to be used to clone (if any)
         self.xPos=xPos
         self.yPos=yPos
         self.sector=sector

        if self.agType == "recipes":
         if common.verbose: print "agent of type", self.agType, "#", self.number, \
        	      "has been created"


    # get graph
    def getGraph(self):
        return common.g


    # ",**d" in the parameter lists of the methods is a place holder
    # in case we use, calling the method, a dictionary as last par

    # fill the content
    def setRecipeContent(self):
        if self.agType != "recipes": return

        if self.content != []: return

        self.canMove=True
        length=random.randint(1,self.maxLength)
        for i in range(length+1):
            self.content.append(random.randint(1,self.maxSector))
        self.factoryInWhichRecipeIs=None

        if common.verbose: print "recipe %d now contains the sequence: " \
                           % (self.number), self.content


    # search for factories
    def searchForSector(self):
        if self.agType != "recipes": return

        if not self.canMove: return

        step=self.content[0] # first step to be done

        res=gvf.findNodesFromSector(step)
        if common.verbose:
           if res ==[]:
               print "recipe %d cannot find a factory for the step of type %d"\
                         % (self.number, step)
        else:
           if common.verbose:
               print "recipe %d found %d factory/ies for the step of type %d"\
                         % (self.number, len(res), step)


        # for debug only!!!!!!!!!!!!!
        #if res!=[]:
        # for aNode in res: print "searchForSector:", aNode.number, aNode.sector
        #else: print "searchForSector: no node for sector", step

        if res !=[]:
            random.shuffle(res)
            if common.verbose: print "recipe %d moving to factory %d" % (self.number,res[0].number)

			# future development: here res[0] simply contain a randomly chosen unit
			# (if in res we have more than a unique possibility)
			# it is possible to put here intelligence (as the effect of the)
			# action of the recipe, searching for data such as production costs of
			# the factories, their waiting lists, their quality standards, their
			# owners, etc.


            # create an edge from self.factoryInWhichRecipeIs to res[0]
            # or upgrading the weight of the link
            if self.factoryInWhichRecipeIs != None: \
                  gvf.createEdge(self.factoryInWhichRecipeIs, res[0])
            self.factoryInWhichRecipeIs=res[0]

            res[0].addToRecipeWaitingList(self) #self here is the calling recipe


    # check if next step can be produced
    def checkIfNextStepCanBeAccomplished(self, aRecipe):
        step=aRecipe.content[0] # next step to be done
        res=gvf.findNodesFromSector(step)

        if res != []: return True
        else:         return False


    # waiting list in factories
    def addToRecipeWaitingList(self, recipe):
        if self.agType != "factories": return


        recipe.canMove=False
        self.recipeWaitingList.append(recipe)
        if common.verbose: print "factory %d waiting list contains %d recipe/s" % \
                                  (self.number,len(self.recipeWaitingList))

        #update factory label
        #the try below is not subject to debug
        try:    pseudoL=common.g[self][self]['pseudoLabel']
        except: pseudoL=""
        gvf.common.g_labels[self]=str(self.number)+" ("+\
                                  str(len(self.recipeWaitingList))+") "\
                                  + "\n"+pseudoL

    # produce
    def produce(self):
        if self.agType != "factories": return

        if self.recipeWaitingList == []: return
        currentRecipe=self.recipeWaitingList[0]

        # remove the current recipe (if next sector exists or if the present
        #                            one is the last step)
        if len(currentRecipe.content)>1:
          if self.checkIfNextStepCanBeAccomplished(currentRecipe):
             self.recipeWaitingList.remove(currentRecipe)
             #if next step cannot be accomplished, the recipe is locked here
        if len(currentRecipe.content)==1:
             self.recipeWaitingList.remove(currentRecipe)

        if common.verbose: print "factory %d producing (recipe %d)" % (self.number, currentRecipe.number)

        currentRecipe.content.pop(0)
        currentRecipe.canMove=True

        if currentRecipe.content == []:
            currentRecipe.canMove=False
            if common.verbose: print "recipe %d completed in factory %d" \
                  % (currentRecipe.number,self.number)


    # addAFactory
    def addAFactory(self):
        if self.agType != "factories": return

        # create a new factory cloning an existing one
        # choose randomly a factory (also a cloned one)

        toBeCloned=self
        #print toBeCloned.number

        # creating

        common.clonedN+=1
        anAgent = Agent(toBeCloned.number*100+common.clonedN,
                        self.myWorldState,
                        toBeCloned.xPos+modPosition(),
                        toBeCloned.yPos+modPosition(),
                        agType=toBeCloned.agType,
                        sector=toBeCloned.sector)
        self.agentList.append(anAgent)
        # updating the agentList of all the agents
        for anAg in self.agentList:
            anAg.setAgentList(self.agentList) # in this way, also the new agent
                                              # has its agentList (updated)
        # udating the agentList in the ModelSwarm instance
        common.modelAddress.agentList=self.agentList

        if common.verbose: print "Factory", self.number, "has created factory #",\
                                  anAgent.number,"in sector",anAgent.sector

    # remove itself
    def removeItself(self):
        if self.agType != "factories": return

        toBeRemoved=self
        if common.verbose: print "Factory #",toBeRemoved.number,\
                                 "removed itself from sector",toBeRemoved.sector
        self.agentList.remove(toBeRemoved)

        # updating the agentList of all the agents
        for anAg in self.agentList:
            anAg.setAgentList(self.agentList) # in this way, also the new agent
                                              # has its agentList (updated)
        # udating the agentList in the ModelSwarm instance
        common.modelAddress.agentList=self.agentList

        #print "removeItself verification of surviving agents"
        #for i in range(len(self.agentList)):
        #    if self.agentList[i].agType=="factories":
        #          print self.agentList[i].number,

        common.orderedListOfNodes.remove(toBeRemoved)
        #print "\nremoveItself node removed in graph", toBeRemoved, \
        #      toBeRemoved.number

        edges_toBeDropped=[]
        for edge in common.g.edges():
            if edge[0]==toBeRemoved or edge[1]==toBeRemoved:
                edges_toBeDropped.append(edge)
        if edges_toBeDropped != []:
            for edge in edges_toBeDropped:
               #print "removeItself edge removed in graph", edge
               if common.g_edge_labels.has_key(edge):
                   common.g_edge_labels.pop(edge)

        #print "removeItself previous nodes in graph", common.g.nodes()
        common.g_labels.pop(toBeRemoved)

        # remove factoryInWhichRecipeIs from all the recipes, also
        # that having just left this factory and waiting for
        # searchForSector order
        if self.agentList != []:
            for anAg in self.agentList:
                if anAg.agType=="recipes" and \
                   anAg.factoryInWhichRecipeIs==self:
                       anAg.factoryInWhichRecipeIs=None

        # recipes in the waiting list
        #print "removeItself recipes in the factory before cleaning"
        #if self.recipeWaitingList != []:
        #    for aR in self.recipeWaitingList:
        #        print aR.number, aR.factoryInWhichRecipeIs,
        #        aR.content
        #else: print "None"

        if self.recipeWaitingList != []:
            for aRecipe in self.recipeWaitingList:
                aRecipe.content = []
                aRecipe.canMove=False
                #aRecipe.factoryInWhichRecipeIs=None # done above

        """
        print "removeItself recipes in the factory after cleaning"
        if self.recipeWaitingList != []:
            for aR in self.recipeWaitingList:
                print aR.number, aR.factoryInWhichRecipeIs, aR.content
        else: print "None"
        """

        common.g.remove_node(toBeRemoved)
        #print "removeItself residual nodes in graph", common.g.nodes()


def modPosition():
    if random.randint(0,1)==0:return random.randint(-8,-6)
    else:                     return random.randint( 6, 8)
