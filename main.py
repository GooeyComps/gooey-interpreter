if __name__ == "__main__":
	from ast import *
	from interpreter import *
	#print("Input a valid 'make' statement")
	#program = input(":> ")
	program = "make"
	makeStmt = ast(program)
		
	#interpret(makeStmt)