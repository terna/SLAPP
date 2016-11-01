# start 4 basicObjectProgrammingManyBugs_bugExternal_+_shuffle
import Bug
import random

nBugs = input("How many bugs? ")
bugList = []
worldXSize= input("X Size of the world? ")
worldYSize= input("Y Size of the world? ")
length = input("Length of the simulation in cycles? ")


for i in range(nBugs):
    aBug = Bug.Bug(i, random.randint(0,worldXSize-1), \
                            random.randint(0,worldYSize-1), \
                            worldXSize, worldYSize)
    bugList.append(aBug)

for t in range(length):

    random.shuffle(bugList)
    
    for aBug in bugList:
        aBug.randomWalk()
        aBug.reportPosition()
