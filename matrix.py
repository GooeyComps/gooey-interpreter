
from enum import Enum

# Takes string names or int indices of a type and an attribute.
# Returns None if that type does not have that attribute.
# Else returns the default value for that attribute.
def getDefault(typeName, attrName):
    # Determine index of type
    if type(typeName) == int:
        typeIndex = typeName
    elif type(typeName) == str:
        typeNameStr = 'TypeName.'+typeName
        typeIndex = eval(typeNameStr).value
    else:
        print("Oops, typeName arg is of the wrong type.")

    #Determine index of attribute
    if type(attrName) == int:
        attrIndex = attrName
    elif type(attrName) == str:
        attrNameStr = 'AttrName.'+attrName
        attrIndex = eval(attrNameStr).value
    else:
        print("Oops, attrName arg is of the wrong type.")

    #Retrieve and return default value for given type and attribute
    return matrix[attrIndex][typeIndex]


class TypeName(Enum):
    Window = 0
    Button = 1
    Checkboxes = 2
    RadioButtons = 3
    Text = 4
    FormattedText = 5
    TextBox = 6
    Menu = 7
    MenuItem = 8
    Image = 9

class AttrName(Enum):
    title = 0
    text = 1
    options = 2
    menuoption = 3
    position = 4
    size = 5
    color = 6
    action = 7
    hidden = 8
    font = 9
    fontSize = 10
    textColor = 11
    bold = 12
    italics = 13
    underline = 14
    source = 15

matrix = [["""Untitled Window""", None, """Untitled Checkboxes""", """Untitled Radio Buttons""", None, None, """Untitled Text Box""", None, """Untitled Menu Item""", """"""],
[None, """Untitled Button""", None, None, """Text""", """Formatted Text""", """Type here""", None, None, """Image Caption"""],
[None, None, "*""Option 1"" ""Option 2"" ""Option 3""", "*""Option 1"" ""Option 2"" ""Option 3""", None, None, None, None, None, None],
[None, None, None, None, None, None, None, 'menuItem1 menuItem2 menuItem3', """Option 1"" ""Option 2"" ""Option 3""", None],
[None, 'center', 'center', 'center', 'center', None, 'center', None, None, 'center'],
['medium', 'medium', 'medium', 'medium', 'medium', None, 'medium', None, None, 'medium'],
['white', None, None, None, 'white', None, None, None, None, None],
["""""", """""", None, None, None, None, None, None, None, None],
[False, False, False, False, False, None, False, False, False, False],
[None, None, None, None, None, """Times New Roman""", None, None, None, None],
[None, None, None, None, None, 12, None, None, None, None],
[None, None, None, None, None, 'black', None, None, None, None],
[None, None, None, None, None, False, None, None, None, None],
[None, None, None, None, None, False, None, None, None, None],
[None, None, None, None, None, False, None, None, None, None],
[None, None, None, None, None, None, None, None, None, 'defaultIcon']]

NUM_ATTRIBUTES = len(matrix)
NUM_TYPES = len(matrix[0])
