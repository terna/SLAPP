#start 5 objectSwarmModelBugs.py
from Tools import *
from ModelSwarm import *

nBugs = eval(input("How many bugs? "))
worldXSize= eval(input("X Size of the world? "))
worldYSize= eval(input("Y Size of the world? "))
nCycles = eval(input("How many cycles? (0 = exit) "))

modelSwarm = ModelSwarm(nBugs, nCycles, worldXSize, worldYSize)

# create objects
modelSwarm.buildObjects()

# create actions
modelSwarm.buildActions()

# run
modelSwarm.run()

print()
print("Simulation stopped after ", nCycles, " cycles")
