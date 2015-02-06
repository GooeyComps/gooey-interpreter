from tkinter import *
from pypeg2 import *
import actionbuttons
from statements import *
import sys

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
        self.bType = bType
        self.varname = varname
        self.bObject = bObject
        self.params = params



class Interpreter():
    def __init__(self, target):
        self.window = target

    def error(self, message):
        errorPopup = Toplevel()
        errorPopup.title("Error")
        errorPopup.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
        msg = Message(errorPopup, text=message)
        msg.pack()

        button = Button(errorPopup, text="Ok", command=errorPopup.destroy)
        button.pack()
        #self.window.destroy()
        sys.exit()

    def interpret(self, ast, bindings):
        print("Interpreting ast", ast)
        print("type of ast", type(ast))
        for expr in ast:
            print("This is an expr in the ast", expr)
            
            
            
            #   MAKE
            if(expr.__class__.__name__ == "MakeWindow"):
                self.checkVarname(expr,bindings)
                w = self.makeWindow(self.window,expr)
                binding = self.makeBinding("Window", expr.varname, w)
                bindings = self.addBinding(binding, bindings)
                
            elif(expr.__class__.__name__ == "MakeButton"):
                self.checkVarname(expr,bindings)
                b = self.makeButton(self.window,expr)
                binding = self.makeBinding("Button", expr.varname, b)
                bindings = self.addBinding(binding, bindings)
                
            elif(expr.__class__.__name__ == "MakeMenu"):
                self.checkVarname(expr,bindings)
                m = self.makeMenu(self.window,expr,bindings)
                options = self.getOptions(expr)
                binding = self.makeBinding("Menu", expr.varname, m, options)
                bindings = self.addBinding(binding,bindings)
                
            elif(expr.__class__.__name__ == "MakeMenuItem"):
                self.checkVarname(expr,bindings)
                mi = self.makeMenuItem(self.window,expr,bindings)
                options = self.getOptions(expr)
                binding = self.makeBinding("MenuItem", expr.varname, mi, options)
                bindings = self.addBinding(binding,bindings)
        
            elif(expr.__class__.__name__ == "MakeTextBox"):
                self.checkVarname(expr,bindings)
                t = self.makeTextBox(self.window, expr)
                binding = self.makeBinding("TextBox", expr.varname, t)
                bindings = self.addBinding(binding,bindings)
                
            
            
            #   SET
            elif(expr.__class__.__name__ == "SetWindow"):
                window = self.getObject(expr,bindings)
                assert w.bType == 'Window'
                w = self.setWindow(window,expr)
                
            elif(expr.__class__.__name__ == "SetButton"):
                button = self.getObject(expr,bindings)
                assert w.bType == 'Button'
                b = self.setButton(button,expr)
                
            elif(expr.__class__.__name__ == "SetMenu"):
                pass
                
            elif(expr.__class__.__name__ == "SetMenuItem"):
                pass
        
            elif(expr.__class__.__name__ == "SetTextBox"):
                pass
                

                

            #               FUNCTIONS
            elif(expr.__class__.__name__ == "FunctionDefinition"):
                print("Expr", expr)
                if hasattr(expr, "funcname"):
                    #Checks bindings to see if function name is already there
                    print("Expr", expr.funcaction)
                    for i in range(len(expr.funcaction)):
                        print("i",expr.funcaction[i])
                        b = self.interpret([expr.funcaction[i]], bindings) #this putting i in a list is stupid and Leah fully admits it
                        # b = self.interpret(expr.funcaction[i], bindings) #this putting i in a list is stupid and Leah fully admits it

                        expr.funcaction[i] = b
                    print("expr after", expr.funcaction)

                    if expr.funcname in bindings:
                        self.error("Sorry, this function name is already used.")

                    #If function isn't already defined, add it to bindings
                    else:
                        print("This is funcaction", expr.funcaction)
                        if hasattr(expr, "params"):

                            binding = self.makeBinding("Function", str(expr.funcname), expr.funcaction, expr.params)
                        else:
                            binding = self.makeBinding("Function", str(expr.funcname), expr.funcaction)
                        bindings = self.addBinding(binding,bindings)
                else:
                    self.error("Sorry, you need to give your function a name")

            elif(expr.__class__.__name__ == "FunctionCall"):
                #Find function with that name
                function = expr.funcname
                if function in bindings:
                    #Look at params in the bindings
                    #if hasattr(expr, "params"):
                    print(bindings[function])
                    localBindings = dict()
                    if len(expr.params)>0:
                        #Make set of local bindings

                        #Bind objects passed into parameter with parameter in function

                        #Take param being passed in (params), bind to expected param in function
                        #add this to local binding
                        functionParam = bindings[function].params[0]
                        #functionInput = bindings[functionParam[0]]
                        functionInput = bindings[expr.params[0]] #Assuming only one parameter in

                        b = self.makeBinding(functionInput.bType, functionParam, functionInput.bObject) #Here we're setting the type of the local to the thing that we're passing in. This is shitty
                        localBindings = self.addBinding(b, localBindings)
                        newBindings = self.runFunction(bindings,function,localBindings)
                        newB = newBindings[functionParam]
                        newB.varname = functionInput.varname

                        #need to bind the returned object to the thing that it modified
                        bindings[functionInput.varname] = newB


                    else:
                        newBindings = self.runFunction(bindings,function,localBindings)



                else:
                    self.error("This function isn't defined.")


            elif(expr.__class__.__name__ == "Line"):
                print("It's a line!")
                print(expr.lineAction)
                return expr.lineAction
            elif(expr.__class__.__name__ == "Return"):
                print("It's a param!")
                print(expr.param)
                return expr.param


                #Look at parameters in bindings
                #If there are parameters, make local bindings for them and run function on those
                #Get rid of local bindings after

        return bindings









    #               WINDOWS
    #Make a window
    def makeWindow(self,w,expr):
        print("making window")
        w.deiconify() #Show the window
        if hasattr(expr, "attributes"):
            for item in expr.attributes:
                if hasattr(item, 'color'):
                    w.configure(bg=item.color.value)
                elif hasattr(item,'size'):
                    if item.size.value[0] == "[":
                        nums = re.findall(r'\d+',item.size.value)
                        rows = int(nums[0])
                        columns = int(nums[1])
                        #fill cells with empty space somehow, so the user gets a sense of it actually being a grid
                        for i in range(0,columns):
                            for j in range(0,rows):
                                text = Text(w)
                                text.insert(INSERT, "  ")
                                text.grid(row = j, column = i)

                    elif item.size.value[0].isdigit():
                        size = item.size.value+"x"+item.size.value
                        w.geometry(size)
                    else:
                        if item.size.value.lower() == "large":
                            w.geometry('500x500')
                        elif item.size.value.lower() == "small":
                            w.geomerty('200x200')
        return w

    #Set a window
    def setWindow(self,w,expr):
        if hasattr(expr, "attributes"):
            for item in expr.attributes:
                if hasattr(item, 'color'):
                    #self.window.configure(bg=item.color.value)
                    w.configure(bg=item.color.value)
                elif hasattr(item,'size'):
                    if item.size.value[0] == "[":
                        nums = re.findall(r'\d+',item.size.value)
                        rows = int(nums[0])
                        columns = int(nums[1])
                        for i in range(0,columns):
                            for j in range(0,rows):
                                text = Text(w)
                                text.insert(INSERT, "  ")
                                text.grid(row = j, column = i)

                    elif item.size.value[0].isdigit():
                        size = item.size.value+"x"+item.size.value
                        w.geometry(size)
                    else:
                        if item.size.value.lower() == "large":
                            w.geometry('500x500')
                        elif item.size.value.lower() == "small":
                            w.geomerty('200x200')
        return w



    #               TEXT BOX
    def makeTextBox(self,w,expr):
        t = Text(w, height=2, width=30)
        if hasattr(expr, "attributes"):
            for item in expr.attributes:
                if hasattr(item, 'text'):
                    t.insert(END, item.text.value)
                    t.pack()
                else:
                    print("you done goofed")
        return t



    #               BUTTONS
    #Make a Button
    #Takes in the window the button should be made in and the expression
    def makeButton(self,w,expr):
        #b = Button(self.window)
        b = Button(w, bd=-2)
        #b.configure(bd=-2)
        if hasattr(expr, "attributes"):
            for item in expr.attributes:
                if hasattr(item, 'color'):
                    print("THis is the color: ", item.color.value)
                    b.configure(bg=item.color.value)
                    print(b.cget('bg'))
                if hasattr(item, 'text'):
                    #b.configure(text=item.test.textValue)
                    b.configure(text=item.text.value)
                elif hasattr(item,'size'):
                    b.configure(width=item.size.value)
                    b.configure(height=item.size.value)

                # These are the action statements
                elif hasattr(item, 'action'):
                    #Cast action to string, otherwise you cannot find right action
                    #This is temporary until I can call the action as a direct line in the command
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

                    # else:
                    #     print("You have entered a command that is not defined")

        b.pack()
        return b

    #Set a Button
    def setButton(self,b,w,expr):
        for item in expr.attributes:
            if hasattr(item, 'color'):
                b.configure(bg=item.color.value)
            if hasattr(item, 'text'):
                b.configure(text=item.text.value)
            elif hasattr(item,'size'):
                b.configure(width=item.size.value)
                b.configure(height=item.size.value)
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








    #               MENUS
    def makeMenu(self,w,expr,bindings):
        rootMenu = None
        children = w.winfo_children()
        for c in children:
            if type(c).__name__ == "Menu":
                rootMenu = c
        w.config(menu=rootMenu)
        return rootMenu

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
                                if v[0] == '"':
                                    subMenu.add_command(label=v[1:-1],command=self.runFunction)
                    menuItem = subMenu
                    w.config(menu=bindings[key].bObject)

        return menuItem






    #               HELPER METHODS
    def makeBinding(self,t,v,o,p=[]):
        binding = Binding(t,v,o,p)
        return binding

    #Takes a binding in the form shown in "makeBinding" and adds to bindings
    def addBinding(self,b,bindings):
        bindings[b.varname] = b
        return bindings

    #Make the binding associated with this function
    #The object will be the parameters passed in and the function action (in a tuple)
    def makeFunction(self,w, expr):
        pass

    #this should maybe take in parameters
    #expects "run" then a user defined function name
    #replaces , separating gooey instructions and adds period at end
    #Makes a temporary binding relating to parameters and then gets rid of that parameter
    def runFunction(self,bindings,function,localBindings):
        print("\n\n I'm running runFunction!")
        functionCode = bindings[function].bObject #We need to make this proper gooey code
        newBindings = localBindings
        print("New Bindings: ", newBindings)
        for action in functionCode:
            print("Here's the action", action)
            newBindings = self.interpret([action], newBindings)
            # newBindings = self.interpret(action, newBindings)

            print("New Bindings: ", newBindings)
        return newBindings
        # funStr = ''
        # for i in functionCode:
        #     funStr = funStr + " " + i
        # funStr = funStr[1:] + "."
        # #parse the function code and pass the parsed code as the ast
        # localAst = parse(funStr,Program)
        # newBindings = self.interpret(localAst,localBindings)
        # return newBindings


    #get list of options, ie: make MenuItem with options [red green blue].
    def getOptions(self,expr):
        for item in expr.attributes:
            if hasattr(item, 'options'):
                print(item.options.value)
                return item.options.value
            else:
                return None
            
    def checkVarname(self,exp,bindings):
        if hasattr(exp, "varname"):
            #if expr.varname in bindings:
            if exp.varname in bindings:
                message = exp.varname, "already defined."
                self.error(message)
                
    def getObject(self,exp,bindings):
        if exp.varname in bindings:
            return bindings[exp.varname].bObject
        else:
            message = exp.varname, "undefined."
            self.error(message)
            
        
                
