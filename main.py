from tokenizer import *
from parser import *
from token import *

def main():

# For testing what is in the stack in a live environment
	#environment = {"set":"set", "fun":"fun", "+":"+", "*":"*"}
	print "Welcome to Gooey. Press Control-D to exit."
	while True:
		try:
			program = raw_input(":> ")
			tokens = tokenize(program)
			#printTokens(makeTokens(tokens))
			#stack = Stack()
			#tokenStack = createStack(stack, tokens)
			#printStack(tokenStack)
			
			parse(tokens)
			
		except EOFError:
			print
			sys.exit()



# If the user ran (rather than imported) this file, then run main.
if __name__ == "__main__":
	main()