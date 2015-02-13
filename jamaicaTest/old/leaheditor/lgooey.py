
from interpreter import *
from tkinter import *
from grammar import *
from tkinter.scrolledtext import *
from pypeg2 import *

'''
This file creates a text editor that echoes the file content into a separate tkinter window using that
window's "pack" method. So we are able to get new content into the window via packing without reloading the
entire window.

This is done with a "Run" option in the original text editor window
'''

class GUIWindow():
   # def __init__(self, window):
    #Changed this so that it doesn't take in a window - it just initializes the live preview when it begins
    def __init__(self):
        #self.window = window
        self.window = Tk(className="Live Preview")
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
        #if (self.is_open):
            #self.stop()
        #self.window.destroy()
        #previewTkObj = tk.Tk(className="Live Preview")
        #self.window = previewTkObj
        #self.openWindow()
        #self.window.withdraw()
        #self.update_preview()

        #create new instance of interpeter class, passing a reference the live preview window
        i = Interpreter(self.window)

        self.bindings = i.interpret(ast, self.bindings)
        del i


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
        #previewTkObj = tk.Tk(className="Live Preview")
        #self.preview = GUIWindow(previewTkObj)
        #self.preview = GUIWindow()
        ast = parse(self.text, Program)
        self.preview.modify(ast)
        #After it takes in a command and does something it deletes all of the text from the textbox
        self.textPad.delete('1.0',END)
        '''
        if hasattr(self,"preview"):
            if self.preview.is_open:
                try:
                    self.retrieve_input()
                    ast = parse(self.text, Program)

                    self.preview.modify(ast)

                except SyntaxError as e:

                    popup = Toplevel()
                    popup.title("Error")
                    popup.geometry("%dx%d%+d%+d" % (200, 200, 200, 200))
                    error = "Syntax Error:", e
                    msg = Message(popup, text=error)
                    msg.pack()

                    button = Button(popup, text="Ok", command=popup.destroy)
                    button.pack()
                    #self.stop_preview()

            else:
                self.open_preview()
        else:
            self.open_preview()
        '''

    def open_preview(self):
        if hasattr(self,"preview"):
            if not self.preview.is_open:

            #live preview window
                #self.previewTkObj = tk.Tk(className="Live Preview")
                #self.previewTkObj.protocol("WM_DELETE_WINDOW", self.on_close)
                #self.preview = GUIWindow(self.previewTkObj)
                #self.preview = GUIWindow()
                self.preview.openWindow()
                self.update_preview()
        else:
            #live preview window
            #self.previewTkObj = tk.Tk(className="Live Preview")
            #self.previewTkObj.protocol("WM_DELETE_WINDOW", self.on_close)
            #self.preview = GUIWindow(self.previewTkObj)
            #self.preview = GUIWindow()
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

    textpad = TextPad()
    textpad.run()
