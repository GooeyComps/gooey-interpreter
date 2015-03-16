from tkinter import *

# Print something actions
def write(window, item):
    printTest = item.action.arguments
    print(printTest)

# Close window actions
def quit(window, item):
    window.quit()

# Change color of window actions
def windowColorChange(window,item):
    print("changingwindow")
    c = item.action.arguments
    print(c)
    window.configure(bg= c)

def findAction(item):
    action = str(item.action.funcname)
    a = "%s" % action
    return a

def findMenuAction(item):
    action = item
    a = "%s" % action
    return a

def callAction(window,item,action):
    exec(action+"(window,item)")

def checkActions(action):
    actionList = ['write','quit','windowColorChange','windowSizeChange']
    if action not in actionList:
        return False
    else:
        return True
