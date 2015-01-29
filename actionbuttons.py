from tkinter import *


# class Actions:

# Print something actions
#def write(printTest):
def write(window, item):
    printTest = item.action.text
    print(printTest)
    #return (window, item)

# Close window actions
#def close(window):
def close(window, item):
    window.quit()
    #return (window, item)

# Change color of window actions
#def windowColorChange(window, c):
def windowColorChange(window,item):
    c = item.action.color
    window.configure(bg= c)
    #return (window,item)

def findAction(item):
    action = str(item.action.value)
    #a = "%s(window,item)" % action
    #print(a)
    #a = "Actions.%s(window,item)" % action
    a = "%s" % action
    return a

def callAction(window,item,action):

    # print(locals())
    # print(globals())
    exec(action+"(window,item)")



    # Submit button

    # Main method which goes through all other methods?  Maybe?
    # def callToAction(type):
    # Nevermind, won't work, still need to make action part of statement
