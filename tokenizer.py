#from stack import *
from token import *
import re
import sys
import copy

# Input: String.
# Output: List of strings, empty if a syntax error has occurred.
def tokenize(program):
        
		#tokenList = re.findall(r'[[\(]|[\)]|\'(?:[\s*\(*\)*\,*\.*\?*(\\\')*\w*\s*]*)\'|[^\'\s\(\)]+]*', program)
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
    pattern = r'''
        [
        [a-zA-Z][a-zA-Z0-9\_]*      #a lowercase letter followed by alphanumeric characters
        [\w*|^a-zA-Z0-9\w]+         #followed by one or more of: any # of whitespace characters OR
                                    #a non-alphanumeric character followed by a whitespace character
        |                           #OR
        [\w*|[[a-zA-Z][a-zA-Z0-9\_]*]*
        ]

    '''
    #patternre = re.compile(pattern, re.VERBOSE)
    tokenList = re.findall(pattern, program,re.VERBOSE)
   # tokenList = re.findall(pattern, program)
   #     #can we set these clauses to variables?
       
        #Not sure if I need the hex clause
#	return tokenList
    return tokenList


def makeTokens(tokenList):
    newTokenList = []
    for i in range(len(tokenList)):
        t = Token()
        t.setToken(tokenList[i])
        #set the type using a helper function
        newTokenList.append(t)
    return newTokenList


def setTokenTypes(tokenList):
    #types
    #actions
    #keywords
    #string
    #number
    #color field
    pass

def printTokens(tokenList):
    for i in range(len(tokenList)):
        tokenList[i].printTokenInfo()
    
    
        
        
