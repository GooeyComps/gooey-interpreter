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
		tokenList = re.findall(r'[[\(]|[\)]|\'(?:[\s*\(*\)*\,*\.*\?*(\\\')*\w*\s*]*)\'|[^\'\s\(\)]+]*', program)
		for i in range(len(tokenList)):
			tokenList[i] = re.sub(r'(?:\\\')', '\'',  tokenList[i])
		return tokenList

# Puts everything in the tokenList into a Stack
def createStack(stack, tokenList):
	for entry in tokenList:
		stack.push(entry)
	return stack

def main():

	#Create a list of tokens to put in a stack and print them
#	p = "( + 1 2 )"
#	tokens = tokenList(p)
#	for entry in tokens:
#		print "tokenList entry: " , entry

#	#Create a stack of all items in the tokenList and print them
#	stack = Stack()
#	parser = createStack(stack, tokens)
#	while not stack.isEmpty():
#		print "stack item: " , stack.pop()


# For testing what is in the stack in a live environment
	environment = {"set":"set", "fun":"fun", "+":"+", "*":"*"}
	print "Welcome to So Super Language. Press Control-D to exit."
	while True:
		try:
			program = raw_input(":> ")
			tokens = tokenList(program)
			stack = Stack()
			parser = createStack(stack, tokens)
			while not stack.isEmpty():
				print "the current stack item is: " , stack.pop()
		except EOFError:
			print
			sys.exit()



# If the user ran (rather than imported) this file, then run main.
if __name__ == "__main__":
	main()jamaicalammi
