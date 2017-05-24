(2015 December)
0.9     First version distributed via the Git system

(2015 02 11)
0.91    Eliminated unused file ObserverSwarm.py in folder
'6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX/basic'

(2015 03 01)

0.911   Improved the presentation with a quick introduction

(2015 04 10)

0.92 Introduced in folder 6, file start.py, a *debug* common variable; if set to True, a large part of the try/except structures will be bypassed, so the errors will be managed directly by the Python interpreter;  this choice can be useful when you build a new project and as an expert user you want to check the errors in a basic way

(2015 04 10)

0.921 Set, in start.py, common.debug=_False_ as default

(2015 04 21)

0.922 Modified ObserverSwarm.py correcting cycle => common.cycle to facilitate the access to this information in any part of the applications

(2015 04 24)

0.93 Added the project 'debug' to check debug capabilities. Have a look to the
file debug.txt in the folder 'debug' of folder '6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX'

Modified a few error message of ModelSwarm.py if the required method does not exist

Improved the Tools.py output in case of error on a method

(2015 06 07)

0.94 'project' is by default both the name of the application and of the subfolder
that contains its code; the subfolder is supposed to be placed within the
SLAPP tree

With this version, the folder can be placed outside the SLAPP tree
if we place a file project.txt in the folder
"6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX"

The file has to contain the path and the name of the folder of the project

(2015 06 10)

0.95 simplified the reference to agentList in Agent.py in production project

simplified Agent.py in projects using a superAgent class as a container of unspecific methods

(2015 08 08)

0.951 fixes a bug in the version control for the library NetworkX, in production/parameters.py

(2015 08 08)

0.952 fixes a residual bug in the version control for the library NetworkX, in production/parameters.py

(2015 08 20)

0.953 adds the capability of recognizing if running in IPython or in Python

(2015 08 26)

0.96  clarified scheduling in Observer.py about 'visualizeNet'; corrected also
oActions.py in production project; no changes in the results

(2015 08 31)

1.0   Having now a Handbook, this is version 1.0  

(2015 09 02)

1.01  Reorganized start.py in the folder '6 objectSwarmObserverAgents_AESOP_turtleLib_NetworkX' considering the possibility running SLAPP also in IPython

(2015 09 10)

1.1   New starting point in the main folder (runShell.py)

The file project.txt (look at the Reference Handbook) can be also placed in the main folder

Better management of 'end' condition for graphical projects

(2015 09 29)

1.11  Allowing a wider use of WorldState. This is only a temporary patch, the interface
to WorldState in ModelSwarm.py will be quite soon re-engineered, also having as
optional the presence of WorldState.py in the folder of a project

(2016 02 15)

1.2   Introducing the extension .txtx (extended txt) to be used for the definition
of the files describing the agents

Have a look to the Reference Handbook, section *The agents and their sets*, sub section *Files .txtx in defining the agents*

(2016 04 08)

1.21 Modifications facing v. 1.5.1 of matplotlib

New independent folder *matplotlib_aQuestForAFewGraphicCapabilities* to explore matplotlib in Python & IPython environments

From now on, SLAPP runs only via a terminal or in IPython (jupyter notebook),
using runShell.py or iRunShell.ipynb (look at the Reference Handbook, section *How to run SLAPP*); it is also possible to run SLAPP in IPython via Spyder and in iptyhon in a terminal

In IPython, the magic command '%matplotlib inline' is internally added if missing;
if '%matplotlib' is the explicit choice, the 'inline' option is internally stated

In the main folder now we have runShell.py to start the shell in Python and
iRunShell.ipynb to start it in IPython (using "jupyter notebook"); have a look
to the Reference Handbook, again section *How to run SLAPP*

The patch for matplotlib 1.3.4 is no more necessary and we have eliminated it;
you can anyway retrieve it in the branch v.1.2 in the github repository of SLAPP

matplotlib produces an annoying warning about creating fonts; to avoid it, several
hints online suggest to delete in ~.cache the folder fontconfig or matplotlib
Instead, in MacOS go to the folder .matplolib in your home and delete the file
fontList.cache
The annoying warning will appear only one more time

(2016 04 15)

1.22 maintenance

corrected ModelSwarm.py in $$slapp$$ - now the agentList is set into the agents
also if operating sets do not exist

class superAgent in agTools.py in $$slap$$ is now SuperAgent (reported the
correction) in all the projects

range # a b in schedule.xls now repeats (b - a + 1) times and not (b - a) times

more detailed graphic reactions to the graphical environment:
Now SLAPP works
- from a plain terminal, with:
python runShell.py
OR
ipython
AND internally
%run runShell.py
(with the same graphic results of python in terminal)

- from jupiter notebook (with inline graphics)

- from Jupiter QtConsole - e.g. Anaconda launcher - (with inline graphics)

- from Spyder ipython (with inline graphics)

(look at the Reference Handbook, section *How to run SLAPP*)

(2016 07 25)

1.3 significant collection of maintenance modification (in GitHub history)

last change: fixed an error with Tkinter, using IPython 5.0 or greater

(2016 08 02)

1.31 new feature: the report in output of the probabilities of the methods,
if any

(2016 08 17)

1.32 debug option can now be set from the project; clarified also in the
Reference

(2016 08 21)

1.33 Reengineering WorldState, as anticipated in version 1.11, to have
a clean structure, now working both as calculation tool and a repository
of values, have a look to the Reference Handbook

In mAction.py modify any occurrence of

     worldStateList[0]
to

     worldState

Unfortunately you have to modify a bit your projects

If you do not use the WorldState feature, simply delete the file
     WorldState.py

If you use it, please modify

     def __init__(self,number):

to

     def __init__(self):

and eliminate any reference to number or to self.number, maybe also in the
initial print, always in WorldState.py

(2016 08 22)

1.34 Eliminated everywhere the dictionary of the action groups
actionDictionary, unnecessary, but kept in Tools.py of $$slapp$$ for
retro compatibility

(2016 08 25)

1.35 Introduced the capability of the agents of adding or eliminating tasks in
the schedule (at the level of the schedule reported in the schedule.xls
file)

Have a look both to the example in 'basic' project, file
scheduleAddElim.xls (to use it, rename it as schedule.xls) and to the
section 'Agents adding and eliminating tasks into the detailed schedule'
of the Reference Handbook

(2016 08 31)

1.36 Big step, now SLAPP uses agent of different classes, as in the example
basic2classes

(2016 09 01)

1.4  Correction of minor problems and alignment of the Reference Handbook to
the novelty of the multi-class capability, look at the Section "SLAPP
multi-class: the *basic2classes* example"

(2016 09 11)

1.41 Improving the introductory files and the Reference Handbook

(2016 09 17)

1.5  Creating [http://slapp-online.net:6789](http://slapp-online.net:6789) to
simplify the initial knowledge of SLAPP

(2016 09 25)

1.6  A step ahead in SLAPP presentation

(2016 11 17)

1.6.1 Fixed an error in production project: in addAFactory method - and in
removeItself one, when applied to an added agents - the list of the agents
was not updated because it was not set in the creation phase for the added
agents

Also the lists of the other agents and that of the ModelSwarm, via the
address now generated by ModelSwarm in commonVar.py, are updated with
a new specific code, within the two method reported above

(2017 04 01)

1.6.2 Multi-class structure is now more general (look at Chapter 3 of the
Reference Handbook contained in the distribution of SLAPP)

(2017 04 18)

1.6.3 Fixed an error in recognizing library versions and updated the Reference
Handbook: the description of the *basic* example was not aligned to the
modifications of version 1.6.2 about agent creation (Section 2.3)

(2017 04 24)

1.6.4 New feature 'specialAction' acting in specific time steps, look at
the example 'basicSpecialAction' and to the paragraph pointed by index
voice 'specialAction'

Put in common space the variable 'project' containing the path to the
project

(2017 05 11)

2.0   Last version in Python 2, we will only report corrections for bugs, no
improvements

The next version, with 3.0 number, will be running in **Python 3**

(2017 05 11)

3.0   New version in **Python 3**

Folder *7 (toBeDeveloped_aFewHints)* is no more useful and has not reported (but you can find it until v.2.0)

Transition notes into the file *from2to3.md* with a technical part dedicated to a **digression on methods and functions** in Python 3

Fixing also .txtx file translation
