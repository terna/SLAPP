#matplotlib_aQuestForAFewGraphicCapabilities.py (April 2016)
import time
import sys
import os

import matplotlib as mpl
print "Matplotlib version %s running\n" % mpl.__version__
# controlling the version
vMpl=mpl.__version__.split('.')
vOK=False
if int(vMpl[0])>1: vOK=True
if len(vMpl)>=2:
      if int(vMpl[0])==1 and int(vMpl[1])>5: vOK=True
if len(vMpl)>=3:
      if int(vMpl[0])==1 and int(vMpl[1])==5 and int(vMpl[2])>=1: vOK=True
if not vOK:
      print "Matplotlib 1.5.1 or greater required"
      os.sys.exit(1)

print "This 'quest' is related to the file running in IDLE/Spyder(as Python)"+\
      " or in a plain terminal running Python or in jupyter notebook\n"+\
      "SLAPP instead works also - with limitations - in a terminal running IPython\n"+\
      "(not in a terminal running 'jupyter console')"



def checkRunningIn():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False

IPython = checkRunningIn()




# running in IPython
if IPython:
 from IPython import get_ipython

 # running in IPython with magic '%matplotlib|%pylab' already set
 if get_ipython().config.has_key('InlineBackendConfig') and \
    not "backend_inline" in mpl.get_backend():
      print "running in IPython with magic '%matplotlib|%pylab' already set"
      graphicStatus="%matplotlib"

 # running in IPython with magic '%matplotlib inline|%pylab' already set
 elif get_ipython().config.has_key('InlineBackendConfig') and \
    "backend_inline" in mpl.get_backend():
      print "running in IPython with magic '%matplotlib inline|%pylab inline' already set"
      graphicStatus="%matplotlib inline"

 # running in IPython without any magic matplotlib already set
 else:
  print "running in IPython without any matplotlib magic command already set"
  n=input("Your choice: 1. continue without magic matplotlib [output with plt.show()];"+\
          "\n             2. add '%matplotlib' magic command;"+\
          "\n             3. add '%matplotlib inline' magic command:\n")

  if n == 1:
      graphicStatus="IPythonNoMagic"

  if n == 2:
      get_ipython().magic("%matplotlib")
      # alternatively it would be possible to run a .ipy file
      # from jupiter; in this kind of files it is possible to
      # write magic commands in regular way, as: %matplotlib
      graphicStatus="%matplotlib"


  if n == 3:
      from IPython import get_ipython
      get_ipython().magic("%matplotlib inline")
      graphicStatus="%matplotlib inline"




# running in Python (not in IPython)
if not IPython:

 graphicStatus="PythonViaTerminal"

 # at http://matplotlib.org/users/shell.html
 # we read "the python IDLE IDE is a Tkinter gui app that does not
 # support pylab interactive mode, regardless of backend"

 if 'idlelib' in sys.modules:
     print(
     'Running in IDLE, with the possibility of improperly functioning graphics')
     graphicStatus="PythonViaIDLEorSpyder"
 if 'spyderlib' in sys.modules:
     print(
     'Running in Spyder, with the possibility of improperly functioning graphics')
     graphicStatus="PythonViaIDLEorSpyder"





#########################################
# outputs
n=" "
while n != "1" and n != "2": n = raw_input(\
                            "1 for simple check; 2 for complex check ")




#########################################
# simple (built with a mixed stucture)
if n == "1":
 import matplotlib.pyplot as plt

 ### experimenting the results in a simple way

 # sys.stdout.write() to allow sys.stdout.flush() generating the output
 if graphicStatus=="PythonViaIDLEorSpyder" or graphicStatus=="IPythonNoMagic":
    sys.stdout.write( \
    "WARNING: please shutdown the graphic window hitting the close mark.")
    sys.stdout.flush()

 if graphicStatus=="%matplotlib" or graphicStatus=="PythonViaTerminal":
    print \
    "WARNING: please shutdown the graphic window with plt.close() or concluding the program."

 if graphicStatus=="PythonViaTerminal":   plt.ion()

 plt.plot([4,2,1,5,-1])

 plt.show() # this instruction is strictly necessary if
 # graphicStatus=="PythonViaIDLEorSpyder" or graphicStatus=="IPythonNoMagic" or
 # in case %matplolib inline" set from jupyter shell, not internally via
 # get_ipython().magic("%matplotlib inline")
 # it does not create any problem in the other cases

 if graphicStatus=="%matplotlib inline" or graphicStatus=="PythonViaTerminal":
  raw_input("Enter to finish") # with "PythonViaIDLEorSpyder" or "IPythonNoMagic"
                               # this is a duplication of the closing operation
                               # that we make hitting the close mark of the graphic
                               # window

                               # with "PythonViaTerminal" it works as a wait (very
                               # useful for SLAPP)

                               # with "matplotlib" this waiting status leaves the cell
                               # unfinished, so producing a white graphic window

                               # with "matplotlib inline" it works as a wait (very
                               # useful for SLAPP)


 if graphicStatus=="PythonViaTerminal":
  plt.close()

#########################################
# complex (built in separated segments)
if n == "2":

 def setAttr(x,y,title):
       #x and y are integer numbers; title a string
       mngr=plt.get_current_fig_manager()
       mngr.window.wm_geometry("+"+str(x)+"+"+str(y))
       mngr.set_window_title(title)

 #----------------------------------------
 # running in a Python IDE (recognized: IDLE or Spyder)
 if graphicStatus=="PythonViaIDLEorSpyder":
  mpl.use("TKAgg")
  import matplotlib.pyplot as plt

  #sys.stdout.write\
  # ("\nWARNING: please shutdown the graphic window hitting the close mark.")
  #sys.stdout.flush()

  print "\nWARNING: please shutdown the graphic window hitting the close mark."

  plt.figure(1)
  setAttr(0,0,"One")
  plt.plot([1,2,4])

  plt.figure(2)
  setAttr(650,0,"Two")
  plt.plot([4,2,1])

  plt.show()

  print "\nWARNING: again, shutdown the graphic window hitting the close mark."

  plt.figure(1)
  setAttr(0,0,"One") # to be repeated after a close
  plt.plot([10,2,40])

  plt.figure(2)
  setAttr(650,0,"Two")
  plt.plot([40,2,10])

  plt.show()



 #----------------------------------------
 # running in a Python terminal
 elif graphicStatus=="PythonViaTerminal":
  mpl.use("TKAgg")
  import matplotlib.pyplot as plt

  plt.ion()

  plt.figure(1)
  setAttr(0,0,"One")
  plt.plot([1,2,4])

  plt.figure(2)
  setAttr(650,0,"Two")
  plt.plot([4,2,1])

  raw_input("Enter to continue")

  plt.figure(1)
  plt.clf() # to clean the figure; commenting, the two plots are reported
  plt.plot([10,2,40])

  plt.figure(2)
  plt.clf()
  plt.plot([40,2,10])

  raw_input("Enter to shutdown the graphic windows")

  plt.close()
  plt.close()

 #----------------------------------------
 # running in IPython without any magic matplotlib
 elif graphicStatus=="IPythonNoMagic":
  mpl.use("TKAgg")
  import matplotlib.pyplot as plt

  sys.stdout.write\
   ("\nWARNING: please shutdown the graphic window hitting the close marks.")
  sys.stdout.flush()

  plt.figure(1)
  setAttr(0,0,"One")
  plt.plot([1,2,4])

  plt.figure(2)
  setAttr(650,0,"Two")
  plt.plot([4,2,1])
  plt.show()

  sys.stdout.write\
   ("\nWARNING: please shutdown the graphic window hitting the close marks.")
  sys.stdout.flush()

  plt.figure(1)
  setAttr(0,0,"One")
  plt.plot([10,2,40])

  plt.figure(2)
  setAttr(650,0,"Two")
  plt.plot([40,2,10])
  plt.show() # strictly necessary here



 #----------------------------------------
 # running in IPython with magic '%matplotlib|%pylab'
 # already set or '%matplotlib' set interactively
 elif graphicStatus=="%matplotlib":
  import matplotlib.pyplot as plt

  #plt.ion() # not necessary here

  # subplot command is documented at
  # http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
  # under 1.4.3.2. Subplots

  sys.stdout.write\
   ("\nWARNING: please shutdown the graphic window hitting the close marks.")
  sys.stdout.flush()

  plt.figure("One, Two")
  plt.subplot(2,1,1)
  plt.plot([1,2,4])

  plt.subplot(2,1,2)
  plt.plot([4,2,1])
  #raw_input("Enter") #this waiting status would leave the cell
                      # unfinished, so producing a white graphic window
  plt.show(block=True) # used to wait until the display is closed
                       # block=True is madatory here

  sys.stdout.write\
   ("\nWARNING: please shutdown the graphic window hitting the close marks.")
  sys.stdout.flush()

  plt.clf()
  plt.subplot(2,1,1)
  plt.plot([10,2,40])

  plt.subplot(2,1,2)
  plt.plot([40,2,10])
  #plt.show() # finishing the IPython cell, non strictly necessary
              # & not necessary here with ion()







 #----------------------------------------
 # running in IPython with magic '%matplotlib inline|%pylab inline'
 # already set or '%matplotlib' set interactively
 elif graphicStatus=="%matplotlib inline":
  import matplotlib.pyplot as plt

  #plt.ion() # disturbing here

  # subplot command is documented at
  # http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html
  # under 1.4.3.2. Subplots


  plt.figure("One, Two")
  plt.subplot(2,1,1)
  plt.plot([1,2,4])

  plt.subplot(2,1,2)
  plt.plot([4,2,1])
  plt.show() # strictly necessary here (to see this intermediate plot)

  raw_input("Enter to continue or to finish")

  #plt.figure("One, Two")
  plt.clf()
  plt.subplot(2,1,1)
  plt.plot([10,2,40])

  plt.subplot(2,1,2)
  plt.plot([40,2,10])
  plt.show() # necessary here (due to the following raw_input)

  raw_input("Enter to continue or to finish")





print "\nEnding trial!"


# a final memo about draw()
# http://stackoverflow.com/questions/23141452/difference-between-plt-draw-and-plt-show-in-matplotlib

# plt.show() will display the current figure that
# you are working on.
# plt.draw() will re-draw the figure. This allows you
# to work in interactive mode and, should you have changed
# your data or formatting, allow the graph itself to change.
