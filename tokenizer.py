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
		tokenList = re.findall(r'[[a-zA-Z][a-zA-Z0-9\_]*[[\w*|^a-zA-Z0-9\w]+|[\w*|[[a-zA-Z][a-zA-Z0-9\_]*]*|[\.\,]]*', program) #can we set these clauses to variables?
        
		return tokenList


def makeTokens(tokenList):
    newTokenList = []
    for i in range(len(tokenList)):
        t = Token()
        t.setToken(tokenList[i])
        #set the type using a helper function
        newTokenList.append(t)
    return newTokenList
    
def printTokens(tokenList):
    for i in range(len(tokenList)):
        tokenList[i].printTokenInfo()
    
    
        
        