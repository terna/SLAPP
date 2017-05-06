#parameters.py
from Tools import *
import commonVar as common

import networkx as nx
import matplotlib as mplt

def loadParameters(self):

  print("NetworkX version %s running" % nx.__version__)
  print("Matplotlib version %s running\n" % mplt.__version__)


  nxv=nx.__version__
  vOK=checkVersion(nxv,'NetworkX',1,9,1)

  if not vOK:
      print("NetworkX 1.9.1 or greater required")
      os.sys.exit(1)


  mpltv=mplt.__version__
  vOK=checkVersion(mpltv,'Matplotlib',1,5,1)

  if not vOK:
      print("Matplotlib 1.5.1 or greater required")
      os.sys.exit(1)

  mySeed = eval(input("random number seed (1 to get it from the clock) "))
  if mySeed == 1:
        random.seed()
  else:
        random.seed(mySeed)

  self.nAgents = 0
  print("No 'bland' agents")

  #self.worldXSize= input("X size of the world? ")
  self.worldXSize=1
  print("X size of the world not relevant")

  #self.worldYSize= input("Y size of the world? ")
  self.worldYSize=50
  print("y size of the world not relevant")

  #recipes
  common.maxLenght=10
  common.maxSector=6
  print("recipes: max lenght", common.maxLenght, "and max sector number", common.maxSector)


  self.nCycles = eval(input("How many cycles? (0 = exit) "))

  v = input("verbose? (y/[n]) ")
  if v=="y" or v=="Y":
    common.verbose=True #predefined False
