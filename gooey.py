
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
        self.window.resizable(width=False, height=False)
        m = Menu(self.window)
        self.window.config(menu=m)
        #What if each binding is a dictionary element that contains type and varname?

        self.bindings = dict()
        self.winBinding = None #This is used to keep track of the binding linked to our master window
        self.is_open = False

    def openWindow(self):
        self.is_open = True
        #self.window.mainloop()
        self.window.deiconify()
    def stop(self):
        self.is_open = False
        #self.window.destroy()

#    def modify(self, ast):
#                '''
#        Takes string Gooey code, parses and interprets it, and updates the preview window.
#        Throws SyntaxError if syntax is incorrect, or GooeyError if there is an interpreter error.
#        '''
#        #create new instance of interpeter class, passing a reference the live preview window
#        i = Interpreter(self.window,self.winBinding,self.bindings)
#
#        (self.bindings, self.winBinding) = i.interpret(ast)
#        del i
    def modify(self, gooeyCode):
        '''
        Takes string Gooey code, parses and interprets it, and updates the preview window.
        Throws SyntaxError if syntax is incorrect, or GooeyError if there is an interpreter error.
        '''
        #create new instance of interpeter class, passing a reference the live preview window
        i = Interpreter(self.window,self.winBinding,self.bindings)

        ### START EMILY CHANGES
        ast = parse(gooeyCode, Program)
        ### END EMILY CHANGES ###

        (self.bindings,self.winBinding) = i.interpret(ast)
        del i
'''
Class for the text pad window where the user types their input
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


### START EMILY CODE ###
        # Add a "definitions" text area so users can see what they've already input but cannot edit it
        self.definitionLabel = Label(text="Definitions")
        self.definitionLabel.pack()

        self.definitions = ScrolledText(self.root, width=60, height=10, state=DISABLED)
        self.definitions.configure(highlightbackground="black", fg="gray30",bg="gray95")
        self.definitions.pack(padx=(12,0))

        # Editing area/text pad
        self.editLabel = Label(text="Enter Code Below")
        self.editLabel.pack()
### END EMILY CODE ###


        #add textPad to root and open window
        self.textPad = ScrolledText(self.root, width=59, height=10)

### START EMILY CODE ###
        # Add a border to the text pad
        self.textPad.configure(borderwidth=4, highlightbackground="black")
### END EMILY CODE ###


        self.textPad.pack(padx=(12,0))

### START EMILY CODE ###
        # Add run and stop buttons to the text pad
        self.runIcon = PhotoImage(file="runIcon.gif")
        self.stopIcon = PhotoImage(file="stopIcon.gif")

        self.stopButton = Button(self.root)
        self.stopButton.configure(image=self.stopIcon, command=self.stop_preview)
        self.stopButton.pack(side=RIGHT)

        self.runButton = Button(self.root)
        self.runButton.configure(image=self.runIcon, command=self.update_preview)
        self.runButton.pack(side=RIGHT)
### END EMILY CODE ###


        #This is where the GUIWindow class is first called - since GUIWindow
        #makes a live preview window when it is initialized, we hide it until we need it
        self.preview = GUIWindow()
        self.preview.window.withdraw()

    def run(self):
        self.root.mainloop()

    def update_preview(self):
#        self.retrieve_input()
#
#### START EMILY CODE ###
#        self.definitions.configure(state=NORMAL)
#        self.definitions.insert(END, self.text)
#        self.definitions.configure(state=DISABLED)
#### END EMILY CODE ###
#
#        ast = parse(self.text, Program)
#        self.preview.modify(ast)
#        #After it takes in a command and does something it deletes all of the text from the textbox
#        self.textPad.delete('1.0',END)
        self.retrieve_input()

        ### START EMILY CHANGES ###
        # moved parsing from here up to GUIWindow.modify

        # Update preview window, handle errors gracefully.
        try:
            self.preview.modify(self.text)
        except SyntaxError as e:
            ErrorPopup("Syntax Error in line "+str(e.lineno)+".")
        else:
            # If there was no error in the interpreter,
            # copy text in text pad to definitions box, and delete from text pad
            self.definitions.configure(state=NORMAL)
            self.definitions.insert(END, self.text)
            self.definitions.configure(state=DISABLED)
            self.textPad.delete('1.0',END)
        ### END EMILY CHANGES ###

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

def readFromFile(infile):
    # Create bindings for Gooey program
    bindings = dict()
    winBinding = None
    # Make the preview window, and hide it until it is needed.
    preview = GUIWindow()
    preview.window.withdraw()

    # Parse, interpret, and execute the program
    i = Interpreter(preview.window,winBinding,bindings)
    try:
        ast = parse(infile.read(), Program)
        (bindings,winBindings) = i.interpret(ast)
    except SyntaxError as e:
        ErrorPopup("Syntax Error in line "+str(e.lineno)+".")
    preview.window.mainloop()

if __name__ == "__main__":
    #Create the command line argument parser
    parser = argparse.ArgumentParser()
    #Parser looks for the optional input filename argument
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()

    #If the input filename argument is something, open the file
    if args.infile.name != '<stdin>':
        readFromFile(args.infile)
    #Otherwise, open our text editor
    else:
        textpad = TextPad()
        textpad.run()

