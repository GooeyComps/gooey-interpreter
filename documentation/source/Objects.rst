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
 make Button b with text "Hello", position 3 5.
 set b action close.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | Text above the button         | - A plaintext string              | none              |
+---------+-------------------------------+-----------------------------------+-------------------+
|text     | Words on button               | - A plaintext string              | "Untitled Button" |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of button on window  | - position keyword                | center            |
|         |                               | - integer coordinate, seperated by|                   |
|         |                               |   space                           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of button                | - size keyword                    | medium            |
|         |                               | - Height and width integers,      |                   |
|         |                               |   seperated by a space            |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|action   | Effect when button clicked    | - name of Python or Gooey function| none              |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if button visible  | - True                            | False             |
|         | (False) or invisible (True)   | - False                           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+ 

Window
======

A window is the frame on which you create your GUI. The window is **always the first object you make**.

Example syntax::

 make Window w with size (10,10), color green.
 set w title "My favorite GUI".

Attributes:

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | The name as displayed in the  | - A plaintext string              | "Untitled Window" |
|         | top bar of the window.        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     |  The width and height of the  | - size keyword                    | medium            |
|         |  window                       | - Height and width integers,      |                   |
|         |                               |   separated by a space            |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|color    | The color of the window       | - color keyword                   | white             |
|         | background                    | - rgb value, sperated by spaces   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|action   | The effect from interacting   | - name of Python of Gooey function| none              |
|         | with a window.                |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if window is       | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|font     | The font for all text used in | - String name of avaliable font   | Times New Roman   |
|         | the window                    |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|fontSize | Size of text                  | - Integer                         | 12                |
+---------+-------------------------------+-----------------------------------+-------------------+
|textColor| Color of text                 | - color keyword                   | black             |
|         |                               | - rgb value, seperated by spaces  |                   |
+---------+-------------------------------+-----------------------------------+-------------------+


Checkboxes
==========

Checkboxes are square boxes the user can click on to select any number of options. If you create a Checkbox object without the *options* attribute, it will have three default checkboxes labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before any of the attributes will mark that option to be selected by default. 

Example syntax::

 make Checkbox c with options "hello" "yellow" "fellow".
 set c position (2,2).
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above checkbox set       | - A plaintext string              | "Untitled         |
|         |                               |                                   | Checkboxes"       |
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The checkbox labels.          | - strings in double quotes,       | \*"Option 1"      |
|         |                               |   seperated by a space            | "Option 2"        |
|         |                               | - string preceeded by \* to       | "Option 3"        |
|         |                               |   mark default selections         |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of checkbox set in   | - position keyword                | center            |
|         | window                        | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of checkbox set          | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if checkboxes      | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
 

RadioButtons
============

Radio Button are circular buttons a user can click to select **one** option out of many. If you create a RadioButton object without the *options* attribute, it will have three default buttons labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before one of the attributes will make that option to be selected by default. 

Example syntax::

 make RadioButton r with options "hello" "mello" "jello".
 set r title "Choose one:".
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above RadioButon set     | - A plaintext string              | "Untitled         |
|         |                               |                                   | RadioButtons"     |
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The RadioButton labels.       | - strings in double quotes,       | \*"Option 1"      |
|         |                               |   seperated by a space            | "Option 2"        |
|         |                               | - string preceeded by \* to       | "Option 3"        |
|         |                               |   mark default selected           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of RadioButton set in| - position keyword                | center            |
|         | window                        | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of RadioButton set       | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if RadioButtons    | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
 

Dropdown
========

Dropdown Menus allow the user to choose one option from pop-down list. If you create a Dropdown object without the *options* attribute, it will have three default options in the list labeled "Option 1", "Option 2", and "Option 3". 

Example syntax::

 make Dropdown with options "hello" "cello" "othello".
 set d position bottomleft.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above Dropdown menu      | - A plaintext string              | "Untitled         |
|         |                               |                                   | Dropdown"         |
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The Drowdown labels.          | - strings in double quotes,       | \*"Option 1"      |
|         |                               |   seperated by a space            | "Option 2"        |
|         |                               | - string preceeded by \* to       | "Option 3"        |
|         |                               |   mark default selected           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of Dropdown menu in  | - position keyword                | center            |
|         | window                        | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of Dropdown menu         | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if Dropdown menu   | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
  

Text
====

Text is a simple text region the user *cannot* interact with. 

Example syntax::
 
 make Text t with text "Welcome to Gooey! Please leave your shoes at the door."
 set t color blue.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|text     | unmutable words in a window   | - A plaintext string              | "Text"            |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of text in window    | - position keyword                | center            |
|         |                               | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of text                  | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|color    | color of text                 | - color keyword                   | black             |
|         |                               | - rgb value, seperated by spaces  |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if text            | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+ 

TextBox
=======

TextBox objects create a space where users can type. When you create a TextBox with a *text* attribute, the value entered will appear as defualt text within the text box.

Example syntax::

 make TextBox tb with text "Write your answer here".
 set tb size large.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above TextBox            | - A plaintext string              | "Untitled TextBox"|
+---------+-------------------------------+-----------------------------------+-------------------+
|text     | mutable words within the      | - A plaintext string              | "Type Here"       |
|         | TextBox                       |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of TextBox in window | - position keyword                | center            |
|         |                               | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of TextBox               | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if TextBox         | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+ 
 

Menu
====

Menus are a list of actions. Menu's are created with Menu Items. When creating a Menu, the *options* attribute points to the MenuItems to be included in the Menu. A Menu *must* include MenuItems.

Example syntax::

 make Menu m with options file edit.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|options  | The top level menu labels     | - list of MenuItem objects        | menuItem1         |
|         |                               |   seperated by spaces             | menuItem2         |
|         |                               |                                   | menuItem3         |
|         |                               |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if menu is         | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+


MenuItem
========

MenuItems are the terminal actions in a Menu. The variable name of the MenuItem must match the name of the correlating option listed in the Menu object. With the *options* attribute, MenuItems have two parts. First the text the user will select, then a colon, followed by the action.

Example syntax::

 make MenuItem file with options "quit":close.
 
+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | name visible in menu          | - A plaintext string              |"Untitled MenuItem"|
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The selections within the menu| - a MenuItem object               | "Option1"         |
|         |                               | - a terminal in the format        | "Option2"         |
|         |                               |   "name":action                   | "Option3"         |
|         |                               |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if MenuItem is     | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
 

Image
=====

Images are pictures you can add your your Gooey. The image must be in **.gif format** although the movement will not be maintained. 

Exampel syntax::

 make Image i with title "Apple", text "This is my most favorite apple", source "apple.gif".

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above Image              | - A plaintext string              | none              |
+---------+-------------------------------+-----------------------------------+-------------------+
|text     | Caption below the Image       | - A plaintext string              | "Image Caption"   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of Image in window   | - position keyword                | center            |
|         |                               | - integer coordinate, seperated   |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of Image                 | - size keyword                    | medium            |
|         |                               | - height and width integers,      |                   |
|         |                               |   seperated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if Iamge           | - True                            | False             |
|         | visible (False) or invisible  | - False                           |                   |
|         | (True)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+ 
|source   | path orfilename of Image      | - image file in .gif formar       | defaultIcon       |
+---------+-------------------------------+-----------------------------------+-------------------+ 
  
