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

# two functions to apply different ways of writing the methods to run
# them as applied to an instance or to a set of instances

# extract the method from m (in Python3 m is a function); formerly it
# was an unbound method (see the from2to3.md file in the main folder)
# m is in the form Class.method
def extractMethodFromMethodFunction(m):

     # m is Class.method; the method can also be defined in a super class
     # NB if m is not a valid Class.method combination, Python raises an error
     # so, we have to include the call to this funcion in a
     # try/except structure

     # class (or super class) name and class address are not necessary, but just in case ...
     #cName=m.__qualname__.split(".")[0] # name of the class that defined the
                                         # method reported in m (that contains 'class.method')
     #print (cName)

     #c=m.__globals__[cName] # class address
     #print (c)

     mName=m.__qualname__.split(".")[1] # name of the method (naked)
     #print (mName)
     return mName


# run a method over an instance
def applyMethod(instance,method,**k):
  # NB, the call of this function can be included in a try/except
  # strucutre to catch the case of an invalid dotted pair
  # class.method

  #handmade changes from Py 2 to Py 3

  # we use extractMethodFromMethodFunction because we have to align to
  # the need of writing methods as strings of characters, when we extract
  # the content of the script of the schedule (.txt or .xls)


  try:
   if inspect.isfunction(method):
   # unbound method/function case, extract method/function in str format
     method = extractMethodFromMethodFunction(method)
  except:
     pass

  # we wrote the method as a str (preferred way from v.1.36)
  if not type(method) is str:
    print(method,"is neither an unbound method nor a string")
    return False
  else:
    # method is a str
    # find the class of the instance
    c=instance.__class__
    # check if that class has the method 'method'
    space={}
    space['c']=c
    space['inspect']=inspect
    test=False
    try:
        exec("test=inspect.isfunction(c."+method+")", space)
        test=space['test']
    except: pass
    if test:
      space['instance']=instance
      space['k']=k
      exec("result=c."+method+"(instance,**k)", space)
      result=space['result']
      return result
    else:
      print("Warning, class", c.__name__, "(or above) of agent", \
             instance.agType, "does not have the method", method)
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
              print('cannot apply (case 0) method', method,\
                    'to agent number', a.number, 'of type ',a.agType)
              # very special case
              if a.agType=="recipes": print("first step", a.content[0])
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
              print('cannot apply (case 1) method', method,\
                    'to agent number', a.number, 'of type ',a.agType)
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
        print('cannot apply (case 2) method', method, 'to agent number', \
              a.number)
        pass

# applying a method to an instance of a class
def askAgentAndExecLocalCode(agent,method,**k):
    """ agent, method, dict. of the parameters (may be empty)"""
    setLocalCode("")

    if common.debug: applyMethod(agent,method,**k)
    else:
     try: applyMethod(agent,method,**k)
     except:
        print('cannot apply (case 3) method', method, 'to agent number', \
              a.number)
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

def checkVersion(version,name,k0,k1,k2):
      # managing the presence of strings as rc in the version components
      vv=version.split('.')
      try: v0 = int(vv[0])
      except:
              try: v0 = int(vv[0][0:2])
              except:
                  try: v0 = int(vv[0][0:1])
                  except:
                      print("error in lib",name,"not regular version number")
                      os.sys.exit(1)
      if v0>k0: return True

      if len(vv)>=2:
          try: v1 = int(vv[1])
          except:
              try: v1 = int(vv[1][0:2])
              except:
                  try: v1 = int(vv[1][0:1])
                  except:
                      print("error in lib",name,"not regular version number")
                      os.sys.exit(1)
          if v0==k0 and v1>k1: return True

      if len(vv)>=3:
          try: v2 = int(vv[2])
          except:
             try: v2 = int(vv[2][0:2])
             except:
                 try: v2 = int(vv[2][0:1])
                 except:
                     print("error in lib",name,"not regular version number")
                     os.sys.exit(1)
          if v0==k0 and v1==k1 and v2>=k2: return True

      # the sequence never succeded
      return False
