// simpleObserverBug

EMBED THE MODEL SWARM IN AN OBSERVER SWARM, PROVIDING GRAPHICAL
                 VISUALIZATION AND INTERACTION

main.m

Now we are doing something different at the top level. We have been
using pretty crude I/O to observe the model's behavior. Now we will
build another Swarm to encapsulate a bunch of graphics observing
capability. We are once again encapsulating an aspect of our
interactions with models, in this case our observations of models, and
making a kind of "thing" out of them, that we can interact with in a
number of ways.

Furthermore, we now have a "hierarchy" of nested swarms. Objects can
clearly encapsulate other objects, and Swarms can encapsulate other
Swarms. Here the ObserverSwarm will take over the creation of the
ModelSwarm inside of itself, which in turn will create the bugs,
foodSpaces, and etc that are internal to it.

With nested hierarchies of Swarms, we also have nested hierarchies of
model execution, and, in general, Swarms can be arbitrarily deeply
embedded in such hierarchies. Furthermore, any one Swarm might be
nurturing a collection of subSwarms, each nurturing further subsets,
so one can have both deep and broad hierarchies of concurrently
executing "models" - all modelling different aspects of our
interactions with models, events, observations, and so forth.

Here, the ObserverSwarm takes over the responsibility of constructing
and managing the ModelSwarm, and provides us with numerous ways of
interacting with, and observing, the model.

The ModelSwarm doesn't have to change very much because it is now
being manipulated differently. However, it is useful to add a few
features to make observing easier.

Here in main.m, we now create a different kind of swarm. The Observer
Swarm will be a "GUISwarm" - a swarm that knows how to communicate
with a user via a terminal screen.

However, other than knowing that it is a GUISwarm, there's not much
different about the creation and initialization process here in main.m
that for the ModelSwarm.

The only exception is that a GUISwarm provides a graphical "controlPanel"
for the user - a kind of "dash-board" with "go", "stop", "step",
and "quit" buttons on it that can be used to start and stop the
activities that run Swarm. 

The controlPanel of a GUISwarm can be talked to by other objects as
well - as if they could reach up to it from the *inside* of the screen
and push the buttons to the same ends. We are reaching out to the
screen here when we simply say [observerSwarm go].

Notice that we no longer store the result of the "activateIn" message
on the toplevel swarm we are creating - this is because the control
panel provides us with another way to access the underlying
activities.  The ActivityControl package is another way to gain a kind
of a "virtual" control panel, or dash-board, one that can be used in
the absence of a GUISwarm.


ObserverSwarm.h and ObserverSwarm.m


The function of the ObserverSwarm is to make observations on the
ModelSwarm. Therefore we build a lot of graphical widget tools in the
ObserverSwarm. The mechanisms for creating and initializing these
graphical objects will be familiar to you by now. Many of these
visualization tools are quite general, so that they can be used to
visualize many different kinds of things, as long as they are the
right Class of objects.

Once again we have three primary methods: buildObjects, buildActions,
and activateIn. This is commonly the case for most Swarms, but not
all. Swarms are collections of objects with schedules of events over
them, so the basic work to build, schedule, and link things together
is usually pretty much the same.

In buildObjects, the first thing we do is to build the ModelSwarm, as
we did in main.m. We can create the ModelSwarm inside the
ObserverSwarm, using the [ModelSwarm create: self] without having to
explicitly create a new Zone.  What this does is create a *separate*
Zone for the ModelSwarm that is nevertheless *pointed-to* by the
current Zone in such a way that if the ObserverSwarm's Zone is dropped
- this will also drop any sub-Zones (such as the ModelSwarm's Zone)
within it.

Zones are objects that manage memory allocation and reclamation in
Swarm. In fact, Swarms are subClassed from Zones, so a Swarm is really
a kind of memory manager, in addition to being an activity
manager. Just as we package up similar functionality in objects, we
package up things that are likely to be created and destroyed at
similar times together. With Zones and Swarms, we can drop everything
that has been allocated within them at once,` without having to resort
to a "dropObjects" method that undoes everything we built up in
"buildObjects". In fact because a Swarm is also a Zone, when you drop
the Swarm you are, in fact, dropping that Swarm's Zone simultaneously.
The distinction between Zones and Swarms is somewhat subtle, but the
ability to be able to create new Swarms within a current Swarm without
having to explicitly create a new Zone, results in more readable and
less cluttered code.

Once we have created the modelSwarm, we tell the control panel
to stop. We generally do this because we might want to alter
the parameters of the model at this point, before the 
ModelSwarm has started building its objects. We'll do that
in the next app. Here, the controlPanel appears on the 
screen, and politely waits for us to punch the "go" button
before anything else happens.

After the user has pressed "go", we go ahead and send a message to the
ModelSwarm to build its objects. This makes sense, because the objects
in the modelSwarm have to be there before we focus our observing
obects on them, so we build them first.

Then we start building the objects that we will use to observe the
model.

First, we construct a colormap: a mapping from numbers to colors so
that we can tell things apart. We get to assign whatever colors we
want to numbers.

Then, we create a ZoomRaster window object for displaying 2D data on
the screen. We are going to display the foodSpace in this window, and
superimpose the bugs on it as well, so we configure it to their notion
of the size of the world. You will notice that we have multiply nested
message sending here. Methods often return a pointer to some structure
which we must further query to get at what we really want.  Here, we
ask the ModelSwarm to for a pointer to its "world" in order to ask
that world how big it is.

The Value2dDisplay is an object that will convert between 2D data
structures and the RasterObject. We can have every point in a lattice
displayed by asking the Value2dDisplay display it.  This object will
manage the displaying of the foodSpace.

Finally, we have an Object2dDisplay, which will manage a collection of
objects and render them at the appropriate parts of a 2D display
widget. Both of these display managers write out to the Raster object.


In buildActions, we create the actions necessary for the simulation.
This is where the schedule is built (but not run!)  Here we create a
display schedule - this is used to display the state of the world and
check for user input. This schedule should be thought of as
independent from the model - in particular, you will also want to run
the model without any display.

We first let the ModelSwarm build its schedules. Then we create an
actionGroup for the messages we want to send to our observation
objects. Thus, we schedule messages to the two display managers asking
them to display to the Raster, and then we tell the Raster to update
itself, drawing on our screen.

Next we arrange to check for any input from the user (like a mouse
click on the controlPanel). Once we've packaged up the display
actions, we place them on a schedule with a potentially variable
display frequency.

Finally, once again we activate the schedules we have built. Notice`
that although hierarchical models are typically built from the leaves
up (higher level objects usually need the lower level objects to be
there first), activation propagates from the top-down. All activities
are ultimately rooted, and managed, from the highest level (where we
rooted them in "nil" in main.m).  An activity has to be grounded in
nil, or activated in something that is activated in nil, so activation
proceeds from the top down, rather than from the bottom-up. This does
not mean that control flows from the top-down, merely the "gluing"
together of activation trees in preparation for traversal by
activities.

Thus, wheras buildObjects typically calls buildObjects recursively opn
a subSwarm before it builds its own objects, activateIn typically
activates itself first in the context that was passed down to it, only
then calling activateIn on its subSwarms or schedules.

Here, the ObserverSwarm activates both the displaySchedule and the
modelSwarm in itself. These schedules will be managed as concurrent
activities - it is a branching point in an activation tree, as opposed
to a nesting. On real parallel hardware, the activity objects
traversing the tree could duplicate at this point, traversing both
branches in a parallel, but coordinated fashion.



ModelSwarm.h and ModelSwarm.m

The ModelSwarm has acquired a few new methods to allow external access
to some of its objects. Other than these three access methods,
however, the ModelSwarm hasn't changed much.

Notice that because we will be able to watch the bugs, we don't bother
with a reporterBug anymore.



FoodSpace and Bug

Haven't changed - we're working with much higher level objects
now. These objects are deep in the object nesting.



Makefile

Adding the ObserverSwarm introduces yet more dependencies.



NEXT -> simpleObserverBug2









, we  



1






