
from interpreter import *
from tkinter import *
from statements import *
from tkinter.scrolledtext import *
from pypeg2 import *
import argparse
from tkinter import font

class GUIWindow():
    '''
    Wrapper class for the live preview window
    '''
    def __init__(self):
        '''
        Initializes preview window, bindings, and master window binding.
        '''
        self.window = Tk(className="Live Preview")
        self.window.resizable(width=False, height=False)
        m = Menu(self.window)
        self.window.config(menu=m)

        self.bindings = dict()
        # Keep track of the binding linked to our master window
        self.winBinding = None
        self.is_open = False

    def openWindow(self):
        '''
        Open the preview window.
        '''
        self.is_open = True
        self.window.deiconify()

    def stop(self):
        '''
        Close the preview window.
        '''
        self.is_open = False

    def modify(self, gooeyCode):
        '''
        Takes string Gooey code, parses and interprets it, and updates the preview window.
        Throws SyntaxError if syntax is incorrect, or GooeyError if there is an interpreter error.
        '''
        #create new instance of interpeter class, passing a reference the live preview window
        i = Interpreter(self.window,self.winBinding,self.bindings)
        
        ast = parse(gooeyCode, Program)

        (self.bindings,self.winBinding) = i.interpret(ast)
        del i
class TextPad():
    '''
    Interactive Gooey editor window.
    '''
    def __init__(self):
        '''
        Initializes the window and its elements:
        an editor text pad, a definitions window where previously entered code stays,
        a menu bar with run and stop options, and run and stop buttons.
        '''
        self.root = Tk(className="Gooey Editor")

        # Text content of the text editor window
        self.text = ""

        # Add a menu bar with run and stop options.
        m = Menu(self.root)
        self.root.config(menu=m)
        fm = Menu(m)
        m.add_cascade(label="File",menu=fm)
        fm.add_command(label="Run",command=self.update_preview)
        fm.add_command(label="Stop",command=self.stop_preview)

        self.textSize = 12

        # Add a "definitions" text area so users can see what has already been input, but cannot edit it.
        self.definitionLabel = Label(text="Definitions")
        self.definitionLabel.pack()

        self.definitions = ScrolledText(self.root, width=60, height=10, state=DISABLED)
        self.definitions.configure(highlightbackground="black", fg="gray30",bg="gray95")
        self.definitions.pack(padx=(12,0))

        # Add the editing text pad
        self.editLabel = Label(text="Enter Code Below")
        self.editLabel.pack()

        # Add text pad to root and open window
        self.textPad = ScrolledText(self.root, width=59, height=10)
        # Add a border to the text pad
        self.textPad.configure(borderwidth=4, highlightbackground="black")
        self.textPad.pack(padx=(12,0))

        self.configText()

        # Add run and stop buttons
        # Run and Stop Icons made by Freepik <http://www.freepik.com> from Flaticon <http://www.flaticon.com> is licensed under Creative Commons BY 3.0 <http://creativecommons.org/licenses/by/3.0/>
        self.runIcon = PhotoImage(file="runIcon.gif")
        self.stopIcon = PhotoImage(file="stopIcon.gif")
        # Plus and Minus Icons made by Icomoon <http://www.icomoon.io> from Flaticon <http://www.flaticon.com> is licensed under Creative Commons BY 3.0 <http://creativecommons.org/licenses/by/3.0/>
        self.plusIcon = PhotoImage(file="plusIcon.gif")
        self.minusIcon = PhotoImage(file="minusIcon.gif")

        self.decrementButton = Button(self.root)
        self.decrementButton.configure(image=self.minusIcon, command=self.decrementEditorSize)
        self.decrementButton.pack(side=LEFT)

        self.incrementButton = Button(self.root)
        self.incrementButton.configure(image=self.plusIcon, command=self.incrementEditorSize)
        self.incrementButton.pack(side=LEFT)

        self.stopButton = Button(self.root)
        self.stopButton.configure(image=self.stopIcon, command=self.stop_preview)
        self.stopButton.pack(side=RIGHT)

        self.runButton = Button(self.root)
        self.runButton.configure(image=self.runIcon, command=self.update_preview)
        self.runButton.pack(side=RIGHT)

        #This is where the GUIWindow class is first called - since GUIWindow
        #makes a live preview window when it is initialized, we hide it until we need it
        self.preview = GUIWindow()
        self.preview.window.withdraw()

    def incrementEditorSize(self):
        self.textSize += 1
        self.configText()

    def decrementEditorSize(self):
        self.textSize -= 1
        self.configText()

    def configText(self):
        f = font.Font(size=self.textSize, font="TKHeadingFont")
        fmono = font.Font(size=self.textSize, family="Courier")
        self.definitionLabel.configure(font=f)
        self.editLabel.configure(font=f)
        self.definitions.configure(font=fmono)
        self.textPad.configure(font=fmono)

    def run(self):
        self.root.mainloop()

    def update_preview(self):
        '''
        Gets user input from editing text pad, parse and interpret it, and update the live preview window.
        '''
        self.retrieve_input()
        # Update preview window, handle errors gracefully.
        try:
            self.preview.modify(self.text)
        except SyntaxError as e:
            ErrorPopup("Syntax Error in line "+str(e.lineno)+".")
        except GooeyError:
            pass
        else:
            # If there was no error in the interpreter,
            # copy text in text pad to definitions box, and delete from text pad
            self.definitions.configure(state=NORMAL)
            self.definitions.insert(END, self.text)
            self.definitions.configure(state=DISABLED)
            self.textPad.delete('1.0',END)

    def open_preview(self):
        '''
        Open the preview window.
        '''
        if hasattr(self,"preview"):
            if not self.preview.is_open:
                self.preview.openWindow()
                self.update_preview()
        else:
            self.preview.openWindow()
            self.update_preview()

    def stop_preview(self):
        '''
        Close the preview window.
        '''
        if self.preview.is_open:
            self.preview.stop()
        self.root.destroy()
        exit()

    def on_close(self):
        self.preview.stop()

    def retrieve_input(self):
        '''
        Get user input from editor text pad and save in text instance variable.
        '''
        self.text = self.textPad.get('1.0', END)

def readFromFile(infile):
    '''
    Gets gooey code from input file, parses and interprets, and displays the output.
    '''
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
    except GooeyError:
        pass
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
