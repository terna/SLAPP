October/November 2016; May 2017

## **Moving to Python 3**

### Automatic changes

The first step has been that of using *2to3*, which is part of the Python 2 distribution, with the script *my2to3* (reported here), containing:  

    #!/bin/bash  
    2to3 -W "$1" > changes  
    mv changes "$1".changes  

e.g.  

    my2to3 "start 1 plainProgrammingBug.py"

(with the usual chain of ../../ etc. in the beginning (before my2to3) and the name of the file quoted if it contains spaces)

produces:

    start 1 plainProgrammingBug.py : the corrected file   
    start 1 plainProgrammingBug.py.bak : the backup of the previous .py file   
    start 1 plainProgrammingBug.py.changes : the list of the changes

The correction done in this way are mainly related to *print* and *input* statements

### Handmade modifications in *$$slapp$$* folder

##### convert_xls_txt.py

modified the sort criteria; it was  

    ll.sort(cmp=lambda x,y: cmp(x[0], y[0]))

but cmp is not implemented in Python 3, so a new way as been introduced,
using *key*, already existing in Python 2, with  

    ll.sort(key=lambda x: x[0])

##### Tools.py, with a technical digression on methods and functions

*my2to3* has automatically modified the former *extractMethod* function, but that function is now completely different and named *extractMethodFromMethodFunction*

The reason is that in Python 3 the concept of unbound method no more exists and m of the class A in the form A.m is simply a function defined in A (or in parent class of A).

*extractMethod* was based on complicate code separating class and method in an unbound method, now instead the **\__qualname__** attribute simplifies the operation.

\__qualname__ applied to a simple function acts in the following way (interactive use of Python):

    >>> def f(x):
    	return x

    >>> f.__qualname__
    'f'

Applied to a function defined in a class, the reply is:

    >>> class A():
	        def m(self):
		         pass
    >>> A.m.__qualname__
    'A.m'

so

    >>> A.m.__qualname__.split()
    ['A.m']
    >>> A.m.__qualname__.split(".")
    ['A', 'm']

and if

    >>> class B(A):
         	def n(self):
          		pass

    >>> B.m.__qualname__
    'A.m'
    >>> B.n.__qualname__
    'B.n'

The novelty is documented in the (funny: "Python 3 adds insult to injury by dropping what was formerly known as unbound methods") [PEP 3155](https://www.python.org/dev/peps/pep-3155/).  


Also the function *applyMethod* has been hand modified due to the modifications above.

Always in *Tools.py* we have to manage the new *exec* definition, being now a function (in Python 2 was a statement). At [https://docs.python.org/3/library/functions.html#exec](https://docs.python.org/3/library/functions.html#exec) we read "Pass an explicit locals dictionary if you need to see effects of the code on locals after function exec() returns".

In *applyMethod* we have now the dictionary *space={}* and *exec* uses it.  

As an example, from *Tools.py*:

    c=instance.__class__
    # check if that class has the method 'method'
    space={}
    space['c']=c
    space['inspect']=inspect
    test=False
    try:
        exec("test=inspect.isfunction(c."+method+")", space)
        test=space['test']

The function *checkVersion(version,name,k0,k1,k2)* has been added in v. 1.6.3 and verified from 2 to 3 via the temporary file *Tools_Addendum.py*


In *ModelSwarm.py*

Modifications related to the new agent creation structure of v.1.6.2

after
    # this block is not alway useful, but (...)

 and in

     if self.classes[agType]=="Agent":


### Handmade modifications in *basic*, *basic2classes*, *basicSpecialAction* and *debug* folders

in *commonVar.py*

    toBeExecuted="print ('Goodbye')" # added () in print BY HAND

or

    toBeExecuted="print ('Goodbye from the debug world.')" # added () in print BY HAND

### Handmade modifications in *basic2classes* folder

Deeply modified the *exec* structure (see also above) in *mActions.py*, function *createTheAgent_Class*, both creating a locals dictionary named *space* and putting the import of the class used to create the agents at the head of *exec* quoted string.  

    exec("from "+agClass+" import ... ; ..."

### Handmade modifications in *basic*, *basic2classes*, *debug*, *production*, and *school* folders

NB, not in *basicSpecialAction*, created directly with the new agent creation feature

Modifications related with the new agent creation structure (v.1.6.2)

in *mActions.py* of *basic*, *basic2classes*, *debug*, *production*, and *school*
modified the creation block
(for *basic2classes* also the creation with classes, via *createTheAgent_Class*)


### A note on random number behavior

Working on *basic*, *basic2classes*, *basicSpecialAction* and *debug* we can verify that a sequence of *random.random()* numbers has the same content in Python 2 and in Python 3 if *n* in *random.seed(n)* is the same.
Unfortunately, *random.shuffle()* behaves in a different way in the two Python versions, as you can read at
[http://stackoverflow.com/questions/38943038/difference-between-python-2-and-3-for-shuffle-with-a-given-seed](http://stackoverflow.com/questions/38943038/difference-between-python-2-and-3-for-shuffle-with-a-given-seed) and also, after a call to *shuffle* the successive sequence of random realizations will be different in the two Python versions.

Due to this behavior we cannot reproduce in a full detailed way a run of a project in SLAPP working with Python 2 and with Python 3.

### Handmade modifications in *production* folder

Found an inconsistent use of tabs and spaces in indentation in line 23 and 36 of *parameters.py* file.  

Modified by hands, for v.1.6.3, in *parameters.py* file, the control of the versions of the libraries NetworkX and Matplotlib

### Handmade modifications in *start.py* file

Temporary eliminated the version number (???py3), keeping updated the build date

Added the copy of the project name in common, block starting with
    # project reported in common for possible uses in other SLAPP segments or
    # applications

### Handmade modifications in *txtxFunctions.py* file

Modified the exec structure, with a dictionary
