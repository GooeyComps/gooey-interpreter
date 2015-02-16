=======
Objects
=======

Objects are the builing blocks of your GUI. Each object has a differnet set of uses, attributes, and functions.
   
Button
======

A button is a clickable object. 

Example syntax::

 make Button b.
 make Button b with text "Hello".
 make Button b with text "Hello", position (3,5).
 set b action close.

Window
======

A window is the frame on which you create your GUI. The window is **always the first object you make**.

Example syntax::

 make Window w with size (10,10), color green.
 set w title "My favorite GUI".

Attributes:

===========  ====================  ===================================  ====================  
Attribute    Description           Possible Values                      Default Value         
===========  ====================  ===================================  ====================  
title                              A plaintext string | A               """Untitled    
                                   FormattedText object                 Window"""             
size                               A string description of the size     medium                
                                   (or keyword?); The (x y) dimensions  
                                   separated by a space                 
color                              A string description of the color    white                 
                                   (or keyword?); An rgb value          
                                   separated by spaces                  
action                             The name of a Python or Gooey        """"""                
                                   function to call when the object is  
                                   acted upon                           
hidden                             A boolean indicating whether the     False                 
                                   object is hidden (True | true |      
                                   False | false)                       
font                               The string name of a font available  """Times New          
                                   in Gooey                             Roman"""              
fontSize                           A number indicating the font size    12                    
textColor                          A color (A string description or an  black                 
                                   rgb value)                           
===========  ====================  ===================================  ====================  


Checkboxes
==========

Checkboxes are square boxes the user can click on to select any number of options. If you create a Checkbox object without the *options* attribute, it will have three default checkboxes labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before any of the attributes will mark that option to be selected by default. 

Example syntax::

 make Checkbox c with options "hello" "yellow" "fellow".
 set c position (2,2).

RadioButtons
============

Radio Button are circular buttons a user can click to select **one** option out of many. If you create a RadioButton object without the *options* attribute, it will have three default buttons labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before one of the attributes will make that option to be selected by default. 

Example syntax::

 make RadioButton r with options "hello" "mello" "jello".
 set r title "Choose one:".

Dropdown
========

Dropdown Menus allow the user to choose one option from pop-down list. If you create a Dropdown object without the *options* attribute, it will have three default options in the list labeled "Option 1", "Option 2", and "Option 3". 

Example syntax::

 make Dropdown with options "hello" "cello" "othello".
 set d position bottomleft.

Text
====

Text is a simple text region the user *cannot* interact with. 

Example syntax::
 
 make Text t with text "Welcome to Gooey! Please leave your shoes at the door."
 set t color blue.

TextBox
=======

TextBox objects create a space where users can type. When you create a TextBox with a *text* attribute, the value entered will appear as defualt text within the text box.

Example syntax::

 make TextBox tb with text "Write your answer here".
 set tb size large.

Menu
====

Menus are a list of actions. Menu's are created with Menu Items. When creating a Menu, the *options* attribute points to the MenuItems to be included in the Menu. A Menu *must* include MenuItems.

Example syntax::

 make Menu m with options file edit.

MenuItem
========

MenuItems are the terminal actions in a Menu. The variable name of the MenuItem must match the name of the correlating option listed in the Menu object. With the *options* attribute, MenuItems have two parts. First the text the user will select, then a colon, followed by the action.

Example syntax::

 make MenuItem file with options "quit":close.
