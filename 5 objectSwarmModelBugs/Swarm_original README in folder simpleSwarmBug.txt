// simpleSwarmBug

                   ADDING A SWARM

main.m

In this next version of the program, we create a special
object called a "Swarm" to take care of creating and
managing the other objects, the "bug" agent and the
"foodSpace" world.

This object isn't really part of the bug's world, it is
more an object in our world - it encapsulates our "model"
of the bug and its world, making the model itself a kind
of "thing" that we can interact with by sending it messages
and asking it to do things.

For a typical Swarm simulation, in main.m you create a toplevel
Swarm, which will manage the tasks of creating, running and
interacting with our models.  As we don't know, or care really,
at this level what the model is, we have a regular procedure
for constructing almost any ModelSwarm - in fact almost
any Swarm - that is independent of the model specifics.

Thus, all of the model particular details have been removed
from main.m, and encapsulated in a model object called
a "modelSwarm". Here in main, as before, we create and
send messages to the this model object, much as we
did for the bug and foodspace objects.

However, a Swarm is a special kind of object. It is likely
to have a number of objects in it, the objects that
constitute the various "actors" and "agents" in our models.
And, it manages the execution of the objects it contains via
another special class of objects called "Activities".

Activities are essentially "lists" of messages to be sent
to objects. A Swarm owns a collection of objects and a
collection of schedules of events over them.

The details are in the files ModelSwarm.h and ModelSwarm.m

Here, we simply create the modelSwarm, tell it to build
its objects and its activities, bind them up together,
and start them going.



ModelSwarm.h and ModelSwarm.m

This Model Object is now where the details of the particular
model we are running are hidden away from other things that
don't want, or need, to know about them. We can alter things
in our model without having to disturb other components of
our whole experiment/simulation.

What we do here is three things.

First we construct the various objects in the model, as we
did before in main.m.
This takes place in the "buildObjects" method.

Second, we arrange for messages to be sent to the objects in
the right order, but not via for-loops. Rather we create
passive data-structures containing the messages we want sent -
or some of them anyway - the ones we know about now.
This takes place in the "buildActions" method code.

Third, as we may have created a number of such passive message-holding
data-structures, we arrange for them all to be glued together, and
we allow the structures we have constructed to be glued together
with other structures constructed elsewhere.
This takes place in the "activateIn" method code.

We don't actually "start" the model going here - we build it, schedule
its parts, and get those schedules glued together with other schedules
that might exist out there in the world that we have to interact with.
Something else will actually do the traversing of those structures,
sending out the messages they encounter as they traverse over them.


The first method we encounter in ModelSwarm is +createBegin. Note the
"+" in front - that signifies that it is different from the "normal"
methods preceeded by "-" symbols. 

+createBegin is a special method - it specifies how an instance
of a modelSwarm is to be created. It doesn't really belong to
a created modelSwarm, because it gets called to create an
instance of a modelSwarm in the first place, so there's no
instance "here" yet when this method gets called.

Effectively, it is a "Class" method, rather than an "Instance"
method. It is stuff that, for all intents and purposes, the
class has to do to bring an instance into existence. Something
has to, but it can't be something which doesn't exist yet!

-createEnd is a place to do any last minute tidying up after
the creator is done - via more normal modes of operation
However, we don't do anything here - except allow our
super-class to clean up if it wants to....

-buildObjects is where we construct the objects in 
the model. This is just what we did previously in
main.m. 

-buildActions 

Here, we construct a data structure which holds messages that we 
know we will want to send in the future, and in the proper order.  
A Schedule is an object that manages our messages for us, allowing 
us to treat the set of events in the world as a kind of "thing", which 
we can interact with via requesting it to do things and give us 
information.

There is a tremendous potential in being able to treat something as 
abstract as a collection of events as a "thing", but we'll get into 
that later.

 Here, we just construct a simple schedule in which we just repeatedly 
send the step message to the bug.  Setting RepeatInterval to 1 ensures 
that this action will happen over and over again for ever, or until
you hit Ctrl-C, whichever comes first. We'll get into termination 
conditions later, and in other apps and tutorials.

-activateIn    

Here is where we arrange for the schedule we built, and in fact 
for the modelSwarm itself to be glued together with whatever other 
schedules have been built above, below, or beside us....
To Activate is to glue a schedule or swarm onto other existing 
schedules or swarms in preparation for traversal by the activity
objects who manage to maintain all this potential chaos of concurrency 
and hierarchy in order.

Here, we activate the swarm in a context that's been passed into us, 
and we provide the context for the schedule we built above in buildActions.

In turn, we return our glued together activity structure to whoever 
called us, so we can get connected to structures that they know about.



Bug.h, Bug.m, FoodSpace.h, and FoodSpace.h

These have not been affected by the move objectify the model.
They get created and manipulated just as before, although
something different is manipulating them.



Makefile

The new ModelSwarm object adds another binary to be linked and
dependencies to be established.




NEXT -> simpleSwarmBug2


