// Tutorial

		SIMPLEBUG SWARM TUTORIAL


This tutorial takes the user through the development of a Swarm
model that makes use of a lot of the functionality of Swarm.

The model consists of bugs taking random walks in space. There
is nothing particular about the model to recommend itself to
our attention, except that it is so simple that it won't get in 
the way of the explication of Swarm as we go along. 

We start out with a very simple, essentially C program for
a bug taking a random walk. Through a progression of models
we introduce basic object-oriented and swarm style programming.

Although this is a particularly simple exercise, it shows how 
easy it is to compose fairly complex software from simple
building blocks. 

In this directory are 8 subdirectories, each with a complete
Swarm application and a README file that walks you through
the code.

You should start with the "simpleCBug" application, and follow
the pointers at the bottom of the README files. You will
go through them in the following order:

simpleCBug
simpleObjCBug
simpleObjcBug2
simpleSwarmBug
simpleSwarmBug2
simpleSwarmBug3
simpleObserverBug
simpleObserverBug2
simpleObserverBug3
simpleBatchBug1
simpleBatchBug2
simpleBatchBug3
simpleExperBug

Once you have gone all the way through this tutorial, you should be
able to make sense of many of the applications on the Swarm
web-site.  They can appear to be quite complex, but once you
get a feel for the underlying patterns, they are really not
that hard to understand, or to build.


On building the applications.

If you have swarm installed, you should just be able to edit the
Makefile in each application to point to SWARMHOME on your system. If
you are on a Linux or Unix system, this is done (suppose you are using
the BASH shell) by typing a command

# export SWARMHOME=/usr

(This can be inserted into your HOME directory's .bash_profile file.)

Then just type 

# make

and the applications should build. Depending on which version of the
GNU compiler you have, you may see more or fewer warning messages 
about possible problems.  Some versions give warnings which, in our
opinion, are quite unnecessary (especially the warning about multiple
declarations of methods inside the Swarm libraries themselves).

To run any of them, just type 

# ./bug

after they've built and linked.

About the Authorship of these Exercises

These tutorials have many excellent insights and helpful pieces of
advice for people who are learning to write programs.  Many users have
wondered who they should thank, and we are not entirely sure! Most
authors have chosen to remain anonymous.  We know that the original
author was Dr. Christopher Langton, the founder of the Swarm project at
the Santa Fe Institute.  

The essential form of the tutorial was maintained from 1996 (when the
Swarm beta was distributed) through 2004. Several members of the Swarm
team (at SFI and later under the auspices of the Swarm Development
Group) have make changes to keep the code up-to-date.  The first
substantial changes in the tutorial correspond with the release of
Swarm-2.2.  The new components, simpleObserverBug3, and
simpleBatchBug[1-3], were installed to facilitate use of Swarm by
researchers.  These are intended as a replacement for the approach
described in simpleExperBug because the approach described there has
not proven workable in some (many) contexts.  We are encouraging
the people who work on these files to sign their names, not only to
take credit for their effort, but also to facilitate future revisions
and to help users in finding answers to their questions.

