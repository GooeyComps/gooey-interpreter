===============
Getting Started
===============

Language Basics
===============

The Gooey GUI language was designed to be easy! Our goal was to make coding look less like code, and more like an English sentence. There are a few basic rules to follow, and then you’ll be on your way.

Normally, each line starts with either **make** or **set**.

As Gooey attempts to simulate english, each line of Gooey **ends with a period**.

Make Commands
=============

You can use the *make* command to create and add new elements to your GUI. 

*make* commands always have the same basic syntax. Typing::
 
 make Object name.
 
will create a new object of the given type with its default values. 

Alternatively, the syntax::

 make OBJECT NAME with 
 ATTRIBUTE value. 
 
will create the object with most of the defaults, with one attribute modification that you specify.

You can add as many attributes as you want in the *make* command, by **separating the attributes with commas**. The syntax this time might look like::

 make OBJECT NAME with 
 ATTRIBUTE VALUE, 
 ATTRIBUTE VALUE,  
 ATTRIBUTE VALUE.

The command *make* is always followed by the type of **object** you want to make. Types of objects always start with capital letters and might include:

- Window

- Button

- Menu

- Text

- Checkbox

And so on.

Set Commands
============

If you choose to use the live Gooey editor, you might want to modify your objects after making them. *set* commands allow you to change any attributes for objects you have already created.

The *set* command syntax is::

 set NAME ATTRIBUTE VALUE.
    
You can also set multiple attributes of a single objects by using commas::

 set NAME ATTRIBUTE VALUE, ATTRIBUTE VALUE, ATTRIBUTE VALUE.

Variable Names
==============

After the object comes the **variable name**. Your object has to start with a lowercase letter, be only one word long, and contain only letters, numbers, or underscore _. 
Valid variable names include:

- ``myvariable``
- ``myVariable2``
- ``mINE``
- ``not_yours``
- ``o_o``

These variable names are NOT valid:

- ``my variable``
- ``MyVariable``
- ``mINE!``
- ``\(^-^)/``

Attributes and Values
=====================

**Attributes** are a variety of customizable components of your object.  Common attributes include:

- size
- color
- text
- position

Some objects may have additional unique attributes.

There are a lot of attributes where commonly desired **values** are preset for you, like the *size* attribute has default values of *small*, *medium*, and *large*. However, for your custom needs, you can also set your own size numerically. So, ``size large`` and ``size 455`` are both legal ways to define the size. 
 
Syntax Example
==============

**In summary**, to create a button, say::

 make Button mybutton.
    
To create a button with the words “Yes” on it, type::

 make Button mybutton with 
 text “Yes”.
 
And to create a big button with the words “Yes”, type::

 make Button mybutton with 
 text “Yes”, 
 size large. 
 
Now you’re ready to start making your own Gooey GUI!
