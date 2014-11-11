if __name__ == "__main__":
	from ast import *
	from interpreter import *
	#print("Input a valid 'make' statement")
	#program = input(":> ")
	program = "make Window w with size 100, color (120,120,120)"
	makeStmt = ast(program)
		
	#interpret(makeStmt)