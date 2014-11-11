from pypeg2 import *
from make import *
from tkinter import *
from actions import *


def interpret(tree):
	top = Tk()
	top.geometry("600x400+100+50")
	
	for item in tree.attributes:
		if(item.attrType == "color"):
			w = Button(top, bg=item.attrValue, text="Button", command=buttonLogic)
			w.pack()
		
	top.mainloop()
	
