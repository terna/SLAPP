October/November 2016

## **Moving to Python 3**

### Automatic changes

The first step has been that of using *2to3*, which is part of the Python 2 distribution, with the script *my2to3* (reported here), containing:  

    #!/bin/bash  
    2to3 -W "$1" > changes  
    mv changes "$1".changes  

e.g.  

    my2to3 "start 1 plainProgrammingBug.py"  

produces:

    start 1 plainProgrammingBug.py : the corrected file   
    start 1 plainProgrammingBug.py.bak : the backup of the previous .py file   
    start 1 plainProgrammingBug.py.changes : the list of the changes

The correction done in this way are mainly related to *print* and *input* statements

### Handmade modifications (in *$$slapp$$* folder)

##### convert_xls_txt.py

modified the sort criteria; it was  

    ll.sort(cmp=lambda x,y: cmp(x[0], y[0]))

but cmp is not implemented in Python 3, so a new way as been introduced,
using *key*, already existing in Python 2, with  

    ll.sort(key=lambda x: x[0])

##### Tools.py

*my2to3* has automatically modified the former *extractMethod* function, but that function is now completely different and named *extractMethodFromMethodFunction*

The reason is that in Python 3 the concept of unbound method no more exists and m of the class A in the form A.m is simply a function defined in A (or in parent class of A).

*extractMethod* was based on complicate code separating class and method in an unbound method, now instead the **\__qualname__** attribute simplifies the operation.

\__qualname__ applied to a simple function acts in the following way (interactive use of Python):

    >>> def f(x):
    	return x

    >>> f.__qualname__
    'f'

    On a function defined in a class:

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

In *applyMethod* we have now *space={}* and *exec* uses it.  

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

### Handmade modifications (in *basic* folder)

in *commonVar*

    toBeExecuted="print ('Goodbye')" # added () in print BY HAND
