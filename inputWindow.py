import tkinter as tk
from make import *
from interpreter import *
from settype import *
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter.scrolledtext import *

'''
This file creates a text editor that echoes the file content into a separate tkinter window using that 
window's "pack" method. So we are able to get new content into the window via packing without reloading the 
entire window. 

This is done with a "Run" option in the original text editor window

So now we need to process that input with interpreter and pass the AST into the GUIWindow Class via an update function 
that can parse the tree and add any new elements or modify old ones

'''
class Interpreter():
	def __init__(self, target):
		self.window = target
	
	def interpret(self, ast, window):
		for expr in ast:
			if hasattr(expr, "type"):
				if (expr.type == "Window"):
					for item in expr.attributes:
						if hasattr(item, 'color'):
							self.window.configure(bg=item.color.value)
						elif hasattr(item,'size'):
							size = item.size.value+"x"+item.size.value
							self.window.geometry(size)
				else:
					print("unsupported Make type")
			else:
				print("else")
				for item in expr.attributes:
					if hasattr(item, 'color'):
						self.window.configure(bg=item.color.value)
					elif hasattr(item,'size'):
						size = item.size.value+"x"+item.size.value
						self.window.geometry(size)
	



class GUIWindow():
	def __init__(self, window):
		self.window = window
	
	def open(self):
		self.window.mainloop()
		
	def stop(self):
		self.window.destroy()
		
	def modify(self, text):
		ast = parse(text, Program)
		i = Interpreter(self.window)
		i.interpret(ast, self.window)
		del i

class TextPad():
	def __init__(self):
		#text editor window
		self.root = tk.Tk(className="Gooey Editor")
		
		#refers to the content of the text editor window
		self.text = ""
		
		#text editor widgets
		m = Menu(self.root)
		self.root.config(menu=m)
		fm = Menu(m)
		m.add_cascade(label="File",menu=fm)
		fm.add_command(label="Run",command=self.update_preview)
		fm.add_command(label="Stop",command=self.stop_preview)
		
		#add textPad to root and open window
		self.textPad = tkst.ScrolledText(self.root, width=60, height=30)
		self.textPad.pack()
		
		self.previewOpen = False
		
	def run(self):
		self.root.mainloop()
		
	def update_preview(self):
		
		if self.previewOpen:
			text = self.retrieve_input()
			self.preview.modify(self.text)
			
		else:
			self.open_preview()
		
	def open_preview(self):
		if not self.previewOpen:
			self.previewOpen = True
			#live preview window
			self.previewTkObj = tk.Tk(className="Live Preview")
			self.preview = GUIWindow(self.previewTkObj)
			#self.preview.open()
			self.update_preview()
			
			
		else:
			print("already open")
		
	def stop_preview(self):
		self.preview.stop()
		self.previewOpen = False
		
	def retrieve_input(self):
		self.text = self.textPad.get('1.0', tk.END)
		
textpad = TextPad()
textpad.run()