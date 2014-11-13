if __name__ == "__main__":
    from make import *
    from interpreter import *
    from settype import *
    from tkinter import * 

    class Program(List):
	    grammar = maybe_some([Make,GooeySet])
		
    print("Input a valid 'make' statement")
    while True:
        try: 
            gooey = input(":> ")
        
        #gooey = "make Window w with size 500, color green. make Button b with window w, color blue, size 20, text hello, action foo."
            
        #build the abstract syntax tree using pypeg2 and our make.py file
            syntaxTree = parse(gooey, Program)

            
        #feed the syntax tree to interpreter.py to which outputs the actual gui and/or python code
            top = interpret(syntaxTree)
            #top.mainloop()
        except EOFError:
            print 
            sys.exit()
