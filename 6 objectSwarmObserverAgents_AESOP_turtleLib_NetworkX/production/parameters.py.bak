#parameters.py
from Tools import *
import commonVar as common

import networkx as nx
import matplotlib as mplt

def loadParameters(self):

  print "NetworkX version %s running" % nx.__version__
  print "Matplotlib version %s running\n" % mplt.__version__


  nxv=nx.__version__.split('.')
  vOK=False
  if int(nxv[0])>1: vOK=True
  if len(nxv)>=2:
      if int(nxv[0])==1 and int(nxv[1])>9: vOK=True
  if len(nxv)>=3:
      if int(nxv[0])==1 and int(nxv[1])==9 and int(nxv[2])>=1: vOK=True

  if not vOK:
		print "NetworkX 1.9.1 or greater required"
		os.sys.exit(1)


  mpltv=mplt.__version__.split('.')
  vOK=False
  if int(mpltv[0])>1: vOK=True
  if len(mpltv)>=2:
      if int(mpltv[0])==1 and int(mpltv[1])>5: vOK=True
  if len(mpltv)>=3:
      if int(mpltv[0])==1 and int(mpltv[1])==5 and int(mpltv[2])>=1: vOK=True

  if not vOK:
		print "Matplotlib 1.5.1 or greater required"
		os.sys.exit(1)

  mySeed = input("random number seed (1 to get it from the clock) ")
  if mySeed == 1:
        random.seed()
  else:
        random.seed(mySeed)

  self.nAgents = 0
  print "No 'bland' agents"

  #self.worldXSize= input("X size of the world? ")
  self.worldXSize=1
  print "X size of the world not relevant"

  #self.worldYSize= input("Y size of the world? ")
  self.worldYSize=50
  print "y size of the world not relevant"

  #recipes
  common.maxLenght=10
  common.maxSector=6
  print "recipes: max lenght", common.maxLenght, "and max sector number", common.maxSector


  self.nCycles = input("How many cycles? (0 = exit) ")

  v = raw_input("verbose? (y/[n]) ")
  if v=="y" or v=="Y":
    common.verbose=True #predefined False
