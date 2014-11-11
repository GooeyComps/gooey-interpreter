from pypeg2 import *
from tkinter import *
from logicFile import *


def interpret(tree):
	top = Tk()
	#default window settings
	top.geometry("200x200+100+50")
	
	for expr in tree:
		if (expr.type == "Window"):
			for item in expr.attributes:
				if hasattr(item, 'color'):
					top.configure(bg=item.color.value)
				elif hasattr(item,'size'):
					size = item.size.value+"x"+item.size.value
					top.geometry(size)
					
		elif (expr.type == "Button"):
			b = Button(top)
			for item in expr.attributes:
				if hasattr(item, 'color'):
					b.configure(bg=item.color.value)
				if hasattr(item, 'text'):
					b.configure(text=item.text.value)
				elif hasattr(item,'size'):
					b.configure(width=item.size.value)
					b.configure(height=item.size.value)
				elif hasattr(item, 'action'):
					b.configure(command=foo)
			b.pack()
	top.mainloop()
	
