==========
Attributes
==========

Attributes control the details of each Object you create. Not all Objects can have the same attributes, and some attributes are specific to one or two Objects.

Each attribute needs a *value*. Some attributes accept values in multiple different formats. 

Title
=====

A title generally creates text *above* the Object.

In a **window**, a title will put a name at the very top bar across the application window.

Values:

- A plaintext string

Text
====

Text will generally create words on top of or inside the object. 

Values:

- A plaintext string

Options
=======

Options will generally be a list describing the different Checkboxes, RadioButtions, or Menu/MenuItems.

Values:

- A space seperated list of plaintext strings surrounded by double quotation marks. 
    + Example: "Option1" "Option2" "Option3"
 
- For *Checkboxes*, an \* before **one or more** of the strings will create those values automatically checked
    + Example: \*"Option1" "Option2" \*"Option3"
 
- For *RadioButtons* an \* before **one** of the strings will create that value automatically selected
    + Example "Option1" \*"Option2" "Option3"

Position
========

Position allows you to move your objects around the window. If you want to set the position  of an Object, you must first set the size of the of the Window. 

Values:

- A position keyword
    + center
    + top
    + bottom
    + left
    + right
    + topleft
    + topright
    + bottomleft
    + bottomright
    
- Height and width integer coordinates, seperated by a space.
    + Example: position 3 5


Size
====

Size allows for the adjustment of the height and width of the object.

Values:

- A size keyword
    + small
    + medium
    + large
    
- Height and Width integers, seperated by a space.
    + Example: size 2 5

Color
=====

Color changes the color of the object. 

Values:

- A color keyword
    + red
    + blue
    + yellow
    + orange
    + green
    + purple
    + pink
    + cyan
    + magenta
    + white
    + black

- A RGB value, seperated by spaces.
    + Example: color 000 000 255.
    
- A hex value
    + Example: color #33aa00

Action
======

Action sets the events that happen after an object is interacted with.

Values:

- A built-in Gooey action:
    + quit
    + write
    + changeWindowColor
    + changeWindowSize
    
- A custom function:
    + See: Functions and Actions

Hidden
======

Determines if object can be seen. Default is **always False**, obejct is *not* hidden. Setting hidden to True will hide the Object without destorying it.

Values:

- True
- False

Font
====

Changes font used if Object incorporates text. Default is "Times New Roman"

Values:

- A font name, surrounded by double quotation marks.
    + "Times New Roman"


FontSize
========

Changes font size used if Object incorporates text.

textColor
=========

Changes color of text if Object incorporates text. 

bold
====

Changes text to bold font when set to True. Default is **False**.

Values:

- True
- False

italics
=======

Changes text to italicized font when set to True. Default is **False**.

Values:

- True
- False

source
======

The path or filename for the Image object. Source files **must be in .gif format**

Values:

- filename surrounded by double quotation marks
    + Example: source "apple.gif"
