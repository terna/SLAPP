#start 1 plainProgrammingBug.py
import random

def SimpleBug():

    # the environment
    worldXSize = 80
    worldYSize = 80

    # the bug
    xPos = 40
    yPos = 40

    # the action
    for i in range(100):
        xPos += randomMove()
        yPos += randomMove()
        xPos = (xPos + worldXSize) % worldXSize
        yPos = (yPos + worldYSize) % worldYSize
        print "I moved to X = ", xPos, " Y = ", yPos

# returns -1, 0, 1  with equal probability
def randomMove():
    return random.randint(-1, 1)

SimpleBug()

"""
you can eliminate the randomMove() function substituting
        xPos += randomMove()
        yPos += randomMove()
with
        xPos += random.randint(-1, 1)
        yPos += random.randint(-1, 1)

but the use of the function allows us to use here a self-explanatory
name
"""
