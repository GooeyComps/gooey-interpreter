from pypeg2 import *
from tkinter import *
from logicFile import *


def interpret(tree, top):

    #default window settings
    top.geometry("200x200+100+50")
    for expr in tree:
        if hasattr(expr, "type"):
            print("TYPE")
            if (expr.type == "Window"):
                print("WIN")
                for item in expr.attributes:
                    if hasattr(item, 'color'):
                        print("COLOR")
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
    return top
