from tkinter import *

class Actions:

    # Print something actions
    def write(printTest):
        print(printTest)

    # Close window actions
    def close(window):
        window.quit()

    # Change color of window actions
    def windowColorChange(window, c):
        window.configure(bg= c)
        print("here")

    # Submit button

    # Main method which goes through all other methods?  Maybe?
    # def callToAction(type):
    # Nevermind, won't work, still need to make action part of statement
