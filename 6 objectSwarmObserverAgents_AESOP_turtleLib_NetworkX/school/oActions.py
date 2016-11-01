from Tools import *
from Agent import *

def do1b(address):
    pass

def do2a(address,cycle):
            self=address # if necessary
            maxY=15 # max on Y axis

            # ask each agent, without parameters
            #print "Time = ", cycle, "ask all agents to report position and attention"
            #askEachAgentInCollection(address.modelSwarm.getAgentList(),Agent.reportPosition)

            if self.v_==[]:
                for a in address.modelSwarm.getAgentList():
                  self.n_.append(a.number)

                i=5
                for a in address.modelSwarm.getAgentList():
                  self.p.penup()
                  self.p.black(-250+i,134)
                  self.p.pendown()
                  self.p.label(str(a.number))
                  
                  i+=20

                
                self.p.penup()
                self.p.black(-250,250)
                self.p.pendown()
                self.p.label(str(maxY))
                self.p.black(-250,150)
                self.p.penup()
                self.p.black(-250,274)
                self.p.pendown()
                self.p.label(" Attention of each pupil")
                self.p.penup()
                self.p.black(-250,150)
                self.p.pendown()

                
            vD=[]
            if self.v_ != []:
                vD = self.v_[:] # D=delete
                del  self.v_[:]
            
            for a in address.modelSwarm.getAgentList():
                #print "agent", a.number, "attention = ",a.getAttention()
                self.v_.append(a.getAttentionAndCleanStep())
            print 'attention index for each pupil =',
            for i in range(len(self.n_)):
                print "["+str(self.n_[i])+","+str(self.v_[i])+"] ",
            print 

            self.p.penup()
            self.p.black(-250,150)
            self.p.pendown()

            k=100./maxY
            
            for i in range(len(self.v_)):
                self.p.black(-240+i*20,150)
                if vD != []: self.p.white(-240+i*20,150+     vD[i]*k)
                self.p.penup()
                self.p.black(-240+i*20,150+self.v_[i]*k)
                self.p.pendown()
                self.p.black(-240+i*20,150)


            
                     

def do2b(address,cycle):
            self=address # if necessary
            
            # ask a single agent, without parameters
            print "Time = ",cycle,"ask first agent to report position"
            if address.modelSwarm.getAgentList() != []:
                askAgent(address.modelSwarm.getAgentList()[0],\
                         Agent.reportPosition)

def otherSubSteps(subStep, address):
            return False
