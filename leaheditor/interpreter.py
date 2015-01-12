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
                            #bindings[expr.varname.thing] = expr
                            if (expr.type == "Window"):
                                self.window.deiconify()
                                binding = makeBinding("Window", expr.varname.thing, self.window)
                                bindings = addBinding(binding,bindings)
                                #bindings[expr.varname.thing] = self.window
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
                                #bindings[expr.varname.thing] = b
                                binding = makeBinding("Button", expr.varname.thing, b)
                                bindings = addBinding(binding,bindings)

                    else:
                        self.error("no varname")
            elif(expr.__class__.__name__ == "GooeySet"):
                print("in set")
               # if hasattr(expr, "type"):
                if hasattr(expr, "varname"):
                    print("Has varname")
                    if expr.varname.thing in bindings:
                        obj = bindings[expr.varname.thing]
                        print("Hey! I found it!")
                        print(obj)
                        #if obj.type == "Window":
                        #####Should we just be modifying the self.window or should we be searching through the bindings??
                        if obj['type'] == "Window":
                            win = obj['object']
                            if hasattr(expr, "attributes"):
                                for item in expr.attributes:
                                    if hasattr(item, 'color'):
                                        #self.window.configure(bg=item.color.value)
                                        win.configure(bg=item.color.value)
                                    elif hasattr(item,'size'):
                                        size = item.size.value+"x"+item.size.value
                                        #self.window.geometry(size)
                                        win.geometry(size)
                        #elif(expr.type == "Button"):
                        elif obj['type'] == "Button":
                            button = obj['object']
                            for item in expr.attributes:
                                if hasattr(item, 'color'):
                                    button.configure(bg=item.color.value)
                                if hasattr(item, 'text'):
                                    button.configure(text=item.text.value)
                                elif hasattr(item,'size'):
                                    button.configure(width=item.size.value)
                                    button.configure(height=item.size.value)
                                elif hasattr(item, 'action'):
                                    print(item)
                                    #b.configure(command=item)
                            #b.pack()
                    else:
                        self.error("undefined varname")

        return bindings
