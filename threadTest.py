import queue
import threading
import sys
from make import *
from settype import *
from interpreter import *
from tkinter import *

class Program(List):
    grammar = maybe_some([Make,GooeySet])
class GUIThread(threading.Thread):
    def __init__(self, q):
        super(GUIThread, self).__init__()
        self.q = q
        self.start()
        #top = Tk()
        #top.geometry("200x200+100+50")
        #top.mainloop()
    #def run(self,q):

    def run(self):
        i = self.q.get()
        parsed = parse(i,Program)
        tree = interpret(parsed)

        #tree.mainloop()
        #top = Tk()
        #top.mainloop()
        #print("run thread")

class IOThread(threading.Thread):
    def __init__(self, q):
        super(IOThread, self).__init__()
        self.q = q
        self.start()
    #def run(self, q):
    def run(self):
        #print("HI HI HI")
        while True:
            #print("in da while")
            #below: used to have input("input: ") but we can't have that right now
            gooey =  sys.stdin.readline() #this causes Tcl_WaitForEvent: Notifier not initialized
            print(gooey)
            self.q.put(gooey)
            self.q.task_done()

def main():
    q = queue.Queue()
    io = IOThread(q)
    #gui = GUIThread(q)
    #print("starting gui thread")
    #gui.start()
    #print("Starting io thread")
    #io.start()
    while True:
        i = q.get()
        parsed = parse(i,Program)
        tree = interpret(parsed)



if __name__ == "__main__":
    main()
