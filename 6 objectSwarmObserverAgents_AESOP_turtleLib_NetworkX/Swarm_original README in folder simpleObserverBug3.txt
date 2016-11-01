// simpleObserverSwarm3

            ADDING A PARAMETER CLASS AND ENABLING COMMAND-LINE ARGUMENT PROCESSING


main.m

There are some significant changes here.  We change the initSwarm
function to

initSwarmArguments(argc, argv, [Parameters class]);

We have created a new class, Parameters (which is in Parameters.h and
Parameters.m) and we tell Swarm to use that class to create an
arguments object for us.  When this works (we did not say "if", but
"when") then there will be a global object called "arguments" and any
class can send messages to it.  These classes will need to import the
Parameters.h file. Don't forget that. Also, when you use the "arguments" 
object, some versions of gcc will insist you cast the object, so that 
the compiler can find the correct methods.  Hence usage is written like:

[(Parameters *)arguments getSeedProb];

In the main.m, we also tell the arguments class to run its init
method, which initializes some variables, and we also create an
arvhived probe display so the user can adjust whatever variables
he/she sees fit to change.  The term "archived" means that, if the
user hits the "SAVE" button in the Control Panel when the simulation
is stopped, then the window positions of the application are saved to
a file called .swarmArchiver in the user's home directory. Assuming
all goes well, then the window positions will be used the next time
the program runs.


Parameters

This is a new class.  It exists for two purposes.

1. It can "parse" command line arguments.  If you set it up right, then you
could start the model with 

./bug -d0.2

and it would run a model with bug density of 0.2 bugs for you.  Note that
would have the same effect as if you used the long command option

./bug --bugDensity=0.2

The main reason why you want this ability is that, with it, you can 
automate the processing of the model with various auxiliary programs,
such as Drone.  Drone can make the program go over and over, testing
various settings and exploring what happens when a model is repeated
a number of times.

2. It can give parameter values to the other objects in the model.

This version of the Parameters.m file uses some functions that were
written by Marcus Daniels.  This version uses the function getInt(),
which can be used by other objects to find out what values the
Parameters object is holding for integer valued variables.For example,
if the ModelSwarm wants to know how many bugs there are supposed to
be, it can just ask, as in

    bugs = getInt( (Parameters*)arguments,"bugDensity");

I have found this more convenient than writing "get" methods for each
individual integer.  But I don't use this approach for other types of
variables.

The most befuddling part of the Parameters.m file, by far, is the
setup to parse command line arguments.  This parse method gets called
many times, once for each command line option you give.  It checks to
see which variable you are trying to set and it copies the value you
give into that variable.  

In the createBegin method, an array of structs, options[], is
declared.  Each element in this array is a series of characters that
control the program's communication with the command line.  Consider
one entry in this array from Parameters.m:

  {"bugDensity",'d',"D", 0, "bug density", 8},
In order, these mean 
	bugDensity: the long name of the command line  option, as in --bugDensity=33 
	d: the "short name," or key, of the command line option, as in -d0.3 
	D: the symbolic value used to refer to the input.
	0: a nonNull flag, indicating an input value is required
	"bug density": a description that will appear to the user
	8: the order of this parameter in the printout to the user.

To find out what command line arguments a program accepts, you type

   ./bugs --usage

or
   ./bugs --help

In this example, we create input values for simulation variables like
the seedProb and bugDensity, as well as a randomSeed value to
initialize random generators, the run number (in a series of repeated
runs, possibly), the input file name, and the experiment duration.
All of these need not be given in the command line in every run.  The
createBegin: method of the Parameters.m file sets default values for
most of the parameters, and these will be used unless overridden from
the command line.

You may notice that some of the arguments that we prepare for parsing
are not used for anything at all.  The "input file" is one example.
These are included with foresight that this program might be used with
Drone, and Drone expects every program to be able to take at least
three command line parameters, the run number, the random seed, and
the name of the input file.
 
The parseKey:arg: method must be carefully tailored so that the
command line options are correctly interpreted by the program.  When
the initSwarmArguments function is called in main.m, it looks at our
Parameters class, creates an instance, and then it uses the parseKey
method to adjust any values in response to the command line.  When the
values are entered from the command line, they are read in as
character arrays, and so we have to use C conversion functions, atoi
and strtod to convert them into integers and doubles, respectively.

The init method now has the probes that used to be in the ModelSwarm's
createBegin method.  We want them to be declared in Parameters so that
we have a "free standing" parameter object, one that exists before
anything else.

ObserverSwarm

We have made a few changes here.  No doubt, the most conceptually
siginificant change is the re-sequencing of the way in which the
modelSwarm is created.  As in the previous tutorial exercises, the
values in "bug.scm" are used to initialize the model. However, we want
the command line parameters to override those values.  So, the
modelSwarm is told to get the new parameters:

[modelSwarm resetParameters];

The other changes in the ObserverSwarm are designed to facilitate
record-keeping and repetitive processing of the model.


One is purely cosmetic, really.  We have disabled the
CREATE_PROBE_DISPLAY(modelSwarm) command.  This is done only to
prevent distraction.  Since we have a probe display from the
Parameters object, we don't want to see the same set of parameters
twice.


In case you really do want to see the same thing twice, and put that
CREATE_PROBE_DISPLAY command back into the ObserverSwarm.m file, you
will see an obvious problem when you run the model.  If you enter
command line arguments to the bug program, as in

./bug -x70 -y70 -d0.3

or, equivalently with long form options:

./bug --worldXSize=70 --worldYSize=70 --bugDensity=0.3

you will see that the probe display from the model swarm is not "up to
date".  The display for the Parameters class is correct, but the
display from the ModelSwarm still shows the default parameter values
that are specified in the scm file that is used to initialize the
modelSwarm in the ObserverSwarm.m file.  The ModelSwarm probe corrects
itself when the first step of the simulation occurs, reflecting the
fact that the values have been obtained from arguments.



The other changes we have made in the ObserverSwarm are intended to
make your life a little easier if you don't want to watch your
simulation run to the bloody end.  

First, There is a new instance variable in the ObserverSwarm. It is 
currentTime.  Sometimes it is important to know what the current
time step of the simulation is.  The Swarm function getCurrentTime()
can be used to retrieve the time, but not if the model is stopped.
Sometimes when the model is stopped, we want to know the time, so
the currentTime variable saves the time.  The time gets used in
the "takeScreenShot" method (see below).

Second, we have added a method called "takeScreenShot". That method
"takeScreenShot" is tied into the graphical interface, so whenever the
user wants to take a picture of the screen, hit the button!

Third, we have added a method called "stopRunning" and scheduled it
so that, even if you are off drinking coffee, your program will take a
picture of itself and close down.  Or, if you want, it will stop there
and wait for your instructions.

Here is how it works.  The effect of the stopRunning method depends on
a C preprocessor flag that we have chosen to call "UNATTENDED".  If
the UNATTENDED flag is defined when the program is compiled, the
simulation will start, even if you don't press the go button, it will
run until it has completed "eventDuration" steps, and then it will
save a picture of the state of the screen, and then it will close the
program.

In case you are unfamiliar with them, the C preprocessor flag is a
useful way to control the inclusion of features in a program.  If you
use the following make command to build the program:

make EXTRACPPFLAGS=-DUNATTENDED

then the C preprocessor will proceed as if the variable UNATTENDED is
defined.  So when the compiler comes to the directive:

#ifdef UNATTENDED

it will proceed to include whatever code follows that line until it
reaches the command 

#else

which will cause to compile an alternative set of commands.  Finally,
when the conditional processing is finished, the program includes the
command

#endif

The endif command closes off the conditional code, and the compiler
picks up once again processing each statement.  

If you compile this program with the C preprocessor flag UNATTENDED,
you will notice a couple of interesting differences when you run the
program.  In the UNATTENDED mode, the control panel is set to the
state "running," so the simulation requires no user intervention.  It
goes until it completes the number of steps that you tell it to
complete, and then the stopRunning method quits the run.  It will take
a picture of your screen and save it in your current directory in a
file called "screenRun01Time01000.png.  The Run number 01 indicate the
run number that you supply in the command line or in Parameters.  The
second number in the file name represents the time step upon which the
simulation ended.  Then it will close up the swarm program altogether.

The idea here is that you can set the variable experimentDuration in
in the command line, along with some other parameters, say something like this

./bug -e1000 -R01 -d0.1 -p0.5 -S9878998

and the simulation will run for 1000 steps, take a snapshot,
and quit.  

If you don't want the simulation to quit at that stage, you can change
the command

[controlPanel setStateQuit]

to

[controlPanel setStateStopped]

and then you can press GO to make it run some more.  And if you get
annoyed because we have the simulation stop after a while (by default,
1000 steps) and wait for user input, you can make the obvious changes
in the stopRunning method.

In order to trigger the stopRunning method, we have added a new
schedule called "stopSchedule" in this model.  The stopSchedule causes
the observer to run the stopRunning method at each time step.  If the
current time, according to the Swarm function getCurrentTime (), is
equal to the experiment duration, then the control panel is told to
quit.

Note that we have added this schedule in the buildActions method and
we have activated it in the activateIn: method.

If the program is compiled without the UNATTENDED flag, then the
experiment duration has a new, useful function.  If you are running
this program interactively, you may want to make it run up to any
given time, such as 467, and stop.  If you type that value for
experimentDuration in the probe display for the Parameter object, and
press the start button, the model will run up to that time and stop.
If you want to see what happens when it goes up to a higher time
value, just type in that value and hit start.

Finally, we have used Swarm's features to save window positions between
runs of the model.  We switched from CREATE_PROBE_DISPLAY to 
CREATE_ARCHIVED_PROBE_DISPLAY and we inserted setWindowGeometryRecordName
argument in the command that creates the ZoomRaster.  Now the control
panel's save button stores window positions.

ModelSwarm


The change here looks pretty drastic, but its not really so bad.  

There is no longer a need for a createBegin method!

We moved the Probe Maps into the Parameters class.  Further, there is no
need to set values for parameter variables here.  We can retrieve them from the
Parameters class when we need them.  

There is a new method called "resetParameters", which will cause the model to
go and get the newest values of the input parameters.

  worldXSize = getInt(arguments, "worldXSize");
  worldYSize = getInt(arguments,"worldYSize");
  seedProb   = getDouble(arguments,"seedProb");
  bugDensity = getDouble(arguments, "bugDensity");

This is necessary because the model swarm was created according to
the parameter values originally specified in bug.scm.  We need to override
those values with the numbers from the command line.


Everything else is unchanged.  Note that, if you leave out one of
these lines, then the parameter value in the bug.scm file will be
used.


Makefile

Don't forget to introduce the Parameters.o in here!


Conclusion

Sometimes people want to run a simulation over and over again to
explore various possibilities.  We are trying to work our way up to
that capability right now.  In fact, we are extremely close.  If you
don't mind a little "stone knive and bear skin" scripting, take a look
at the file we have included called "batchBug.sh".  The file
"batchBug" is just a list of runs of the bug model.  If you adjust
the parameters how you like, you can make the model run over and over
again by executing the program "batchBug.sh". (On Unix, that file must be
executable, of course.)

If you want to do a little shell programming, you can enhance and
beautify the batchBug file to cycle through a large number of values
for any of the variables.  Or it could simply replicate an experiment
many times.  

There are pre-existing programs that can manage parameter sweeps of
that sort. One is called Drone, which is available from the web pages
of the University of Michigan.  Drone uses a tcl/tk addon called
Expect.  Some day, there might be a section of this tutorial
explaining more about how Drone can work with Swarm.

Until then, you can look over the next step in the tutorial, which
outlines one way in which it is possible to make a batch simulation
repeat itself by building a model swarm that lives inside an
experiment managing object.  If you use Drone, or batchBug for that
matter, there is no practical need to pursue the simpleExperBug
approach.

Paul Johnson pauljohn@ku.edu  May 13, 2003

NEXT ->  simpleObserverBug4













