
from interpreter import *
from tkinter import *
from statements import *
from tkinter.scrolledtext import *
from pypeg2 import *
import argparse

'''
Wrapper class for the live preview window
'''
class GUIWindow():
   # def __init__(self, window):
    #Changed this so that it doesn't take in a window - it just initializes the live preview when it begins
    def __init__(self):
        #self.window = window
        self.window = Tk(className="Live Preview")
        m = Menu(self.window)
        self.window.config(menu=m)
        #What if each binding is a dictionary element that contains type and varname?
        
        self.bindings = dict()
        self.is_open = False

    def openWindow(self):
        self.is_open = True
        #self.window.mainloop()
        self.window.deiconify()
    def stop(self):
        self.is_open = False
        #self.window.destroy()

    def modify(self, ast):
        #create new instance of interpeter class, passing a reference the live preview window
        i = Interpreter(self.window)

        self.bindings = i.interpret(ast, self.bindings)
        del i

'''
Class for the text pad window wher the user types their input
'''
class TextPad():
    def __init__(self):
        #text editor window
        self.root = Tk(className="Gooey Editor")

        #refers to the content of the text editor window
        self.text = ""

        #text editor widgets
        m = Menu(self.root)
        self.root.config(menu=m)
        fm = Menu(m)
        m.add_cascade(label="File",menu=fm)
        fm.add_command(label="Run",command=self.update_preview)
        fm.add_command(label="Stop",command=self.stop_preview)

        #add textPad to root and open window
        self.textPad = ScrolledText(self.root, width=60, height=30)
        self.textPad.pack()

        #This is where the GUIWindow class is first called - since GUIWindow
        #makes a live preview window when it is initialized, we hide it until we need it
        self.preview = GUIWindow()
        self.preview.window.withdraw()

    def run(self):
        self.root.mainloop()

    def update_preview(self):
        self.retrieve_input()
        ast = parse(self.text, Program)
        self.preview.modify(ast)
        #After it takes in a command and does something it deletes all of the text from the textbox
        self.textPad.delete('1.0',END)


    def open_preview(self):
        if hasattr(self,"preview"):
            if not self.preview.is_open:
                self.preview.openWindow()
                self.update_preview()
        else:
            self.preview.openWindow()
            self.update_preview()

    def stop_preview(self):
        if self.preview.is_open:
            self.preview.stop()
        else:
            print("preview window not open")

    def on_close(self):
        print("on close")
        self.preview.stop()

    def retrieve_input(self):
        self.text = self.textPad.get('1.0', END)



if __name__ == "__main__":
    #Create the parser
    parser = argparse.ArgumentParser()
    #Parser looks for the optional filename argument
    parser.add_argument('filename', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    #If the filename argument is something, open the file
    if args.filename.name!='<stdin>':
        print("Hi")
        bindings = dict()
        preview = GUIWindow()
        preview.window.withdraw()

        for line in args.filename:
            ast = parse(line, Program)
            i = Interpreter(preview.window)

            bindings = i.interpret(ast, bindings)
            #del i
        preview.window.mainloop()

    #Otherwise, open our text editor
    else:
        textpad = TextPad()
        textpad.run()
