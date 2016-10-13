// SimpleCBug

                FROM C TO OBJECTIVE-C

main.m

This is an object-oriented version of the simpleCBug program.
The code for the "bug" has been encapsulated in an "object",
defined in the two files Bug.h and Bug.m.

main.m has new code to "create" a bug, to set its internal
state, and to tell it to execute  - to "do its thing" over
and over again. We communicate with the "bug" by sending
it "messages", using the following syntax:

             [aBug setX: xPos Y: yPos];

is a command to send the object "aBug" the message:

     `set your X and Y coords to xPos and yPos'

The message [Bug create: globalZone] is asking the Bug "Class"
to give us an instance of a Bug, which we thereafter refer to
as "aBug". The message [aBug step] is asking the object "aBug"
to perform it's major action, taking a random walk - but the 
code for doing so is hidden from us here. We just ask it to 
"do its thing", and it does it, whatever it is.



Bug.h and Bug.m

The objects are implemented in two files each. The "Interface"
and the "Implementation" files (".h" and ".m" files, respectively.) 

The ".h" files declare what internal variables an object has and 
what messages it will respond to.  They are called "interface" files, 
because they declare *what* the object will do, without stating *how* 
they will do it. In principle, nobody should care how the object does 
what it does, they only need to know what it does. 

The ".m" files are where one specifies *how* the object will respond 
to the messages defined on it. In principle, nobody needs to know about 
*how* except the people who have to implement it somehow.

In this case, the "bug" object has four internal variables: xPos,
yPos, worldXSize, and worldYSize. It has three different types
of messages that it will respond to: setX:Y:, setWorldSizeX:Y:, and
step. All of the parts followed by colons (:) are considered to
be part of the message name, while the bits in between (x and y here)
are the arguments carried along by the messages. 

Thus, on the basis of looking at the Bug.h file, we can tell that 
this Bug object can be asked to set its X and Y coordinates
to specific values and to set its idea of how big its "world" is.
It also can be asked to "do its thing" - whatever that is, by
sending it the "step" message,

By looking at the Bug.m file, we can see how it does what it
does. The "methods" that are implemented here are pretty
much just what was done in main.m before, just seen from the other
side of the object "mirror".  Thus we set X and Y coords, fix
the size of the world, and take a step in a random walk.



Makefile

Here, we have two binaries to be linked: Bug.o and main.o, and
the linkage and recompilation dependencies are as shown.



NEXT -> simpleObjCBug2
