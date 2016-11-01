// simpleSwarmBug2


                     MANAGING MORE AGENTS


main.m

We extend the model in this version, but............not here! 

Our model is now encapsulated in the ModelSwarm, so any extensions 
will now happen there. This main.m is exactly the same as the previous
one: We just build and start the modelSwarm



ModelSwarm.h and ModelSwarm.m

Now that we have our model encapsulated in an object, further work 
on the model happens here. In this version, we extend the model by 
allowing for a large number of bugs to live in the same world.

We add two structures to accomodate the newcomers.

First, we don't want them stepping all over each other so we add 
another space with which the bugs interact which makes sure that 
there is never more than one bug at a site.

Second, we create a "collection" of all the bugs, so we can treat 
them as a unit. In fact, we encapsulate them into a "List" object, 
and now we communicate with them by sending messages to the bugList, 
which, in turn, forwards our messages to the whole set of bugs.

Thus, we have "incarnated" another abstraction into a kind of "thing" 
that we can interact with: the collection of all the bugs.

Grid2d is Class of objects that is already defined in the Swarm 
libraries, so we just ask it to make us an instance.  Grid2d 
enforces only 1 bug per site. "nil" means that there is no bug at 
the site, while a bug's "id" itself is stored there when a bug is 
there.

The collection of bugs is entrusted to a List object. A List is also 
predefined, so we don't need to define either of these ourselves 
via .h and .m files.

The uniformDblRand id is an object in the random number library
of swarm that gives us random "real" numbers with a uniform
distribution when we ask it to.

We grab the first bug we created off the list and anoint it
the "reporterBug" - we'll continue to have one bug tell us about 
its food encounters. After we've grabbed it we stick it back on 
the list....or rather, we ask the list to reinsert it.

In buildActions, we again create the list of simulation actions. 
We put these in an action group, because we want these actions to 
be executed in a specific order, but these steps should take no 
(simulated) time. The M(foo) means "The message called <foo>". 
You can send a message To a particular object, or ForEach object 
in a collection.

Here, we construct an action that will go on a schedule that has more 
than one thing happening, but we assume that they both happen in "zero" 
time, and hence effectively concurrently

We want two things to happen: we want *all* of the bugs to take their 
basic time-step action, and we want the reportBug to report to us if it 
found food.

The creatActionTo: message to the reportBug is like the one in the last 
version to tell aBug to take its step.

However, the createActionForEach: message is what we send to the List 
managing the collection of bugs, requesting that it rebroadcast the 
request to each of the bugs it manages, saving us from having to know 
about or deal with each bug explicitly. Bugs could come and go, and 
yet we would not have to change our behavior at this level.


Then we create a schedule that executes the modelActions. modelActions
is an ActionGroup, by itself it has no notion of time. In order to
have it executed in time, we create a Schedule that says to use
the modelActions ActionGroup at particular times.
This schedule has a repeat interval of 1, it will loop every time step.
The action is executed at time 0 relative to the beginning of the loop.

activateIn is the same as before



Bug.h andBug.m

We have added functionality to the bugs, as they now must share
a world with each other. They have to be able to determine that
there is nobody else at the site that they have chosen to move
to. They now check for this as well as for food in the step method.

For reporting purposes, the bugs set a variable if they did eat on
this step, so that they can report that if they happen to be the
reporterBug.

Also, we have a new method for "being" a reporterBug. If you get sent
this message, you were selected as the reporterBug, and you will
check that you ate this last step, and tell the world about it. 


FoodSpace.h and FoodSpace.m 

No change.



Makefile

No change.



NEXT -> simpleSwarmBug3


