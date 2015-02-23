=====================
Actions and Functions
=====================

Actions and functions are extremely important elements of GUIs. Actions and functions make things happen.

Actions
=======

*Actions* are the attributes for objects like *Buttons* and *MenuItems* that make them do things. For example::

 make Button quit with title "Stop", action quit.

will make a button that shuts down the program when clicked.

*quit* is one of a handful of default actions Gooey has created for you.

Write
-----

The *write* action will print a string to the terminal. After declaring the write action, add a string in double quotation marks, as follows::

 make Button b with action write "I'm a print statement".

Quit
----

The *quit* action closes the program.

Example::

 make Button b with action quit.


windowColorChange
-----------------

The *windowColorChange* action changes the color of the window. After declaring the *windowColorChange*, add a color value.

Example::

 make Button error with title "Error", action windowColorChange red.


Functions
=========

A function will let you *create your own actions*. The syntax for functions is as follows::

 function NAME(VARIABLE) does GOOEY_CODE; return VARIABLE.

A real example would look like this:

 function myFunction(win) does set win color green; return win.

This line of code means that the function named myFunction, which takes in an object *win*, will reset the window color to green. You need to return the object at the end for your changes to occur.

There are two ways to run your function. You can use the *run* command to run the function yourself::

 make Window w.
 function myFunction(win) does set win color green.
 run myFunction(w).

Alternatively, you can set the function as a Button.::

 make Window w.
 function myFunction(win) does set win color green; return win.
 make Button b with action myFunction w.
