// SimpleObjCbug2

           FROM THE LONE BUG TO HOME ON THE RANGE

main.m

In this version, we extend the previous model by providing the bug 
with a spatial "world" with which it can interact.  In this case, 
the spatial world has "food" that the bug "eats" as it wanders, 
removing it from the world.

This "world" is another object, and we create it and interact with 
it just as we do with the bug. The details of its implementation are 
laid out in the FoodSpace.h and FoodSpace.m files.

At initialization, the foodSpace is empty, and we first ask it to 
"seed" itself with food with a certain probability per site.

We also have to tell the bug how to access the foodSpace, which we do 
by passing its "id" to the bug in the message:

             [aBug setFoodSpace: foodSpace];

After that, it is pretty much the same as in the previous model.



Bug.h and Bug.m

Here, we have added a new internal variable to the bug: a pointer
to the "foodSpace" it will interact with. 

We have also added a coupld of methods. First, we have split
the "create" phase of the bug into two pieces: createBegin
and createEnd. We do this because we have a variable to set
that will not change throughout the run, and, for a number of
very good but very technical reasons, we want to set such
non-changing variables "during", rather than "after" the 
creatiion of the object. You don't see a createBegin method
here, because, for the time being, we are content to simply
inherit the createBegin method of our superClass, so we don't
have to list it here. However, we use the createEnd method
here as a visual seperator, a reminder, that the methods
listed above it will set internal state that will not, or
probably should not, change during the bug's lifetime, while
the methods after createEnd may change internal state.

Also, "create phase" methods, as the ones above createEnd are
called, will be called *before* createEnd is called. Most of
the time, they may *not* be called afterwards.

So, during the creation phase of a bug, we set its world size 
and the pointer to its food world, and then we call createEnd
to finalize the creation of a bug. 


The other thing that has changed is that the bug will interact
with the foodSpace during its "step" method. If it finds food
at the spot it moves to, it will consume it (remove it from
the foodSpcae) and tell us about it. 



FoodSpace.h and FoodSpace.m

A FoodSpace object is clearly pretty simple. It is completely
passive - it has no "step" method of its own. It actually is 
more complex than it looks, because it is a subclass of 
an existing Class of object already defined in the Swarm 
Libraries. The line:

	@interface FoodSpace : Discrete2d 

says that a FoodSpace is a subclass of the Discrete2D class.
That means that it is whatever a Discrete2d object is (has
all of the variables and methods that a Discrete2d object
has) but it also adds some variables or functions over and
above those of Discrete2d. 

  In this case, Discrete2D is basicly a lattice of integer values,
and it has methods defined on it that can set its size, get and
set values at sites in the lattice, and so forth. For reference
purposes, I've included a copy of the Discrete2d.h interface
file in this directory. You can look at that and see *what* 
Discrete2d can do, but not *how*. Remember, we don't really care
how it does its stuff, we just need to know what it can do.

  FoodSpace does not add any new internal variables, but it does
add a new method: -seedFoodWithProb:, which, when called with
an argument, will cause a FoodSpace to set some of its internal
lattice sites to 1's. How it does that is shown in FoodSpace.m

It simply walks over its lattice flipping a biased coin to decide
whether or not sites should be 1's. 

 By the way - it is common to "return self" if a method has no
need to return any value to its caller. "self" is an "id" - an object
name - that always points to the object in whose scope it is. 
Some methods normally return "self", but can return "nil" if
something went wrong when they tried to do what they were supposed
to do. The caller can test for the return value, and catch
the fact that something didn't go right in the other object if
it returns nil.



Discrete2d.h

This is here so you can see what FoodSpace inherits from it.
You ought to be able to get a pretty good idea by scanning 
over this .h file by now.



NEXT -> simpleSwarmBug


