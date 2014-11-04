if __name__ == "__main__":
	from ast import *
	print("Input a valid 'make' statement")
	program = input(":> ")
	#program = "make Button b with color red, size large."
	makeStmt = ast(program)
	print(makeStmt)
	print("Object Type: ", makeStmt.objType)
	print("Object name: ", makeStmt.varname)
	for item in makeStmt.attributes:
		print ("Common attribute type: ", item.attrType)
		print ("Common attribute value: ", item.attrValue)