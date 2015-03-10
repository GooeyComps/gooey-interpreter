=======
Objects
=======

Objects are the building blocks of your GUI. Each object has a different set of uses, attributes, and functions.

Button
======

A button is a clickable object.

Example syntax::

 make Button b.
 make Button b with text "Hello".
 make Button b with text "Hello", position 100 25.
 set b action close.

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|text     | Words on button               | - A plaintext string              | "Untitled Button" |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of button on window  | - position keyword                | center            |
|         |                               | - integer pixels, separated by    |                   |
|         |                               |   space                           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of button                | - size keyword                    | medium            |
|         |                               | - width and height pixel integers,|                   |
|         |                               |   separated by a space            |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|action   | Effect when button clicked    | - name of Python or Gooey function| none              |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if button visible  | - true                            | false             |
|         | (false) or invisible (true)   | - false                           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+

Window
======

A window is the frame on which you create your GUI. The window is **always the first object you make**.

Example syntax::

 make Window w with size 500 500, color green.
 set w title "My favorite GUI".

Attributes:

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | The name as displayed in the  | - A plaintext string              | "Untitled Window" |
|         | top bar of the window.        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     |  The width and height of the  | - size keyword                    | medium            |
|         |  window                       | - width and height pixel integers,|                   |
|         |                               |   separated by a space            |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|color    | The color of the window       | - color keyword                   | white             |
|         | background                    | - rgb value, separated by spaces  |                   |
|         |                               |   (0 - 255)                       |                   |
|         |                               | - #hexvalue                       |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|action   | The effect from interacting   | - name of Python of Gooey function| none              |
|         | with a window.                |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|font     | The font for all text used in | - String name of available font   | Times New Roman   |
|         | the window                    |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|fontSize | Size of text                  | - Integer                         | 12                |
+---------+-------------------------------+-----------------------------------+-------------------+
|textColor| Color of text                 | - color keyword                   | black             |
|         |                               | - rgb value, separated by spaces  |                   |
+---------+-------------------------------+-----------------------------------+-------------------+


Checkboxes
==========

Checkboxes are square boxes the user can click on to select any number of options. If you create a Checkboxes object without the *options* attribute, it will have three default checkboxes labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before any of the attributes will mark that option to be selected by default.

Example syntax::

 make Checkboxes c with options "hello" "yellow" "fellow".
 set c position 20 20.

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above checkbox set       | - A plaintext string              | "Untitled         |
|         |                               |                                   | Checkboxes"       |
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The Checkboxes labels.        | - strings in double quotes,       | \*"Option 1"      |
|         |                               |   separated by a space            | "Option 2"        |
|         |                               | - string preceded by \* to        | "Option 3"        |
|         |                               |   mark default selections         |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of checkbox set in   |                                   | center            |
|         | window                        | - integer pixels, separated by    |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+



RadioButtons
============

RadioButtons are circular buttons a user can click to select **one** option out of many. If you create a RadioButtons object without the *options* attribute, it will have three default buttons labeled "Option 1", "Option 2", and "Option 3". Placing an asterisk before one of the attributes will make that option to be selected by default.

Example syntax::

 make RadioButtons r with options "hello" "mello" "jello".
 set r title "Choose one:".

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|title    | text above RadioButtons set   | - A plaintext string              | "Untitled         |
|         |                               |                                   | RadioButtons"     |
+---------+-------------------------------+-----------------------------------+-------------------+
|options  | The RadioButtons labels.      | - strings in double quotes,       | \*"Option 1"      |
|         |                               |   separated by a space            | "Option 2"        |
|         |                               | - string preceded by \* to        | "Option 3"        |
|         |                               |   mark default selected           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of RadioButtons set  | - position keyword                | center            |
|         | in window                     | - integer pixels, separated by    |                   |
|         |                               |   by space                        |                   |
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
|         |                               | - integer pixels, separated by    |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of text                  | - size keyword                    | medium            |
|         |                               | - width and height integers,      |                   |
|         |                               |   separated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|color    | color of text                 | - color keyword                   | black             |
|         |                               | - rgb value, separated by spaces  |                   |
|         |                               |   (0 - 255)                       |                   |
|         |                               | - #hexvalue                       |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if text            | - true                            | false             |
|         | visible (false) or invisible  | - false                           |                   |
|         | (true)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+

TextBox
=======

TextBox objects create a space where users can type. When you create a TextBox with a *text* attribute, the value entered will appear as default text within the text box.

When setting the *size* of the TextBox using integers for width and height, the integers will set the width and height by **character count**. For example, size 15 10 will create a TextBox 15 *characters* across, with ten *lines* of height.

Example syntax::

 make TextBox tb with text "Write your answer here".
 set tb size large.

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|text     | mutable words within the      | - A plaintext string              | "Type Here"       |
|         | TextBox                       |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|position | location of TextBox in window | - position keyword                | center            |
|         |                               | - integer pixels, separated by    |                   |
|         |                               |   by space                        |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of TextBox               | - size keyword                    | medium            |
|         |                               | - width and height pixel integers,|                   |
|         |                               |   separated by space              |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|hidden   | Determines if TextBox         | - true                            | false             |
|         | visible (false) or invisible  | - false                           |                   |
|         | (true)                        |                                   |                   |
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
|         |                               |   separated by spaces             | menuItem2         |
|         |                               |                                   | menuItem3         |
|         |                               |                                   |                   |
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


Image
=====

Images are pictures you can add your your Gooey. The image must be in **.gif format** although the movement will not be maintained.

Example syntax::

 make Image i with title "Apple", text "This is my most favorite apple", source "apple.gif".

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|hidden   | Determines if Image           | - true                            | false             |
|         | visible (false) or invisible  | - false                           |                   |
|         | (true)                        |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|source   | path or filename of Image     | - image file in .gif format       | defaultIcon       |
+---------+-------------------------------+-----------------------------------+-------------------+

FormattedText
=============

FormattedText is an object that stores values for a text with different formatting options. It is first created by the user with attributes of their choice and then can be used in button text, checkboxes/radiobutton titles, and text objects.

Example syntax::

 make FormattedText t with text "Hello World!", font "Arial", size 15, color blue, bold true, italic true, underline true.
 make Button b with text t.
 make Checkboxes c with title t, options "Yay" "Nay", position 50 50, size medium.

+---------+-------------------------------+-----------------------------------+-------------------+
|Attribute| Description                   | Possible Values                   | Default Value     |
+=========+===============================+===================================+===================+
|text     | text to be stored in object   | - A plaintext string              | "Untitled Text"   |
+---------+-------------------------------+-----------------------------------+-------------------+
|font     | font of text                  | - A plaintext string: "Times",    | "Times"           |
|         |                               |   "Arial"/"Helvetica", "Courier"  |                   |
|         |                               |   "Comic Sans MS", "MS Sans Serif"|                   |
|         |                               |   "MS Serif", "Verdana"           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|color    | color of text                 | - color keyword                   | black             |
|         |                               | - rgb value, separated by spaces  |                   |
|         |                               |   (0 - 255)                       |                   |
|         |                               | - #hexvalue                       |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|size     | size of text                  | - integer (pt size)               | 12                |
+---------+-------------------------------+-----------------------------------+-------------------+
|bold     | Determines if the text is     | - true                            | false             |
|         | bold (true) or not (false)    | - false                           |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|italic   | Determines if the text is     | - true                            | false             |
|         | italicized (true) or not      | - false                           |                   |
|         | (false)                       |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
|underline| Determines if the text is     | - true                            | false             |
|         | underlined (true) or not      | - false                           |                   |
|         | (false)                       |                                   |                   |
+---------+-------------------------------+-----------------------------------+-------------------+
