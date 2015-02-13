===============
Getting Started
===============


What is Gooey?
==============

Gooey is a tool for quick and easy creation of Graphical User Interfaces (GUIs). A GUI is the layout of an application - the buttons, the menus, the style, and so on. GUIs are notoriously troublesome to make, even for experienced programmers. The language was designed for people who have very little experience coding, and so is designed to look more like an English sentence than long blocks of code. 

Language Basics
===============

The Gooey GUI language was designed to be easy! Our goal was to make coding look less like code, and more like an English sentence. There are a few basic rules to follow, and then you’ll be on your way.

Normally, each line starts with either **make** or **set**.

Each line of Gooey **ends with a period**.

You can use the *make* command to create and add new elements to your GUI. 


*make* commands always have the same basic syntax. Typing::
 
 make Object name.
 
will create a new object of the given type with its default values. 

The command *make* is always followed by the type of **object** you want to make. Types of objects always start with capital letters and might include:

- Window

- Button

- Menu

- Text

- Checkbox

And so on.

After the object comes the **name**. Your object has to start with a lowercase letter, be only one word long, and contain only letters, numbers, or underscore _. 
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

You can also modify the default attributes as you make an object.  The syntax::

 make OBJECT NAME with 
 ATTRIBUTE value. 
 
will create the object with most of the defaults, with one attribute modification that you specify.

You can add as many attributes as you want in the *make* command, by separating the attributes with commas. The syntax this time might look like::

 make OBJECT NAME with 
 ATTRIBUTE VALUE, 
 ATTRIBUTE VALUE,  
 ATTRIBUTE VALUE.

The *set* command syntax is::

 set NAME ATTRIBUTE VALUE.
    
You can also set multiple attributes of a single objects by using commas::

 set NAME ATTRIBUTE VALUE, ATTRIBUTE VALUE, ATTRIBUTE VALUE.
 
**Attributes** are a variety of customizable components of your object.  Common attributes include:

- size
- color
- text
- position

Some objects may have additional unique attributes.

There are a lot of attributes where commonly desired **values** are preset for you, like the *size* attribute has default values of *small*, *medium*, and *large*. However, for your custom needs, you can also set your own size numerically. So, ``size large`` and ``size 455`` are both legal ways to define the size. 

**In summary**, to create a button you would say::

 make Button mybutton.
    
To create a button with the words “Yes” on it, you would type::

 make Button mybutton with 
 text “Yes”.
 
And to create a big button with the words “Yes”, you would type::

 make Button mybutton with 
 text “Yes”, 
 size large. 
 
 Now you’re ready to start making your own Gooey GUI!
