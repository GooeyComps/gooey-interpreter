from tkinter import *
from pypeg2 import *
import actionbuttons
from statements import *
import sys
import matrix
import math

import os

### START EMILY CODE ###
class ErrorPopup:
	'''
	A pop-up window that gracefully handles Gooey errors.
	Displays the error message to the user and closes when "OK" button is clicked.
	'''
	def __init__(self, message):
		self.message = message
		# Create error popup window
		self.window = Toplevel()
		self.window.title("Error")
		self.window.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
		# Add message to popup
		messageText = Message(self.window, text=self.message)
		messageText.pack()
		# Add "OK" button to popup, that will close popup when clicked
		button = Button(self.window, text="Ok", command=self.window.destroy)
		button.pack()
### END EMILY CODE ###

#Binding object has four instance variables
#bType - the type of object with regards to "Gooey" ex) Window, Button
#varname - how we identify the object (a string)
#bObject - the actual tkinter object
#params - an optional argument use to take in the parameters of a user defined function
class Binding:
	bType = None
	varname = None
	bObject = None
	params = None

	def __init__(self,bType,varname,bObject,params):
		'''Sets instance variables: type, name, Tkinter object, and optional parameters'''
		self.bType = bType
		self.varname = varname
		self.bObject = bObject
		self.params = params

### START EMILY CHANGE ###
	def __repr__(self):
		'''Prints a pretty version of the bindings'''
		prettyStr = "Binding " + str(self.varname) + " of type " + str(self.bType) + "."
		return prettyStr
### END EMILY CHANGE ###

class Interpreter():
	'''Interpreter class: creates GUI based on the expression given by the user.'''
	gRows = 0
	gColumns = 0

	def __init__(self, target):
		'''Initializes the GUI window'''
		self.window = target
		self.var = IntVar()

### START EMILY CHANGE ###
	def error(self, message):
		'''Generates a popup error message'''
		ErrorPopup(message)
### END EMILY CHANGE ###

	def interpret(self, ast, bindings):
		'''Interprets the Gooey code and creates a GUI in the window.
		It takes in an abstract syntax tree as generated by pypeg, and the current bindings.
		Returns a new list of bindings. '''
		for expr in ast:



			#   MAKE
			if(expr.__class__.__name__ == "Make"):
				if hasattr(expr, "type"):
					if (expr.type == "Window"):
						self.checkVarname(expr,bindings)
						w = self.makeWindow(self.window,expr)
						binding = self.makeBinding("Window", expr.varname, w)
						bindings = self.addBinding(binding, bindings)

					elif(expr.type == "Button"):
						self.checkVarname(expr,bindings)
						b = self.makeButton(self.window,expr)
						binding = self.makeBinding("Button", expr.varname, b)
						bindings = self.addBinding(binding, bindings)

					elif(expr.type == "Menu"):
						self.checkVarname(expr,bindings)
						m = self.makeMenu(self.window,expr,bindings)
						options = self.getOptions(expr)
						binding = self.makeBinding("Menu", expr.varname, m, options)
						bindings = self.addBinding(binding,bindings)

					elif(expr.type == "MenuItem"):
						self.checkVarname(expr,bindings)
						mi = self.makeMenuItem(self.window,expr,bindings)
						options = self.getOptions(expr)
						binding = self.makeBinding("MenuItem", expr.varname, mi, options)
						bindings = self.addBinding(binding,bindings)

					elif(expr.type == "TextBox"):
						self.checkVarname(expr,bindings)
						t = self.makeTextBox(self.window, expr)
						binding = self.makeBinding("TextBox", expr.varname, t)
						bindings = self.addBinding(binding,bindings)

					elif(expr.type == "Image"):
						self.checkVarname(expr,bindings)
						i = self.makeImage(self.window, expr)
						binding = self.makeBinding("Image", expr.varname, i)
						bindings = self.addBinding(binding,bindings)

					elif(expr.type == "Text"):
						self.checkVarname(expr,bindings)
						t = self.makeText(self.window, expr)
						binding = self.makeBinding("Label", expr.varname, t)
						bindings = self.addBinding(binding,bindings)

					elif(expr.type == "Checkboxes"):
						self.checkVarname(expr,bindings)
						if hasattr(expr, "attributes"):
							for item in expr.attributes[0]:
								if hasattr(item, 'position'):
									if hasattr(item.position.value, "r"):
										cbRow = int(item.position.value.r)
										cbColumn = int(item.position.value.c)
									else:
										cbRow, cbColumn = self.getPositionByKeyword(item.position.value)

							for item in expr.attributes[0]:
								if(hasattr(item, 'options')):
									i = 0
									while(i < len(item.options.options)):
										cb = self.makeCheckboxes(self.window,expr,item.options.options[i], i, cbRow, cbColumn)
										binding = self.makeBinding("Checkboxes", expr.varname, cb)
										bindings = self.addBinding(binding, bindings)
										i += 1
								elif(hasattr(item, 'title')):
									cbTitle = item.title.title.strip("[]'")
									ttl = Label(self.window, text=cbTitle)
									ttl.grid(row=cbRow, column=cbColumn, sticky=N+S+E+W)
									binding = self.makeBinding("Checkboxes", expr.varname, ttl)
									bindings = self.addBinding(binding, bindings)
								elif(hasattr(item, 'position')):
									pass
								else:
									self.error("Error: Incorrect attribute.")
						else:
							# Use default values
							pass

					elif(expr.type == "RadioButtons"):
						self.checkVarname(expr,bindings)
						if hasattr(expr, "attributes"):
							for item in expr.attributes[0]:
								if hasattr(item, 'position'):
									if hasattr(item.position.value, "r"):
										rbRow = int(item.position.value.r)
										rbColumn = int(item.position.value.c)
									else:
										rbRow, rbColumn = self.getPositionByKeyword(item.position.value)

							for item in expr.attributes[0]:
								if(hasattr(item, 'options')):
									i = 0
									while(i < len(item.options.options)):
										rb = self.makeRadioButtons(self.window,expr,item.options.options[i], i, rbRow, rbColumn)
										binding = self.makeBinding("RadioButtons", expr.varname, rb)
										bindings = self.addBinding(binding, bindings)
										i += 1
								elif(hasattr(item, 'title')):
									rbTitle = self.extractTextValue(item.title.title)
									ttl = Label(self.window, text=rbTitle)
									ttl.grid(row=rbRow, column=rbColumn, sticky=N+S+E+W)
									binding = self.makeBinding("RadioButtons", expr.varname, ttl)
									bindings = self.addBinding(binding, bindings)
								elif(hasattr(item, 'position')):
									pass
								else:
									self.error("Error: Incorrect attribute.")
						else:
							# Use default values
							pass

					else:
						self.error("Error: Object not recognized. Make sure to capitalize the object name.")

				else:
					self.error("Error: No type recognized.")



			#   SET
			elif(expr.__class__.__name__ == "GooeySet"):
				print("GOOEY Set")
				if hasattr(expr, "varname"):
					print("Has Varname: ", expr.varname)
					print("BINDINGS: ", bindings)
					if expr.varname in bindings:
						print("expr.varname is in bindings")
						obj = bindings[expr.varname]
						if obj.bType == "Window":
							win = self.getObject(expr,bindings)
							print("Type Before: ", win.bType)
							assert win.bType == 'Window'
							print("Type After: ", win.bType)
							wColorBefore = win.bObject.cget('bg')
							w = self.setWindow(win.bObject,expr)
							wColorAfter = w.cget('bg')
							if wColorBefore != wColorAfter:
								bindings = self.fixButtonPadding(wColorAfter,bindings)
							w = self.setWindow(win.bObject,expr)

						elif(obj.bType == "Button"):
							button = self.getObject(expr,bindings)
							assert button.bType == 'Button'
							b = self.setButton(button.bObject,self.window, expr)

						elif(obj.bType == "Menu"):
							pass

						elif(obj.bType == "MenuItem"):
							pass

						elif(obj.bType == "TextBox"):
							t = self.getObject(expr,bindings)
							assert t.bType == 'TextBox'
							tbox = t.bObject
							if hasattr(expr, "attributes"):
								for item in expr.attributes[0]:
									if hasattr(item, 'text'):
										tbox.insert(END, item.text.value)
										tbox.pack()
						#print("THIS IS EXPR: ",expr.attributes.text)
						#tbox.insert(END, expr)
				else:
					self.error("Error: Undefined variable used.")


			#               FUNCTIONS
			#Interprets all function definition statements
			elif(expr.__class__.__name__ == "FunctionDefinition"):
				if hasattr(expr, "funcname"):
					#Checks bindings to see if function name is already there
					for i in range(len(expr.funcaction)):
						b = self.interpret([expr.funcaction[i]], bindings) #this putting i in a list is stupid and Leah fully admits it
						# b = self.interpret(expr.funcaction[i], bindings) #this putting i in a list is stupid and Leah fully admits it

						expr.funcaction[i] = b

					if expr.funcname in bindings:
						self.error("Sorry, this function name is already used.")

					#If function isn't already defined, add it to bindings
					else:
						if hasattr(expr, "params"):
							binding = self.makeBinding("Function", str(expr.funcname), expr.funcaction, expr.params)
						else:
							binding = self.makeBinding("Function", str(expr.funcname), expr.funcaction)
						bindings = self.addBinding(binding,bindings)
				else:
					self.error("Sorry, you need to give your function a name")

			#Interprets all function calls
			elif(expr.__class__.__name__ == "FunctionCall"):
				#Find function with that name
				function = expr.funcname
				if function in bindings:
					#Look at params in the bindings
					#if hasattr(expr, "params"):
					localBindings = dict()
					if len(expr.params)>0:
						#Make set of local bindings

						#Bind objects passed into parameter with parameter in function

						#Take param being passed in (params), bind to expected param in function
						#add this to local binding
						print("BINDINGS THING: ", bindings[function].params)
						functionParam = bindings[function].params
						#functionInput = bindings[functionParam[0]]

						#Assuming only one parameter
						functionInput = bindings[expr.params[0]]

						#Sets the type of the local to the thing that we're passing in.
						print("FunctionParam: ", functionParam)
						b = self.makeBinding(functionInput.bType, functionParam, functionInput.bObject)
						localBindings = self.addBinding(b, localBindings)
						print("local bindings: ", localBindings)
						newBindings = self.runFunction(bindings,function,localBindings)
						newB = newBindings[functionParam]
						newB.varname = functionInput.varname

						#Binds the returned object to the thing that it modified
						bindings[functionInput.varname] = newB
					else:
						newBindings = self.runFunction(bindings,function,localBindings)
						for key in newBindings.keys():
							bindings[key] = newBindings[key]
						print("NEW BINDINGS: ", newBindings)
				else:
					self.error("This function isn't defined.")


			#Interprets each line of a function.
			elif(expr.__class__.__name__ == "Line"):
				print("got into Line")
				return expr.lineAction
			elif(expr.__class__.__name__ == "Return"):
				print("got into Return")
				return expr.param

			else:
				#Invalid first word
				self.error("Error: Invalid command. Please start your command with Make, Set, or other valid start commands.")
		print("THESE ARE THE BINDINGS: ", bindings)
		return bindings

    #               CHECKBOXES


	def makeDefaultCheckboxes(self,w,defaults):
		pass


	def makeCheckboxes(self,w,expr,i,num, r, c):
		r = r + num + 1
		i = self.extractTextValue(i)
		op = Checkbutton(w, text=i, variable=str(num), anchor=W)
		op.grid(row=r, column=c, sticky=N+S+E+W)
		return op

#
#    #               RADIOBUTTONS
#
#
	def makeDefaultRadioButtons(self,w,defaults):
		pass

	def makeRadioButtons(self,w,expr,i,num, r, c):
		r = r + num + 1
		i = self.extractTextValue(i)
		gg = Radiobutton(w, text=i, variable=self.var, value=num, anchor=W)
		gg.grid(row=r, column=c, sticky=N+S+E+W)
		return gg


#    #               TEXT
	def makeDefaultText(self,w,defaults):
		tl = Label(w, text = defaults['text'], bg = defaults['color'])
		#needs position and size
		return tl

	def makeText(self,w,expr):
		defaults = self.getAllDefaults("Text")
		tl = self.makeDefaultText(w,defaults)
		#tl = Label(w, text="Text")
		r, c = 0, 0
		if hasattr(expr, "attributes"):
			for item in expr.attributes:
				if hasattr(item, 'text'):
					tl.configure(text=self.extractTextValue(item.text.value))
				elif hasattr(item, 'position'):
					if hasattr(item.position.value, "r"):
						r = int(item.position.value.r)
						c = int(item.position.value.c)
					else:
						r, c = self.getPositionByKeyword(item.position.value)
				elif hasattr(item, 'color'):
					tl.configure(fg=item.color.value)
				else:
					self.error("Error: Incorrect attribute.")
		tl.grid(row=r, column=c, sticky=N+S+E+W)
		return tl


	#               WINDOWS


	def makeDefaultWindow(self,w,defaults):
		'''Makes a window with default attributes'''
		#Configure the window with defaults
		w.deiconify()
		####NEED TO ADD FONT AND FONTSIZE####
		####NEED TO DO textcolor as fg = defaults[textcolor]####
		####NEED TO ADD WINDOW SIZE -- Right now it is just medium size
		w.geometry('400x400')
		w.title(defaults['title'])
		w.configure(bg=defaults['color'])
		return w

	def makeWindow(self,w,expr):
		'''Makes a window given user attributes.
		It should set anything that the user has not specified to the defaults.'''
		#Construct the default window
		defaults = self.getAllDefaults("Window")
		w = self.makeDefaultWindow(w,defaults)
		#If the user input any attributes, change the default window to reflect that
		if hasattr(expr, "attributes"):
			windowAttributeList = expr.attributes
			for item in windowAttributeList:
				print(item)

				if hasattr(item, 'color'):
					w.configure(bg=item.color.value)
				elif hasattr(item,'size'):
					if hasattr(item.size.value, "columns"):
						rows = int(item.size.value.rows)
						columns = int(item.size.value.columns)
						Interpreter.gRows = rows
						Interpreter.gColumns = columns
						#fill cells with empty space somehow, so the user gets a sense of it actually being a grid
						for i in range(0,columns):
							for j in range(0,rows):
								l = Frame(w, height=100, width=100)
								l.grid(row = j, column = i)

					elif item.size.value[0].isdigit():
						size = item.size.value+"x"+item.size.value
						w.geometry(size)
					else:
						print("ITEM.SIZE.LOWER = ", item.size.value.lower())
						if item.size.value.lower() == "large":
							w.geometry('600x600')
						elif item.size.value.lower() == "medium":
							print("got to medium")
							w.geometry('400x400')
						elif item.size.value.lower() == "small":
							w.geometry('200x200')
				elif hasattr(item, 'title'):
					w.title(item.title.value)
				elif hasattr(item, 'font'):
					pass
				elif hasattr(item, 'fontSize'):
					pass
				elif hasattr(item, 'textColor'):
					pass
		#somewhere in here we need to look and error check that there are only
		#attributes that are supposed to be here
		return w




	def setWindow(self,w,expr):
		'''Sets window attributes to those specified by the user.'''
		print("GOT TO SETWINDOW")
		if hasattr(expr, "attributes"):
			for item in expr.attributes:
				if hasattr(item, 'color'):
					#self.window.configure(bg=item.color.value)
					w.configure(bg=item.color.value)
				elif hasattr(item,'size'):
					if hasattr(item.size.value, "columns"):
						rows = int(item.size.value.rows)
						columns = int(item.size.value.columns)
						for i in range(0,columns):
							for j in range(0,rows):
								l = Frame(w, height=100, width=100)
								l.rowconfigure('all', minsize = 100)
								l.columnconfigure('all', minsize = 100)
								l.grid(row = j, column = i)

					elif item.size.value[0].isdigit():
						size = item.size.value+"x"+item.size.value
						w.geometry(size)
					else:
						if item.size.value.lower() == "large":
							w.geometry('600x600')
						elif item.size.value.lower() == "medium":
							w.geometry('400x400')
						elif item.size.value.lower() == "small":
							w.geometry('200x200')
				elif hasattr(item, 'title'):
					w.title(item.title.value)
				elif hasattr(item, 'font'):
					pass
				elif hasattr(item, 'fontSize'):
					pass
				elif hasattr(item, 'textColor'):
					pass
		return w




	#               TEXT BOX

	def makeDefaultTextBox(self,w,defaults):
		###STILL NEEDS MORE ###
		'''Makes a TextBox with default attributes'''
		t = Text(w)
		t.insert(END,defaults['text'])
		#need
		#title
		#Position
		#size
		#hidden
		return t

	def makeTextBox(self,w,expr):
		'''Makes a text box with the user defined attributes.'''
		#t = Text(w, height=2, width=30)
		defaults = self.getAllDefaults("TextBox")
		t = self.makeDefaultTextBox(w,defaults)
		r, c = 0, 0
		if hasattr(expr, "attributes"):
			for item in expr.attributes[0]:
				if hasattr(item, 'text'):
					t.insert(END, self.extractTextValue(item.text.value))
				elif hasattr(item, 'position'):
					if hasattr(item.position.value, "r"):
						r = int(item.position.value.r)
						c = int(item.position.value.c)
					else:
						r, c = self.getPositionByKeyword(item.position.value)
				else:
					self.error("Error: Incorrect attribute.")
		t.grid(row=r, column=c, sticky=N+S+E+W)
		return t



	#               BUTTONS

	def makeDefaultButton(self, w, defaults):
		'''Makes a button with default attributes'''
		#This is the current background color of the window
		#We need this to correct for padding issues on the mac
		hB = w.cget('bg')
		b = Button(w, highlightbackground = hB)
		#Need to add in position, size, color?
		b.configure(text=defaults['text'])
		return b


	def makeButton(self,w,expr):
		'''Makes a button by taking in the window the button should be made in
		and the expression given by the user.'''
		defaults = self.getAllDefaults('Button')
		b = self.makeDefaultButton(w,defaults)
		r, c = 0, 0
		print("GOT TO MAKE BUTTON: ", r, c)
		if hasattr(expr, "attributes"):
			buttonAttributeList = expr.attributes
			for item in buttonAttributeList:
				if hasattr(item, 'color'):
					b.configure(bg=item.color.value)
				if hasattr(item, 'text'):
					b.configure(text=self.extractTextValue(item.text.value))
				elif hasattr(item,'size'):
					b.configure(width=item.size.value)
					b.configure(height=item.size.value)
				elif hasattr(item,'position'):
					if hasattr(item.position.value, "r"):
						r = int(item.position.value.r)
						c = int(item.position.value.c)
					else:
						r, c = self.getPositionByKeyword(item.position.value)

				# These are the action statements
				elif hasattr(item, 'action'):
					#Cast action to string, otherwise you cannot find right action
					#This is temporary until I can call the action as a direct line in the command
					action = str(item.action.value)
					print("THIS IS THE ACTION: ", action)
					# print("AKLSJDHFKLAJHFH")
					# print(item.action.value)
					# if action == 'write':
					#     b.configure(command=lambda: actionbuttons.Actions.write(item.action.text))
					# elif action == 'close':
					#     b.configure(command=lambda: actionbuttons.Actions.close(w))
					# elif action == 'colorChange':
					#     b.configure(command=lambda: actionbuttons.Actions.windowColorChange(w, item.action.color))
					#     print("interpreter")
					#a = actionbuttons.Actions.callAction(w,item)
					a = actionbuttons.findAction(item)
					#w = a[0]
					#item = a[1]
					b.configure(command=lambda: actionbuttons.callAction(w,item,action))
					# else:
					#     print("You have entered a command that is not defined")

		b.grid(row=r, column=c, sticky=N+S+E+W)
		return b


	def setButton(self,b,w,expr):
		'''Sets button based on user attributes.'''
		buttonAttributeList = expr.attributes
		for item in buttonAttributeList:
			if hasattr(item, 'color'):
				b.configure(bg=item.color.value)
			if hasattr(item, 'text'):
				b.configure(text=self.extractTextValue(item.text.value))
			elif hasattr(item,'size'):
				b.configure(width=item.size.value)
				b.configure(height=item.size.value)
			elif hasattr(item,'position'):
				if hasattr(item.position.value, "r"):
					r = int(item.position.value.r)
					c = int(item.position.value.c)
				else:
					r, c = self.getPositionByKeyword(item.position.value)
				b.grid(row=r, column=c, sticky=N+S+E+W)
			elif hasattr(item, 'action'):
				# print(item)
				action = str(item.action.value)
				# print("AKLSJDHFKLAJHFH")
				# print(item.action.value)
				# if action == 'write':
				#     b.configure(command=lambda: actionbuttons.Actions.write(item.action.text))
				# elif action == 'close':
				#     b.configure(command=lambda: actionbuttons.Actions.close(w))
				# elif action == 'colorChange':
				#     b.configure(command=lambda: actionbuttons.Actions.windowColorChange(w, item.action.color))
				#     print("interpreter")
				#a = actionbuttons.Actions.callAction(w,item)
				a = actionbuttons.findAction(item)
				#w = a[0]
				#item = a[1]
				b.configure(command=lambda: actionbuttons.callAction(w,item,action))
		return b

	def fixButtonPadding(self,color,bindings):
		'''Fixes the padding around the buttons'''
		for i in bindings.keys():
			if bindings[i].bType == "Button":
				bindings[i].bObject.configure(highlightbackground = color)
		return bindings








#	#               MENUS
#    def makeDefaultMenu(self,w,defaults):
#        pass
	def makeMenu(self,w,expr,bindings):
		rootMenu = None
		children = w.winfo_children()
		for c in children:
			if type(c).__name__ == "Menu":
				rootMenu = c
		w.config(menu=rootMenu)
		return rootMenu

#	def makeDefaultMenuItem(self,w,defaults):
#		pass

	def makeMenuItem(self,w,expr,bindings):
		menuItem = None
		rootMenu = None
		children = w.winfo_children()
		for c in children:
			if type(c).__name__ == "Menu":
				rootMenu = c

		#check if menu item has already been defined as a child of some other menu or menuitem
		for key in bindings:
			if bindings[key].bType == "Menu":
				if expr.varname in bindings[key].params:
					#binding found, add to submenu to rootMenu
					subMenu = Menu(bindings[key].bObject, tearoff=0)
					#get the text attribute
					subMenuText = "Undefined"
					for item in expr.attributes:
						if hasattr(item,'text'):
							subMenuText = item.text.value
					bindings[key].bObject.add_cascade(label=subMenuText,menu=subMenu)

					for item in expr.attributes:
						if hasattr(item, 'options'):
							for v in item.options.value:
								print(v)
								'''
								action = str(v)
								a = actionbuttons.findAction(v)
								subMenu.add_command(label=v.text,command=lambda: actionbuttons.callAction(w,v,action))
								'''


					menuItem = subMenu
					w.config(menu=bindings[key].bObject)

		return menuItem


	#           IMAGES - not in window right now!
	def makeDefaultImage(self,w,defaults):
		pass
	def makeImage(self, w, expr):
		'''Makes a images with the user defined attributes.'''
		defaults = self.getAllDefaults("Image")
		#(i,l) = self.makeDefaultImage(w,defaults)
		r, c = 0, 0
		if hasattr(expr, "attributes"):
			for item in expr.attributes:
				if hasattr(item, 'source'):


					######## Images only work when you read in from text file, otherwise source path is different

					#directory = os.getcwd()
					#print("OS : ", os.getcwd())
					#directory = str(sys.path[0])
					#directory = directory.append('/apple.gif')
					#print("CURRENT WORKING DIR IS: ", directory+'/apple.gif')
					#print("DIRECTORY IS: ", sys.path.append(os.path.dirname(os.path.abspath(__file__)))
					#i = PhotoImage(file=open(directory+'/apple.gif'))


					i = PhotoImage(file=item.source.value)
					l = Label(image=i)
					l.image = i
				elif hasattr(item, 'position'):
					if hasattr(item.position.value, "r"):
						r = int(item.position.value.r)
						c = int(item.position.value.c)
					else:
						r, c = self.getPositionByKeyword(item.position.value)
				else:
					self.error("Error: Incorrect attribute.")
		l.grid(row=r, column=c, sticky=N+S+E+W)
		return l




	#               HELPER METHODS
	def makeBinding(self,t,v,o,p=[]):
		'''Makes a binding for the object.'''
		binding = Binding(t,v,o,p)
		return binding

	def addBinding(self,b,bindings):
		'''Takes a binding and adds to the dictionary of bindings.'''
		bindings[b.varname] = b
		return bindings

	'''#Make the binding associated with this function
	#The object will be the parameters passed in and the function action (in a tuple)
	def makeFunction(self,w, expr):
		pass'''

	#this should maybe take in parameters
	#expects "run" then a user defined function name
	#replaces , separating gooey instructions and adds period at end
	#Makes a temporary binding relating to parameters and then gets rid of that parameter
	def runFunction(self,bindings,function,localBindings):
		#Run function should create local bindings maybe?????????????????
		#print("\n\n I'm running runFunction!")
		print("got to runFunction")
		functionCode = bindings[function].bObject #We need to make this proper gooey code
		print("This is the functionCode: ", functionCode)
		newBindings = localBindings
		#print("New Bindings: ", newBindings)
		for i in range(len(functionCode)-1):
		#for action in functionCode:
			print("Here's the action", functionCode[i])
			newBindings = self.interpret([functionCode[i]], newBindings)
			# newBindings = self.interpret(action, newBindings)

			#print("New Bindings: ", newBindings)
		return newBindings
		# funStr = ''
		# for i in functionCode:
		#     funStr = funStr + " " + i
		# funStr = funStr[1:] + "."
		# #parse the function code and pass the parsed code as the ast
		# localAst = parse(funStr,Program)
		# newBindings = self.interpret(localAst,localBindings)
		# return newBindings


	def getOptions(self,expr):
		'''Get list of options, ie: make MenuItem with options [red green blue]. '''
		for item in expr.attributes:
			if hasattr(item, 'options'):
				print(item.options.value)
				return item.options.value
			else:
				return None


	def getAllDefaults(self, typeName):
		'''Given a Gooey type name, like "Window" or "Button", consult our matrix
		and return the predetermined default attributes for that type'''
		defaults = {}
		for i in range(0,matrix.NUM_ATTRIBUTES):
			defaultAttr = matrix.getDefault(typeName, i)
			defaults[matrix.AttrName(i).name] = defaultAttr
			#Need to figure out how to return these
		return defaults

	def checkVarname(self,exp,bindings):
		if hasattr(exp, "varname"):
			#if expr.varname in bindings:
			if exp.varname in bindings:
				message = exp.varname, "already defined."
				self.error(message)


	def getObject(self,exp,bindings):
		if exp.varname in bindings:
			return bindings[exp.varname]
		else:
			message = exp.varname, "undefined."
			self.error(message)


	def getPositionByKeyword(self, keyword):
		if keyword == "center":
			r = math.floor(float(Interpreter.gRows)/2)
			c = math.floor(float(Interpreter.gColumns)/2)
		elif keyword == "top":
			r = 0
			c = math.floor(float(Interpreter.gColumns)/2)
		elif keyword == "bottom":
			r = Interpreter.gRows
			c = math.floor(float(Interpreter.gColumns)/2)
		elif keyword == "left":
			r = math.floor(float(Interpreter.gRows)/2)
			c = 0
		elif keyword == "right":
			r = math.floor(float(Interpreter.gRows)/2)
			c = Interpreter.gColumns
		elif keyword == "topleft":
			r = 0
			c = 0
		elif keyword == "topright":
			r = 0
			c = Interpreter.gColumns
		elif keyword == "bottomleft":
			r = Interpreter.gRows
			c = 0
		elif keyword == "bottomright":
			r = Interpreter.gRows
			c = Interpreter.gColumns
		return r, c

	def extractTextValue(self, value):
		words = re.findall(r'[\w\d\.]+', value)
		return ' '.join(words)
