import sys
import os
import commonVar as common

common.graphicStatus=""

def checkRunningIn():
    try:
        __IPYTHON__
        return True
    except NameError:
        return False


def graphicControl():
 # IPython/Python
 IPython = checkRunningIn()

 # running in Python (not in IPython)
 if not IPython:

  # at http://matplotlib.org/users/shell.html
  # we read "the python IDLE IDE is a Tkinter gui app that does not
  # support pylab interactive mode, regardless of backend"

  if 'idlelib' in sys.modules:
     print(
     'Running in IDLE, please start SLAPP using a terminal with\n'+
     'python runShell.py\nexecuted being in SLAPP main folder')
     os.sys.exit(1)

  elif 'spyderlib' in sys.modules:
     print(
     'Running in Spyder, please start SLAPP using a terminal with\n'+
     'python runShell.py\nexecuted being in SLAPP main folder')
     os.sys.exit(1)

  else:
      common.graphicStatus="PythonViaTerminal"
      print 'SLAPP started from a terminal'


 # running in IPython
 if IPython:
  from IPython import get_ipython
  import matplotlib
  matplotlib.use("TkAgg")
  import matplotlib as mpl
  import matplotlib.pyplot as plt

  # check if running in a plain terminal with IPython starting with the
  # 'ipython' command line OR in a jupyter notebook


  # IN 'ipython' command line in a terminal, but the case of using it via
  # Spyder, which is behaving as a Jupyter QtConsole (see below)
  if "IPython.terminal.interactiveshell.TerminalInteractiveShell" \
   in str(get_ipython()):

   common.graphicStatus="PythonViaTerminal"
   print 'SLAPP started from a terminal'


  # IN a jupyter notebook OR in a Jupyter QtConsole (same effects)
  if "zmqshell.ZMQInteractiveShell" \
   in str(get_ipython()):

   # running in IPython with magic '%matplotlib|%pylab' already set,
   # modified to '%matplotlib inline'
   if get_ipython().config.has_key('InlineBackendConfig') and \
      not "backend_inline" in mpl.get_backend():
      print "SLAPP running with magic '%matplotlib|%pylab' already set"

      get_ipython().magic("%matplotlib inline")
      print "'%matplotlib inline' magic command NOW SET"
      common.graphicStatus="%matplotlib inline"

   # running in IPython with magic '%matplotlib inline|%pylab' already set
   elif get_ipython().config.has_key('InlineBackendConfig') and \
      "backend_inline" in mpl.get_backend():
      print "running with magic '%matplotlib inline|%pylab inline' already set"
      common.graphicStatus="%matplotlib inline"

   # running in IPython without any magic matplotlib already set
   else:
      print "SLAPP starting without any matplotlib magic command"

      get_ipython().magic("%matplotlib inline")

      print "'%matplotlib inline' magic command NOW SET"
      common.graphicStatus="%matplotlib inline"

  # size of the pictures within an IPython notebook
  width=12
  height=8
  try: width=common.width
  except: pass
  try: height=common.height
  except: pass
  plt.rcParams['figure.figsize'] = width, height  #in inches, but ... on paper
                                                  #and on the screen the effect is
                                                  #related to the screen
                                                  #and printer pixel density
                                                  #suggested ratio 3/2


if __name__=="__main__": graphicControl()
