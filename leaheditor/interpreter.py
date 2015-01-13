from tkinter import *
from pypeg2 import *
#Takes in the type t, varname v, and actual object o, returns binding
#Later we should maybe do error checking to make sure type and object match?
#Or this might get caught earlier
#Maybe this shouldn't have varname in the dict? Unclear
def makeBinding(t,v,o):
    binding = {'type': t, 'varname': v, 'object': o}
    return binding

#Takes a binding in the form shown in "makeBinding" and adds to bindings
def addBinding(b,bindings):
    bindings[b['varname']] = b
    return bindings

#Make a window
#w
def makeWindow(w,expr):
    w.deiconify() #Show the window
    if hasattr(expr, "attributes"):
        for item in expr.attributes:
            if hasattr(item, 'color'):
                w.configure(bg=item.color.value)
            elif hasattr(item,'size'):
                size = item.size.value+"x"+item.size.value
                w.geometry(size)
    return w

#Set a window
def setWindow(w,expr):
    if hasattr(expr, "attributes"):
        for item in expr.attributes:
            if hasattr(item, 'color'):
                #self.window.configure(bg=item.color.value)
                w.configure(bg=item.color.value)
            elif hasattr(item,'size'):
                size = item.size.value+"x"+item.size.value
                #self.window.geometry(size)
                w.geometry(size)
    return w

#Make a Button
#Takes in the window the button should be made in and the expression
def makeButton(w,expr):
    #b = Button(self.window)
    b = Button(w)
    if hasattr(expr, "attributes"):
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
    return b

#Set a Button
def setButton(b,expr):
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
    return b

class Interpreter():
    def __init__(self, target):
        self.window = target
        #self.localBindings = dict()

    def error(self, message):
        errorPopup = Toplevel()
        errorPopup.title("Error")
        errorPopup.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
        msg = Message(errorPopup, text=message)
        msg.pack()

        button = Button(errorPopup, text="Ok", command=errorPopup.destroy)
        button.pack()
        #self.window.destroy()
    def make(self, ast, bindings):
        print(ast)
    def gooeyset(self, ast, bindings):
        print(ast)

    def interpret(self, ast, bindings):
        print("Interpreting")
        for expr in ast:
            if(expr.__class__.__name__ == "Make"):
                if hasattr(expr, "type"):
                    if hasattr(expr, "varname"):
                        if expr.varname.thing in bindings:
                            message = expr.varname.thing, "already defined."
                            self.error(message)
                            break
                        else:
                            if (expr.type == "Window"):
                                w = makeWindow(self.window,expr)
                                binding = makeBinding("Window", expr.varname.thing, w)
                                bindings = addBinding(binding, bindings)

                            elif (expr.type == "Button"):
                                b = makeButton(self.window,expr)
                                binding = makeBinding("Button", expr.varname.thing, b)
                                bindings = addBinding(binding,bindings)

                    else:
                        self.error("no varname")
            elif(expr.__class__.__name__ == "GooeySet"):
                if hasattr(expr, "varname"):
                    if expr.varname.thing in bindings:
                        obj = bindings[expr.varname.thing]
                        #####Should we just be modifying the self.window or should we be searching through the bindings??
                        if obj['type'] == "Window":
                            win = obj['object']
                            w = setWindow(win,expr)
                        #elif(expr.type == "Button"):
                        elif obj['type'] == "Button":
                            button = obj['object']
                            b = setButton(button,expr)
                    else:
                        self.error("undefined varname")

        return bindings
