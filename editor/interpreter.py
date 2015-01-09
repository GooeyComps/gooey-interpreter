from tkinter import *
from pypeg2 import *

class Interpreter():
	def __init__(self, target):
		self.window = target
		self.localBindings = dict()
		
	def error(self, message):
		errorPopup = Toplevel()
		errorPopup.title("Error")
		errorPopup.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
		msg = Message(errorPopup, text=message)
		msg.pack()

		button = Button(errorPopup, text="Ok", command=errorPopup.destroy)
		button.pack()
		#self.window.destroy()
		
	def interpret(self, ast, bindings):
		for expr in ast:
	
			if hasattr(expr, "type"):
				if hasattr(expr, "varname"):
					if expr.varname.thing in self.localBindings:
						message = expr.varname.thing, "already defined."
						self.error(message)
						break
					else:
						self.localBindings[expr.varname.thing] = expr
				if (expr.type == "Window"):
					if hasattr(expr, "attributes"):
						for item in expr.attributes:
							if hasattr(item, 'color'):
								self.window.configure(bg=item.color.value)
							elif hasattr(item,'size'):
								size = item.size.value+"x"+item.size.value
								self.window.geometry(size)
				elif (expr.type == "Button"):
					b = Button(self.window)
					for item in expr.attributes:
						if hasattr(item, 'color'):
							b.configure(bg=item.color.value)
						if hasattr(item, 'text'):
							b.configure(text=item.text.value)
						elif hasattr(item,'size'):
							b.configure(width=item.size.value)
							b.configure(height=item.size.value)
						elif hasattr(item, 'action'):
							print(item)
							#b.configure(command=item)
					b.pack()
			else:
				print("else")
				'''
				for item in expr.attributes:
					if hasattr(item, 'color'):
						self.window.configure(bg=item.color.value)
					elif hasattr(item,'size'):
						size = item.size.value+"x"+item.size.value
						self.window.geometry(size)
				'''
		return bindings