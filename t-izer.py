#from stack import *
from token import *
import re
import sys
import copy

# Input: String.
# Output: List of strings, empty if a syntax error has occurred.

def tokenize(program):
		#tokenList = re.findall(r'[[\(]|[\)]|\'(?:[\s*\(*\)*\,*\.*\?*(\\\')*\s*\s*]*)\'|[^\'\s\(\)]+]*', program)
	    #tokenList = re.findall(r'[[a-zA-Z][a-zA-Z0-9]*[\w*|^a-zA-Z0-9\w]+]*', program) #FIX THE \W to be symbols!!
	    #regexp expects the first character to be a letter, followed by any series of alphanumeric characters, which is then followed by
	    #1) one or more of: Any number of whitespace characters OR non-alphanumeric character followed by a whitespace character
	    #2) zero or more of: any number of whitespace characters OR one letter followed by zero or more alpha-numeric characters
	    #3) A single period or a comma
        #4) A color field in RGB form (1 or more digits followed by a comma with one or more digits followed by another comma and one or more digits)
        #5) A color field in HEX form ([0-9] or [A-F],[0-9] or [A-F],[0-9] or [A-F],[0-9] or [A-F],[0-9] or [A-F],[0-9] or [A-F])
		#tokenList = re.findall(r'[[a-zA-Z][a-zA-Z0-9\_]*[\w*|^a-zA-Z0-9\w]+|[\w*|[[a-zA-Z][a-zA-Z0-9\_]*]*|[\.\,]|\([0-9]+\,[0-9]+\,[0-9]+\)|\([[0-9]|[A-F]][[0-9]|[A-F]][[0-9]|[A-F]][[0-9]|[A-F]][[0-9]|[A-F]][[0-9]|[A-F]]\)]*', program)
#    pattern = re.compile(r'''
#    (
#    [a-zA-Z]*   #one
#    [0-9][0-9]  #two
#
#    )
#    ;
#    ''', re.VERBOSE)
    # #
    pattern = r'''

        [a-zA-Z][a-zA-Z0-9\_]*          #A token that begins with a letter and
                                        #is then followed by any number of
                                        #alphanumeric characters or an underscore

        |
        \d+\.{0,1}\d+                   #A floating point number
        |
        \d+                             #An integer
        |
        \.                              #A single period

        |
        [\=\+\-\/\*]
        
        |
        \,                              #A single comma
        |
        \"[a-zA-Z\s]+\"                   #A string in double quotes

        |
        \'[a-zA-Z\s]+\'                   #A string in single quotes

        |

        \(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\) #an RGB triple
        |

        \#[A-Fa-f0-9]{6}             #A HEX color grouping


    '''


    tokenList = re.findall(pattern, program,re.VERBOSE)



    return tokenList


def makeTokens(tokenList):
    newTokenList = []
    for i in range(len(tokenList)):
        t = Token()
        t.setToken(tokenList[i])
        #set the type using a helper function
        setTokenType(t)

        newTokenList.append(t)
    return newTokenList


def setTokenType(token):
#    print 'hi'
#    print re.match(r'[A-Z][a-zA-Z]*', token.getToken())
    
    if re.match(r'[a-zA-Z][a-zA-Z0-9\_]*',token.getToken()):
        if re.match(r'[A-Z][a-zA-Z0-9\_]*',token.getToken()):
            token.setType("type")
        elif re.match:
            token.setType("var")
    elif re.match(r'\d+\.{0,1}\d+',token.getToken()):
        token.setType("numeral")
        print("#A floating point number")
    elif re.match(r'\d+', token.getToken()):
        token.setType("numeral")
        print("#An integer")
    elif re.match(r'\.',token.getToken()):
        token.setType("period")
        print("#A single period")
    elif re.match(r'[\=\+\-\/\*]', token.getToken()):
        token.setType("symbol")
        print("symbol")
    elif re.match(r'\,', token.getToken()):
        token.setType("comma")
        print("#A single comma")
    elif re.match(r'\"[a-zA-Z\s]+\"', token.getToken()):
        token.setType("string")
        print("#A string in double quotes")
    elif re.match(r'\'[a-zA-Z\s]+\'',token.getToken()):
        token.setType("string")
        print("#A string in single quotes")
    elif re.match(r'\(\d{1,3}\,\s*\d{1,3}\,\s*\d{1,3}\)',token.getToken()):
        token.setType("rgbcolor")
        print("#an RGB triple")
    elif re.match(r'\#[A-Fa-f0-9]{6}', token.getToken()):
        token.setType("hex")
        print("#A HEX color grouping")
    else:
        print("Keine Ahnung Mofo")
    
    #actions
    #keywords
    #string
    #number
    #color field

def printTokens(tokenList):
    for i in range(len(tokenList)):
        tokenList[i].printTokenInfo()
