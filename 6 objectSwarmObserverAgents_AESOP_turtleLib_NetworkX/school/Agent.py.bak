#Agent.py
from Tools import *
from agTools import *
from turtle import *

register_shape("school/pupilBlackF.gif")
register_shape("school/pupilGreenF.gif")
register_shape("school/pupilRedF.gif")
register_shape("school/pupilYellowF.gif")
register_shape("school/pupilSpecialF.gif")
register_shape("school/pupilBlackM.gif")
register_shape("school/pupilGreenM.gif")
register_shape("school/pupilRedM.gif")
register_shape("school/pupilYellowM.gif")
register_shape("school/pupilSpecialM.gif")

register_shape("desk",((5,-15),(15,-15),(15,15),(5,15)))

class Agent(Turtle, SuperAgent):
    def __init__(self, number, myWorldState,
                 xPos, yPos, lX =-20,rX=19, bY=-20, tY=19, agType=""):
        Turtle.__init__(self)
        # nb lX (left lim. on X axis),
        #    rX (right lim. on X axis),
        #    bY (bottom lim. on Y axis),
        #    tY (top lim. on y axis),
        # are defined in ModelSwarm.py

        # the environment
        self.agOperatingSets=[]
        self.number = number
        self.lX = lX
        self.rX = rX
        self.bY = bY
        self.tY = tY
        self.myWorldState = myWorldState
        self.agType=agType
        # the agent
        self.xPos = xPos
        self.xPos0=xPos
        self.yPos = yPos
        self.yPos0=yPos
        self.deltaAtt=0
        print "agent", self.agType, "#", self.number, \
     	      "has been created at", self.xPos, ",", self.yPos

        # turtle behavior
        self.speed(0)
        self.penup()
        self.color("black") # default color
        self.setx(self.xPos*1) # *1 is a memo to change scale if needed
        self.sety(self.yPos*1)

        # attention accounting
        self.attention=0
        self.tickAttention=0
        self.nMethodsAttention=0

        self.lastExecutedMethod=''

    def setColorAndGender(self,color,gender):
        self.color(color)
        self.gender=gender
        if gender=="F":
         if color=="black"  : self.shape("school/pupilBlackF.gif")
         if color=="green"  : self.shape("school/pupilGreenF.gif")
         if color=="red"    : self.shape("school/pupilRedF.gif")
         if color=="yellow" : self.shape("school/pupilYellowF.gif")
         if color=="violet" : self.shape("school/pupilSpecialF.gif")
        if gender=="M":
         if color=="black"  : self.shape("school/pupilBlackM.gif")
         if color=="green"  : self.shape("school/pupilGreenM.gif")
         if color=="red"    : self.shape("school/pupilRedM.gif")
         if color=="yellow" : self.shape("school/pupilYellowM.gif")
         if color=="violet" : self.shape("school/pupilSpecialM.gif")

        if color=="brown"  : self.shape("desk")

    # reset values (substitures that in agTools.py)
    def setNewCycleValues(self):
        self.deltaAtt=0
        #self.attention=0
        #self.lastExecutedMethod=''

    # attention (total value until previous step)
    def getAttention(self):
        return self.attention

    # attention (with the last step)
    def getAttentionAndCleanStep(self):
        self.attention+=self.tickAttention
        self.tickAttention=0
        self.nMethodsAttention=0
        return self.attention

    # ",**d" in the parameter lists of the methods is a place holder
    # in case we use, calling the method, a dictionary as last param.

    # active methods

    # asking well
    def askWell(self,**d):
        self.lastExecutedMethod=self.askWell
        print
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm asking well!"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention

        self.write("Asking well!!!", font=("Arial", 14)) # turtle action

    # fidgeting
    def fidget(self,**d):
        self.lastExecutedMethod=self.fidget
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm fidgeting"
        add=random.random()*0.3+0.7
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention

    # shaking
    def shake(self,**d):
        self.lastExecutedMethod=self.shake
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm shaking"
        if self.agType == "greenPupil":
            add=random.random()*0.3+0.6
        else: add=random.random()*0.4+0.4
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.xPos+=random.random()*20-10
        self.setx(self.xPos)
        self.yPos+=random.random()*20-10
        self.sety(self.yPos)

        self.write("Shaking", font=("Arial", 16)) # turtle action

    # twisting
    def twist(self,**d):
        self.lastExecutedMethod=self.twist
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm twisting"
        add=random.random()*0.3
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.xPos+=random.random()*30-10
        self.setx(self.xPos)
        self.yPos+=random.random()*30-10
        self.sety(self.yPos)

        self.write("Twisting", font=("Arial", 16)) # turtle action



    # paying attention
    def payAttention(self,**d):
        self.lastExecutedMethod=self.payAttention
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm paying attention"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

    # attracting attention teacher well
    def attractTeacherAttentionWell(self,**d):
        self.lastExecutedMethod=self.attractTeacherAttentionWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm attracting Teacher attention well"

        # not relevant for attention

        self.write("Excuse me", font=("Arial", 12)) # turtle action


    # attracting attention teacher not well
    def attractTeacherAttentionNotWell(self,**d):
        self.lastExecutedMethod=self.attractTeacherAttentionNotWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm attracting Teacher attention not well"

        # not relevant for attention

        self.write("TEACHER!!", font=("Arial", 14)) # turtle action




    # attention elsewhere
    def attElsewhere(self,**d):
        self.lastExecutedMethod=self.attElsewhere
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "and I'm distracted"
        add=random.random()*0.2
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("!?!?", font=("Arial", 14)) # turtle action


    # sitting down not well
    def sitDownNotWell(self,**d):
        self.lastExecutedMethod=self.sitDownNotWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm sitting down not well"

        # not relevant for attention

        self.xPos=self.xPos0+random.random()*20-10
        self.setx(self.xPos)
        self.yPos=self.yPos0+random.random()*20-10
        self.sety(self.yPos)

    # sitting down well
    def sitDownWell(self,**d):
        self.lastExecutedMethod=self.sitDownWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm sitting down well"

        # not relevant for attention

        self.xPos=self.xPos0
        self.setx(self.xPos)
        self.yPos=self.yPos0
        self.sety(self.yPos)

    # standing up
    def standUp(self,**d):
        self.lastExecutedMethod=self.standUp
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm standing up"

        # not relevant for attention

        self.xPos=self.xPos0
        self.setx(self.xPos)
        self.yPos=self.yPos0
        self.sety(self.yPos+15)

    # turning back
    def turnBack(self,**d):
        self.lastExecutedMethod=self.turnBack
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm turning back"

        # not relevant for attention

        self.xPos=self.xPos0+random.random()*30-10
        self.setx(self.xPos)
        self.yPos=self.yPos0+random.random()*30-10
        self.sety(self.yPos)

    # move to teacher desk
    def moveToTeacherDesk(self,**d):
        self.lastExecutedMethod=self.moveToTeacherDesk
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "going to teacher desk"

        # not relevant for attention

        self.xPos=200+random.random()*10-5
        self.setx(self.xPos)
        self.yPos=-75+random.random()*10-5
        self.sety(self.yPos)

    # move to blackboard
    def moveToBlackboard(self,**d):
        self.lastExecutedMethod=self.moveToBlackboard
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "going to blackboard"

        # not relevant for attention

        self.xPos=40+random.random()*10-5
        self.setx(self.xPos)
        self.yPos=-125+random.random()*10-5
        self.sety(self.yPos)

    # doing desk
    def doDesk(self,**d):
        self.lastExecutedMethod=self.doDesk
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm doing desk"

        # not relevant for attention

        self.write("Do desk", font=("Arial", 14)) # turtle action

    # doing work
    def doWork(self,**d):
        self.lastExecutedMethod=self.doWork
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm doing work"

        # not relevant for attention

        self.write("Work", font=("Arial", 14)) # turtle action

    # doing metacognition
    def metaCognition(self,**d):
        self.lastExecutedMethod=self.metaCognition
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm doing metacognition!"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention

        self.write("meta", font=("Arial", 14)) # turtle action




    # talking
    def talk(self,**d):
        self.lastExecutedMethod=self.talk
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking"
        add=0.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("blah blah", font=("Arial", 14)) # turtle action

    # talking to teacher well
    def talkTeacherWell(self,**d):
        self.lastExecutedMethod=self.talkTeacherWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking to the teacher well"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("ok", font=("Arial", 14)) # turtle action

    # talking to teacher bad
    def talkTeacherBad(self,**d):
        self.lastExecutedMethod=self.talkTeacherBad
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking to the teacher bad"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("gulp", font=("Arial", 14)) # turtle action

    # talking to teacher not well
    def talkTeacherNotWell(self,**d):
        self.lastExecutedMethod=self.talkTeacherNotWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking to the teacher not well"
        add=0.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("not ok", font=("Arial", 14)) # turtle action

    # talking to teacher wrong
    def talkTeacherWrong(self,**d):
        self.lastExecutedMethod=self.talkTeacherWrong
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking to the teacher wrong"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("bleah", font=("Arial", 14)) # turtle action

    # checking Teacher and Talking closely
    def checkTeacherTalkClose(self,**d):
        self.lastExecutedMethod=self.checkTeacherTalkClose
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking teacher and talking closely"
        if self.agType == "greenPupil":
            add=random.random()*0.2+0.4
        else: add=random.random()*0.2+0.3
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("spy, pss pss", font=("Arial", 12)) # turtle action



    # talking closely
    def talkClose(self,**d):
        self.lastExecutedMethod=self.talkClose
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm talking closely"
        if self.agType == "greenPupil":
            add=random.random()*0.3+0.6
        else: add=random.random()*0.4+0.4
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("pss pss", font=("Arial", 12)) # turtle action



    # answering (well)
    def answerWell(self,**d):
        self.lastExecutedMethod=self.answerWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "answering well"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("answ ok", font=("Arial", 14)) # turtle answ

    # answering (bad)
    def answerBad(self,**d):
        self.lastExecutedMethod=self.answerBad
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "answering bad"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("answ gulp", font=("Arial", 14)) # turtle answ

    # answering (not well)
    def answerNotWell(self,**d):
        self.lastExecutedMethod=self.answerNotWell
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "answering not well"
        add=0.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("answ not ok", font=("Arial", 14)) # turtle answ

    # answering (wrong)
    def answerWrong(self,**d):
        self.lastExecutedMethod=self.answerWrong
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "answering wrong"
        add=1.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("answ bleah", font=("Arial", 14)) # turtle answ

    # answering Chorus
    def answerChorus(self,**d):
        self.lastExecutedMethod=self.answerChorus
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm answering chorus"
        add=0.0
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("Chorus", font=("Arial", 14)) # turtle action

    # ask repeat
    def askRepeat(self,**d):
        self.lastExecutedMethod=self.askRepeat
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm asking repeat"

        # not relevant for attention

        self.write("Repeat", font=("Arial", 14)) # turtle action



    # tidying
    def tidy(self,**d):
        self.lastExecutedMethod=self.tidy
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm tidying"
        add=random.random()*0.2+0.7
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("Tidy", font=("Arial", 12)) # turtle action


    # untidying
    def untidy(self,**d):
        self.lastExecutedMethod=self.untidy
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm untidying"
        add=random.random()*0.2+0.7
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("Untidy", font=("Arial", 12)) # turtle action


    # untidying-tidying
    def untidyTidy(self,**d):
        self.lastExecutedMethod=self.untidyTidy
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm untidying tidying"
        add=random.random()*0.2+0.6
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("un-tidy", font=("Arial", 12)) # turtle action

    # borrowing
    def borrow(self,**d):
        self.lastExecutedMethod=self.borrow
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm borrowing"
        add=random.random()*0.2+0.7
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("Borrow", font=("Arial", 12)) # turtle action


    # wellness
    def wellness(self,**d):
        self.lastExecutedMethod=self.wellness
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "Wellness"
        add=random.random()*0.2+0.7
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.xPos+=random.random()*20-10
        self.setx(self.xPos)
        self.yPos+=random.random()*20-10
        self.sety(self.yPos)

        self.write("wellness", font=("Arial", 14)) # turtle action


    # being praised
    def bePraised(self,**d):
        self.lastExecutedMethod=self.bePraised
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm being praised"

        # not relevant for attention

        self.write("Good", font=("Arial", 14)) # turtle action


    # be quite bored
    def beQuiteBored(self,**d):
        self.lastExecutedMethod=self.beQuiteBored
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm quite bored"
        add=random.random()*0.2+0.6
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("uff", font=("Arial", 12)) # turtle action

    # being scolded
    def beScolded(self,**d):
        self.lastExecutedMethod=self.beScolded
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm being scolded"

        # not relevant for attention

        self.write("ohi ohi", font=("Arial", 14)) # turtle action

    # be very bored
    def beVeryBored(self,**d):
        self.lastExecutedMethod=self.beVeryBored
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm very bored"
        add=random.random()*0.2+0.3
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                         \
                             / self.nMethodsAttention


        self.write("ronf", font=("Arial", 12)) # turtle action





    # mumbling
    def mumble(self,**d):
        self.lastExecutedMethod=self.mumble
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm mumbling"

        # not relevant for attention

        self.write("mumble", font=("Arial", 14)) # turtle action

    # growling
    def growl(self,**d):
        self.lastExecutedMethod=self.growl
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm growling"
        if self.agType == "greenPupil":
            add=random.random()*0.2+0.5
        else: add=random.random()*0.2+0.4
        self.nMethodsAttention+=1
        self.tickAttention = (self.tickAttention*(self.nMethodsAttention-1) \
                             + add)                                 \
                             / self.nMethodsAttention

        self.write("Growl", font=("Arial", 14)) # turtle action

    # teasing
    def tease(self,**d):
        self.lastExecutedMethod=self.tease
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm teasing"

        # not relevant for attention

        self.write("ihihih", font=("Arial", 14)) # turtle action


    # helping classmate
    def helpClassmate(self,**d):
        self.lastExecutedMethod=self.helpClassmate
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm helping you"

        # not relevant for attention

        self.write("SOS", font=("Arial", 14)) # turtle action




    # checking teacher
    def checkTeacher(self,**d):
        self.lastExecutedMethod=self.checkTeacher
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking teacher"

        # not relevant for attention

        self.write("spy teacher", font=("Arial", 14)) # turtle action



    # checking classmate work
    def checkClassmateWork(self,**d):
        self.lastExecutedMethod=self.checkClassmateWork
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking classmate work"

        # not relevant for attention

        self.write("spy work", font=("Arial", 14)) # turtle action



    # checking work
    def checkWork(self,**d):
        self.lastExecutedMethod=self.checkWork
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking work"

        # not relevant for attention

        self.write("check work", font=("Arial", 14)) # turtle action


    # checking fast work
    def checkFastWork(self,**d):
        self.lastExecutedMethod=self.checkFastWork
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking fast work"

        # not relevant for attention

        self.write("check fast work", font=("Arial", 14)) # turtle action


    # checking learning
    def checkLearning(self,**d):
        self.lastExecutedMethod=self.checkLearning
        print "I'm %s agent %d: " % (self.agType,self.number),
        print "I'm checking learning"

        # not relevant for attention

        self.write("Do I Know?", font=("Arial", 14)) # turtle action




    # conditional (maybe mirroring) actions

    # shake if
    def shakeIf_greenPupil(self,**d):
        self.lastExecutedMethod=self.shakeIf_greenPupil
        count=0
        for a in self.agentList:
            #print a.number, a.getLastExecutedMethod(), a.containers
            found=str(a.getLastExecutedMethod()).find('shake')
            #print found
            # -1 means 'not found'
            if found > -1 and 'greenPupil' in a.containers\
               and a.number != self.number: count+=1
        #print "*** ",count
        if count>0: self.shake()

    # chorus if
    def chorusIf_all(self,**d):
        self.lastExecutedMethod=self.chorusIf_all
        count=0
        for a in self.agentList:
            #print a.number, a.getLastExecutedMethod(), a.containers
            found=str(a.getLastExecutedMethod()).find('answerWell')
            #print found
            if found > -1 and 'all' in a.containers\
               and a.number != self.number: count+=1
        #print "*** ",count
        if count>0: self.answerChorus()
