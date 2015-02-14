import sys

# Takes a csv file in the following format

# |-------------------------------------------|
# |           |   Type Name   |   Type Name   |
# | Attr Name | Default Value | Default Value |
# | Attr Name | Default Value | Default Value |
# | Attr Name | Default Value | Default Value |
# |-------------------------------------------|

# And writes a new csv file in this format

# |---------------------------------------|
# | Type Name | Attr Name | Default Value |
# |           | Attr Name | Default Value |
# |           | Attr Name | Default Value |
# | Type Name | Attr Name | Default Value |
# |           | Attr Name | Default Value |
# |           | Attr Name | Default Value |
# |---------------------------------------|

# Usage:
# python formatCSV.py "InputFilename.csv" "OutputFilename.csv"

if (len(sys.argv)) < 3:
    infile_name = raw_input("Input Filename: ")
    outfile_name = raw_input("Output Filename: ")
else:
    infile_name = sys.argv[1]
    outfile_name = sys.argv[2]

# Open and read input file
infile = open(infile_name)
infile_list = infile.readlines()
infile.close()

# Split the input file into a 2D list (first by newlines then by commas)
infile_split = infile_list[0].split('\r')

for line in range(len(infile_split)):
    infile_split[line] = infile_split[line].split(',')

# Construct a 2D list in new format for new CSV file
outlist = []

# For each object type, append each attribute it possesses to its entry in the new csv file
# along with its default value
for col in range(1, len(infile_split[0]) - 1):
    first = True
    for row in range(1, len(infile_split)):
        if infile_split[row][col]:
            object_name = infile_split[0][col]
            attr_name = infile_split[row][0]
            default_val = infile_split[row][col]
            if first:
                outlist.append([object_name, attr_name, default_val])
                first = False
            else:
                outlist.append(['', attr_name, default_val])

outfile = open(outfile_name, "w")

outfile.write("Type, Attribute, Default Value\n")

for row in outlist:
    for col in row[:-1]:
        outfile.write(col)
        outfile.write(',')
    outfile.write(row[-1])
    outfile.write('\n')

outfile.close()
