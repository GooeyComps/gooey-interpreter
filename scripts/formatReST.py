import sys

'''
Takes a csv file in the following format

|-----------------------------------------------------------------------|
|           |    Type Name    |    Type Name    |...|  Possible Values  |
| Attr Name | Default Value A | Default Value B |...| Possible Values A |
| Attr Name | Default Value C | Default Value D |...| Possible Values B |
| Attr Name | Default Value E | Default Value F |...| Possible Values C |
|-----------------------------------------------------------------------|

and writes a new ReStructuredText (ReST) file documenting the types and
attributes in the input file, creating a section for each type, with an
attributes subsection containing a table with all the available attributes,
with a description, all their possible values, and their default values.
'''

# Usage:
# python formatReST.py "InputFilename.csv" "OutputFilename.rst"

# Constants and Options
gapWidth = 2
gap = ' '*gapWidth
colNames = ['Attribute','Description', 'Possible Values', 'Default Value']
colWidths = [11, 20, 35, 20]
assert(len(colNames) == len(colWidths))
numCols = len(colNames)

def splitIntoFixedWidthLines(inputStr, width):
    '''
    Function to split a string into lines of the given width
    (with padding on the right to fill the given space).
    Takes a string inputStr and an int width. Returns a list of strings.
    '''
    words = inputStr.strip('\n').split(' ')
    lines = []
    line = []
    # For each word, add it to the current line if it will fit,
    # else, start a new line and add there.
    for word in words:
        # length of current line so far + 1 (for a space) + length of next word
        if len(' '.join(line)) + 1 + len(word) <= width:
            line.append(word)
        else:
            lines.append(line)
            line = [word]
    # append new line to 
    if len(line) > 0:
        lines.append(line)
    for l in range(len(lines)):
        lines[l] = ' '.join(lines[l])
        lines[l] += ' '*(width-len(lines[l]))
    return lines

def main():
    # Get input and output file names
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

    # Construct a string that will contain the output in ReStructuredText format
    restFileStr = ''
    restFileStr += '#######\n'
    restFileStr += 'Objects\n'
    restFileStr += '#######\n'
    restFileStr +=  '\n'

    # Make the border of '=' around the first row of the attributes table
    tableBorder = ''
    for col in range(numCols):
        width = colWidths[col]
        tableBorder += ('='*width) + gap
    tableBorder += '\n'

    '''
    Make the first row of the attributes table in the form:
    ========  ========  ...
    heading1  heading2  ...
    ========  ========  ...
    '''
    tableHeading = ''
    tableHeading += tableBorder
    for col in range(numCols):
        name = colNames[col]
        width = colWidths[col]
        tableHeading += name
        tableHeading += ' '*(width-len(name))
        tableHeading += gap
    tableHeading += '\n'
    tableHeading += tableBorder

    # make an entry for each type in the input csv table
    for col in range(1, len(infile_split[0])-1):
        # add title with overline and underline
        title = str(infile_split[0][col])
        underoverline = '*'*len(title)
        restFileStr += underoverline + '\n'
        restFileStr += title + '\n'
        restFileStr += underoverline + '\n'
        restFileStr += '\n'
        # construct Attributes subsection
        restFileStr += 'Attributes\n'
        restFileStr += '==========\n'
        restFileStr += '\n'
        # make attributes table
        restFileStr += tableHeading
        for row in range(1, len(infile_split)):
            attr = str(infile_split[row][0])
            possValues = str(infile_split[row][-1])
            defaultValue = str(infile_split[row][col])
            if defaultValue:
                possValues = splitIntoFixedWidthLines(possValues, colWidths[2])
                defaultValue = splitIntoFixedWidthLines(defaultValue, colWidths[3])
                for line in range(max(len(possValues), len(defaultValue))):
                    # Attributes column: attr name on first line, subsequent lines empty
                    if line>0:
                        restFileStr += ' '*(colWidths[0])
                        restFileStr += gap
                    else:
                        restFileStr += attr
                        restFileStr += ' '*(colWidths[0]-len(attr))
                        restFileStr += gap
                    #Description column (empty)
                    restFileStr += ' '*colWidths[1]
                    restFileStr += gap
                    #Possible Values column
                    if line<len(possValues):
                        restFileStr += possValues[line]
                        restFileStr += gap
                    #Default Value column
                    if line<len(defaultValue):
                        restFileStr += defaultValue[line]
                        restFileStr += gap
                    #Don't forget the line break!
                    restFileStr += '\n'
        # Add bottom border
        restFileStr += tableBorder + '\n'

    # Write ReST string to output file
    outfile = open(outfile_name, "w")
    outfile.write(restFileStr)
    outfile.close()

main()