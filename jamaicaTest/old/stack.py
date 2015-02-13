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
		print ("the current stack item is: " , s.pop())