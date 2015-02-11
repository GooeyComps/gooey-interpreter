
from enum import Enum

# Takes string names or int indices of a type and an attribute.
# Returns None if that type does not have that attribute.
# Else returns the default value for that attribute.
def getDefault(typeName, attrName):
    #Retrieve indices from type and attribute enums to access the correct entry in the matrix
    # Determine index of type

    if type(typeName) == int:
        typeIndex = typeName
    elif type(typeName) == str:
        typeNameStr = 'TypeName.'+typeName
        typeIndex = eval(typeNameStr).value

    else:
        print("Not a valid type")


    #Determine index of attribute
    if type(attrName) == int:
        attrIndex = attrName
    elif type(attrName) == str:
        attrNameStr = 'AttrName.'+attrName
        attrIndex = eval(attrNameStr).value

    else:
        print("Not a valid attribute")
    return matrix[attrIndex][typeIndex]


class TypeName(Enum):
    Window = 0
    Button = 1
    Checkboxes = 2
    RadioButtons = 3
    DropDown = 4
    Text = 5
    FormattedText = 6
    TextBox = 7
    Menu = 8
    MenuItem = 9
    Search = 10
    Image = 11

# class AttrName(Enum):
#     title = 0
#     options = 0
#     defaultText = 0
#     position = 0
#     size = 0
#     color = 0
#     action = 0
#     window = 0
#     hidden = 0
#     font = 0
#     fontSize = 0
#     textColor = 0
#     style = 0
#     source = 0
#     caption = 0

class AttrName(Enum):
    title = 0
    options = 1
    text = 2
    position = 3
    size = 4
    color = 5
    action = 6
    window = 7
    hidden = 8
    font = 9
    fontSize = 10
    textColor = 11
    style = 12
    source = 13
    caption = 14


matrix = [['"""Untitled Window"""', '"""Untitled Button"""', '"""Untitled Checkboxes"""', '"""Untitled Radio Buttons"""', '"""Untitled Drop Down"""', '*', '*', '"""Untitled Text Box"""', 'None', '"""Untitled Menu Item"""', '?', '?'],
['None', 'None', '"*""Option 1"" ""Option 2"" ""Option 3"""', '"*""Option 1"" ""Option 2"" ""Option 3"""', '"*""Option 1"" ""Option 2"" ""Option 3"""', 'None', 'None', 'None', '"""Menu Item 1"" ""Menu Item 2"" ""Menu Item 3"""', '"""Option 1"" ""Option 2"" ""Option 3"""', 'None', 'None'],
['None', 'None', 'None', 'None', 'None', 'None', 'None', '"""Type here"""', 'None', 'None', '"""Search"""', 'None'],
['None', 'T', 'T', 'T', 'T', 'T', 'None', 'T', '?', 'None', 'T', 'T'],
['T', 'T', '?', '?', '?', '?', 'None', 'T', '?', 'None', '?', 'T'],
['white', '*', 'None', 'None', 'None', 'white', 'None', 'None', 'None', 'None', 'None', 'None'],
['T', 'T', 'None', 'None', 'None', 'None', 'None', 'None', 'T', 'None', '?', 'None'],
['None', 'T', 'T', 'T', 'T', 'T', 'None', 'T', 'T', 'None', 'T', 'T'],
['False', 'False', 'False', 'False', 'False', 'False', 'None', 'False', 'False', 'False', 'False', 'False'],
['?', 'None', 'None', 'None', 'None', 'None', 'Times New Roman', 'None', 'None', 'None', 'None', 'None'],
['?', 'None', 'None', 'None', 'None', 'None', '12', 'None', 'None', 'None', 'None', 'None'],
['?', 'None', 'None', 'None', 'None', 'None', 'black', 'None', 'None', 'None', 'None', 'None'],
['?', 'None', 'None', 'None', 'None', 'None', '*', 'None', 'None', 'None', 'None', 'None'],
['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'T'],
['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', '"""A Beautiful Image"""']]

NUM_ATTRIBUTES = len(matrix)
NUM_TYPES = len(matrix[0])
