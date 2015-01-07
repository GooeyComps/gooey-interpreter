from pypeg2 import *
from tkinter import *
from logicFile import *

'''
Right now interpreter is set up to take in the tree and the root, which
is how threadtest.py

In our old main.py, it doesn't send a root into interpreter, so you'll get an error
'''
def interpret(tree, root):

    #default window settings
    root.geometry("200x200+100+50")
    for expr in tree:
        if hasattr(expr, "type"):
            print("TYPE")
            if (expr.type == "Window"):
                #print("WIN")
                #Leah added this during finals fall term
                top = Toplevel()
                for item in expr.attributes:
                    if hasattr(item, 'color'):
                        top.configure(bg=item.color.value)
                    elif hasattr(item,'size'):
                        size = item.size.value+"x"+item.size.value
                        top.geometry(size)

            elif (expr.type == "Button"):
                b = Button(root)
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
        else:
            print("else")

            for item in expr.attributes:
                if hasattr(item, 'color'):
                    top.configure(bg=item.color.value)
                elif hasattr(item,'size'):
                    size = item.size.value+"x"+item.size.value
                    top.geometry(size)
    print("I DID IT")
    #top.mainloop()
    #print("looping forever")
    return root
