import tkinter as tk
from interpreter import *
from tkinter import *
from grammar import *
from tkinter import Menu
import tkinter.scrolledtext as tkst
from tkinter.scrolledtext import *
from pypeg2 import *

'''
This file creates a text editor that echoes the file content into a separate tkinter window using that 
window's "pack" method. So we are able to get new content into the window via packing without reloading the 
entire window. 

This is done with a "Run" option in the original text editor window
'''

class GUIWindow():
	def __init__(self, window):
		self.window = window
		self.bindings = dict()
		#self.is_open = False
		
	def open(self):
		self.is_open = True
		#self.window.mainloop()
		
	def stop(self):
		self.is_open = False
		self.window.destroy()
		
	def modify(self, ast):	
		#create new instance of interpeter class, passing a reference the live preview window
		i = Interpreter(self.window)
		
		self.bindings = i.interpret(ast, self.bindings)
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
		
		
	def run(self):
		self.root.mainloop()
		
	def update_preview(self):
		if hasattr(self,"preview"):
			if self.preview.is_open:
				try:
					self.retrieve_input()
					ast = parse(self.text, Program)
					
					self.preview.modify(ast)
					
				except SyntaxError as e:
					
					popup = Toplevel()
					popup.title("Error")
					popup.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
					error = "Syntax Error:", e
					msg = Message(popup, text=error)
					msg.pack()

					button = Button(popup, text="Ok", command=popup.destroy)
					button.pack()
					#self.stop_preview()
		
			else:
				self.open_preview()
		else:
			self.open_preview()
		
	def open_preview(self):
		if hasattr(self,"preview"):
			if not self.preview.is_open:
				#live preview window
				self.previewTkObj = tk.Tk(className="Live Preview")
				self.previewTkObj.protocol("WM_DELETE_WINDOW", self.on_close)
				self.preview = GUIWindow(self.previewTkObj)
				self.preview.open()
				self.update_preview()
		else:
			#live preview window
			self.previewTkObj = tk.Tk(className="Live Preview")
			self.previewTkObj.protocol("WM_DELETE_WINDOW", self.on_close)
			self.preview = GUIWindow(self.previewTkObj)
			self.preview.open()
			self.update_preview()
		
	def stop_preview(self):
		if self.preview.is_open:
			self.preview.stop()
		else:
			print("preview window not open")
		
	def on_close(self):
		print("on close")
		self.preview.stop()
		
	def retrieve_input(self):
		self.text = self.textPad.get('1.0', tk.END)
		
textpad = TextPad()
textpad.run()