from tkinter import *
import actionbuttons

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text = "QUIT", fg = "red", command = frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame, text = "Hello", command = actionbuttons.Actions.write_something)
        self.slogan.pack(side=LEFT)


root = Tk()
app = App(root)
root.mainloop()
