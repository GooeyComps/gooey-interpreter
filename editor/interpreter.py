from tkinter import *
from pypeg2 import *

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
                                bindings[expr.varname.thing] = self.window
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
                                bindings[expr.varname.thing] = b
                    else:
                        self.error("no varname")
                elif(expr.__class__.__name__ == "GooeySet"):
                    if hasattr(expr, "type"):
                        if hasattr(expr, "varname"):
                            if expr.varname.thing in bindings:
                                obj = bindings[expr.varname.thing]
                                if obj.type == "Window":
                                    if hasattr(expr, "attributes"):
                                        for item in expr.attributes:
                                            if hasattr(item, 'color'):
                                                self.window.configure(bg=item.color.value)
                                            elif hasattr(item,'size'):
                                                size = item.size.value+"x"+item.size.value
                                                self.window.geometry(size)
                                elif(expr.type == "Button"):
                                    for item in expr.attributes:
                                        if hasattr(item, 'color'):
                                            obj.configure(bg=item.color.value)
                                        if hasattr(item, 'text'):
                                            obj.configure(text=item.text.value)
                                        elif hasattr(item,'size'):
                                            obj.configure(width=item.size.value)
                                            obj.configure(height=item.size.value)
                                        elif hasattr(item, 'action'):
                                            print(item)
                                            #b.configure(command=item)
                                    #b.pack()
                            else:
                                self.error("undefined varname")
                                
        return bindings