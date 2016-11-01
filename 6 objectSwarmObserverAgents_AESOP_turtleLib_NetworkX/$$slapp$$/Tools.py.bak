import random
import os
import commonVar as common
import inspect

"""
A memo from
http://www.devshed.com/c/a/Python/Python-Parameters-Functions-and-Arguments/
At the end of the parameters, you may optionally use either or both
of the special forms *identifier1 and **identifier2 .
If both forms are present, the form with two asterisks must
be last. *identifier1 specifies that any call to the function may
supply any number of extra positional arguments, while **identifier2
specifies that any call to the function may supply any number of
extra named arguments (positional and named arguments are covered
in "Calling Functions" on page 73). Every call to the function
binds identifier1  to a tuple whose items are the extra positional
arguments (or the empty tuple, if there are none). Similarly,
identifier2  gets bound to a dictionary whose items are the names
and values of the extra named arguments (or the empty dictionary,
if there are none).
"""

# two functions to apply different ways of writing method in the call of the
# run a method over an instance

# extract the method from the unbound method m
def extractMethod(m):
  # about python 3 and im_class, see paragraph A.28 at
  # http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html
  name=""
  c=m.im_class                      # class of m
  while name != 'object':
   dk=c.__dict__.keys()             # keys   in the dict of c
   dv=c.__dict__.values()           # values in the dict of c
   f=m.__func__                     # the implicit func of m
   try:
        method=dk[dv.index(f)]      # the key of the value==f
        name='object'               # to leave while
   except:
        c=c.__bases__[0]            # moving to super class
        name=c.__name__             # it top recursion, name contains
                                    # 'object'as our SuperAgent inherits
                                    # from object
  return method


# run a method over an instance
def applyMethod(instance,method,**k):
  # NB, the call of this function can be included in a try/except
  # strucutre to catch the cases of invalid dotted couples
  # class.method

  # we wrote the method in the 'unbound method' way (accepted for
  # compatibility with versions < 1.36), mainly using the generic
  # class Agent, maybe to be substituted by the class of the instance
  if inspect.ismethod(method):
     # unbound method case, extract method in str format
     method = extractMethod(method)

  # we wrote the method as a str (preferred way from v.1.36)
  if not type(method) is str:
    print method,"is neither an unbound method nor a string"
    return False
  else:
    # method is an str
    # find the class of the instance
    c=instance.__class__
    # check if that class has the method 'method'
    try:exec("test=inspect.ismethod(c."+method+")")
    except: test=False
    if test:
      exec("result=c."+method+"(instance,**k)")
      return result
    else:
      print "Warning, class", c.__name__, "(or above) of agent", \
             instance.agType, "does not have the method", method
      return False


# dictionary of the action groups (not necessary, kept only for
# retro compatibility)
actionDictionary={}


# applying a method to a collection of instances
def askEachAgentInCollection(collection,method,**k):
    """ collection, method, dict. of the parameters (may be empty)"""

    for a in collection:
            if common.debug: applyMethod(a,method,**k)
            else:
             try:
                applyMethod(a,method,**k)
             except:
              print 'cannot apply (case 0) method', method,\
                    'to agent number', a.number, 'of type ',a.agType
              # very special case
              if a.agType=="recipes": print "first step", a.content[0]
              pass
            # if we use k (a dictionary), the same notation has to
            # be placed into the agent methods

# applying a method to a collection of instances
def askEachAgentInCollectionAndExecLocalCode(collection,method,**k):
    """ collection, method, dict. of the parameters (may be empty)"""

    setLocalCode("")

    for a in collection:
            if common.debug: applyMethod(a,method,**k)
            else:
             try: applyMethod(a,method,**k)
             except:
              print 'cannot apply (case 1) method', method,\
                    'to agent number', a.number, 'of type ',a.agType
              pass
            # if we use k (a dictionary), the same notation has to
            # be placed into the agent methods

            execLocalCode()



# applying a method to an instance of a class
def askAgent(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    if common.debug: applyMethod(agent,method,**k)
    else:
     try: applyMethod(agent,method,**k)
     except:
        print 'cannot apply (case 2) method', method, 'to agent number', \
              a.number
        pass

# applying a method to an instance of a class
def askAgentAndExecLocalCode(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    setLocalCode("")

    if common.debug: applyMethod(agent,method,**k)
    else:
     try: applyMethod(agent,method,**k)
     except:
        print 'cannot apply (case 3) method', method, 'to agent number', \
              a.number
        pass

    execLocalCode()



# extracting a step and rotating a list (obsolete)
"""
def extractAStepAndRotate(aList):
        if len(aList)==0:
            print "Error: action list is empty"
            os.sys.exit(1)

        aSubList=aList.pop(0)
        if type(aSubList)!=list:
            print "Error: the elements of the action list need to be a list"
            os.sys.exit(1)
        aList.append(aSubList)

        return aSubList[:] # with [:] we return the elements
                           # of aSubList, not the address
"""

# extracting a subStep
def extractASubStep(aSubList):
        if len(aSubList)>0: return aSubList.pop(0)
        else: return []

# insert an element in next position
def insertElementNextPosition(aList,what):
    aList.insert(0,what)


# exec("instruction 1; instruction 2; ...")
# pay attention to the semicolon
def execLocalCode():
      global localCode
      exec(localCode)
      cleanLocalCode()

def cleanLocalCode():
      global localCode
      localCode=""

def getLocalCode():
      global localCode
      return localCode

def setLocalCode(code):
      global localCode
      localCode=code

def checkRunningIn():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
