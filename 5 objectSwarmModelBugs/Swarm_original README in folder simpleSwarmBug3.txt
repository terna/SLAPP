// simpleSwarmBug3

               LOADING AND SAVING PARAMETERS

main.m

Only a small change here. By now, we're tired of altering the default
parameters in the code and then recompiling each time. 

In main(), we take advantage of an the default `lispAppArchiver'
global singleton variable to read in the state variables of the
ModelSwarm from a file.  Every Swarm application has an instance of
the `lispAppArchiver', by default, the `lispAppArchiver' looks for a
file with the name <appname>.scm.

In this case, <appname> = `bug', so the expected filename is
`bug.scm'.

[Note: If this file does not exist all call to the `lispAppArchiver'
will return `nil'.  See the `mousetrap' application to see how to use
the Archiver feature with alternative filenames].

Each file can have as many named objects as the user wishes (the user
has control over the names, which are simply strings).

Now, we can change the parameters of the model by editing the file
`bug.scm', which has a simple Lisp-like format:

(list 
 (cons 'modelSwarm
       (make-instance 'ModelSwarm
                      #:worldXSize 80
                      #:worldYSize 80
                      #:seedProb 0.9F0
                      #:bugDensity 0.01F0)))

So, we name the copy of the object `modelSwarm', and ask it to
`make-instance' of the class `ModelSwarm' with the instance variables
as described.  [Note the special `F0' after the end of the number,
this is to tell Archiver to create a `float' instance variable rather
than `double', which is what it will do by default.]

In main.m we simply `ask' the Archiver to create a copy of the object
with the name `modelSwarm', the lispAppArchiver takes care of the
instantiation of the object (i.e. running the createBegin/createEnd on
the object) internally.

[The `lispAppArchiver' can also write the object state back to a file,
with the `putShallow:' and `putDeep:' methods.  Not discussed here].



NEXT -> simpleObserverBug



