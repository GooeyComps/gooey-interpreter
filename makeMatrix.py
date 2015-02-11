import sys

# Takes a csv file in the following format

'''
|-------------------------------------------|-----------------|
|___________|   TypeName1   |   TypeName2   | Possible Values |
| AttrName1 | DefaultValueA | DefaultValueB |    Poss Val 1   |
| AttrName2 |               | DefaultValueD |    Poss Val 2   |
| AttrName3 | DefaultValueE | DefaultValueF |    Poss Val 3   |
|-------------------------------------------|-----------------|
'''

# And writes a new python file in this format

'''
from enum import Enum

class TypeName(Enum):
    TypeName1 = 0
    TypeName2 = 1
    # . . .

class AttrName(Enum):
    AttrName1 = 0
    AttrName2 = 1
    # . . .

matrix = [[DefaultValueA, DefaultValueB],
          [None,          DefaultValueD],
          [DefaultValueE, DefaultValueF]]

getDefault(typeName, attrName):
    . . .

'''

# Usage:
# python makeMatrix.py "InputFilename.csv" "OutputFilename.py"

if (len(sys.argv)) < 3:
    infile_name = raw_input("Input Filename: ")
    outfile_name = raw_input("Output Filename: ")
else:
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]

# Open and read input file
infile = open(infile_name)
infile_split = infile.readlines()
infile.close()

# Split the input file into a 2D list (first by newlines then by commas)
for line in range(len(infile_split)):
    infile_split[line] = infile_split[line].split(',')

# Start a string that will contain our final program
progStr = """
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

"""

# Construct the Type Enumeration from list of Types
progStr += """
class TypeName(Enum):
"""

typeList = []
typeNum = 0
for typeName in infile_split[0][1:]:
    progStr += "    " + typeName.strip() + " = " + str(typeNum) + "\n"
    typeNum += 1


# Construct the Attribute Enumeration from list of Attributes
progStr += """
class AttrName(Enum):
"""

attrList = []
attrNum = 0
for attrLine in infile_split[1:]:
    attrName = attrLine[0]
    progStr += "    " + attrName.strip() + " = " + str(attrNum) + "\n"
    attrNum += 1

# Construct final matrix of Types/Values/Defaults

# Construct cleaned-up list
outlist = []
attrNum, typeNum = 0, 0
for row in infile_split[1:]:
    line = []
    for col in row[1:]:
        if type(col) == str:
            col = col.strip()
        if not col:
            col = None
        line.append(col)
    outlist.append(line)

# Add the list as a string to the program string
progStr += "\nmatrix = "
progStr += "["
for line in outlist:
    progStr += "["
    for item in line:
        progStr += "'"
        progStr += str(item)
        progStr += "', "
    progStr = progStr[:-2]
    progStr += "],\n"
progStr = progStr[:-2]
progStr += "]"

progStr += """

NUM_ATTRIBUTES = len(matrix)
NUM_TYPES = len(matrix[0])
"""

# Write the completed program string to the output file
outfile = open(outfile_name, "w")
outfile.write(progStr)
outfile.close()
