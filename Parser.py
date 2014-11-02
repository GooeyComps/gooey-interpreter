#import Stack

import re
import sys
import copy

# Class to create a stack and pull everything given in an
# expression into a stack
class Stack(object):

	def __init__(self):
		self.stack = []

	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def isEmpty(self):
		if self.stack == []:
			return True
		else:
			return False

# Scans a program into the corresponding list of tokens.
# Each token is "(", ")", or a sequence of non-white,
# non-parenthesis characters.
# Input: String.
# Output: List of strings, empty if a syntax error has occurred.
def tokenList(program):
        
		#tokenList = re.findall(r'[[\(]|[\)]|\'(?:[\s*\(*\)*\,*\.*\?*(\\\')*\w*\s*]*)\'|[^\'\s\(\)]+]*', program)
	    #tokenList = re.findall(r'[[a-zA-Z][a-zA-Z0-9]*[\w*|^a-zA-Z0-9\w]+]*', program) #FIX THE \W to be symbols!!
	    #regexp expects the first character to be a letter, followed by any series of alphanumeric characters, which is then followed by
	    #1) one or more of: Any number of whitespace characters OR non-alphanumeric character followed by a whitespace character
	    #2) zero or more of: any number of whitespace characters OR one letter followed by zero or more alpha-numeric characters
	    #3) A single period or a comma
		tokenList = re.findall(r'[[a-zA-Z][a-zA-Z0-9\_]*[[\w*|^a-zA-Z0-9\w]+|[\w*|[[a-zA-Z][a-zA-Z0-9\_]*]*|[\.\,]]*', program) #can we set these clauses to variables?

	
		#tokenList = re.findall(r'[[\(]|[\)]|\'(?:[\s*\(*\)*\,*\.*\?*(\\\')*\w*\s*]*)\'|[^\'\s\(\)]+]*', program)
		#for i in range(len(tokenList)):
			#tokenList[i] = re.sub(r'(?:\\\')', '\'',  tokenList[i])
		'''
		words = re.findall(r'(?ms)\W*(\w+)', program)
		tokenList = []
		for item in words:
			if item == 'set':
				token = {'item':item, 'type':'set'}
				tokenList.append(token)
			if item == 'make':
				token = {'item':item, 'type':'make'}
				tokenList.append(token)
			else:
				token = {'item':item, 'type':'undef'}
				tokenList.append(token)
		'''
		return tokenList

# Puts everything in the tokenList into a Stack
def createStack(stack, tokenList):
	for entry in tokenList:
		stack.push(entry)
	return stack

def printStack(stack):
	s = Stack()
	while not stack.isEmpty():
		s.push(stack.pop())
	while not s.isEmpty():
		print "the current stack item is: " , s.pop()


def main():



# For testing what is in the stack in a live environment
	environment = {"set":"set", "fun":"fun", "+":"+", "*":"*"}
	print "Welcome to Gooey. Press Control-D to exit."
	while True:
		try:
			program = raw_input(":> ")
			tokens = tokenList(program)
			stack = Stack()
			parser = createStack(stack, tokens)
			printStack(stack)
			# print 5
			# while not stack.isEmpty():
			# 	print "the current stack item is: " , stack.pop()
		except EOFError:
			print
			sys.exit()



# If the user ran (rather than imported) this file, then run main.
if __name__ == "__main__":
	main()
