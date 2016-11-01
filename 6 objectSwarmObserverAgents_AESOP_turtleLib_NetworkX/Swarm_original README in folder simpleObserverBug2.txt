// simpleObserverSwarm2

             ADDING PROBES AND PROBE DISPLAYS ON OBJECTS

main.m

Again, nothing new here - we build the ObserverSwarm and start it.


ObserverSwarm.h and ObserverSwarm.m

Now we add a very useful observation object. Probes are just what
their name implies - probe-like access directly to the internals
of any object in Swarm. The Probe Library allows one to, effectively
break the hiding away of information within objects inaccesibly.

A Probe can be attached to any object in Swarm, and all of its internal
state and methods can be accessed and manipulated from the outside.
This is both incredibly useful and incredibly dangerous. 

However, probes are essential. We can never anticipate in advance
everything what we might want to know about objects state. And it
would be inefficient to provide a "get" method for every 
internal variable on every object. Hence probes.

Probing is based on ProbeMaps. There is a probeMap for every 
class in the system, although they don't really exist until
someone asks for one. probeMaps make the mapping from an object's
class to the location of variables in its internal data-structure.

Therefore, every aspect of internal state is potentially observable
in swarm.

In createBegin, we create an empty probeMap for the ObserverSwarm
class, so that we can customize it to look only at the variables
and methods we are interested in. Without customizing, one gets
*everything*. We customize the probeMap to show us the one
variable of interest, displayFrequency, and then install the
probeMap in the probeLibrary. Fro now on, anytime anyone wants
to probe the ObserverSwarm class, they will get this map.


In buildObjects, we create "probeDisplays", probes attached
to graphic widgets that will show object's internal state
on the terminal screen. ProbeDisplays can be typed into, to
change object's state, and the objects methods can be invoked,
asking them to do things. by creating a ProbeDisplay on 
the ModelSwarm, all of the models' parameters are displayed
on the screen, where they can be altered. 

This is where we halt the process with a stop message to the
control panel. Once we have displayed the Model parameters,
we give the user a chance to alter them before going on
to actually construct the model.

We then go on to the normal construction of ObserverSwarm
objects. At the end of buildObjects, however, we send a
message to the worldRaster object, which enables it to
make a probeDisplay for any object that it knows about
on the screen. Thus, we will be able to "click" on the 
bugs that we've been running, and get to look inside of 
them and/or change their state.

Once you have started the model running, stop it by clicking
on the controlPanel stop button, and then click on one of the
bugs on the screen. You will get a window listing its internal
state, (not much more than xPos, yPos).



ModelSwarm

We also build probeMaps within the ModelSwarm. All of the Model's
parameters will be available for inspection and alteration.



NEXT ->  simpleExperBug
