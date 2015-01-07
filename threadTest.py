import queue
import threading
import sys
from make import *
from settype import *
from interpreter import *
from tkinter import *

'''
This is our thread experimentation from finals period fall term
'''
class Program(List):
    grammar = maybe_some([Make,GooeySet])


class GUIThread(threading.Thread):
    def __init__(self, q, root):
        super(GUIThread, self).__init__()
        self.q = q
        self.start()
        self.root = root
        #top = Tk()
        #top.geometry("200x200+100+50")
        #top.mainloop()
    #def run(self,q):

    def run(self):
        print("Hello, friends")
        while True:
            i = self.q.get()
            parsed = parse(i,Program)
            tree = interpret(parsed,self.root)

        #tree.mainloop()

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
            #This adds actions to the queue


            #below: used to have input("input: ") but we can't have that right now
            gooey =  sys.stdin.readline() #this causes Tcl_WaitForEvent: Notifier not initialized
            print(gooey)
            self.q.put(gooey)
            self.q.task_done()

def main():
    q = queue.Queue()
    root = Tk()
    root.withdraw()
    io = IOThread(q)


    gui = GUIThread(q,root)
    print(str(root.winfo_children()))
    root.mainloop()
    #How to get the info about the root while mainloop is running?



    #Right now it seems like we have 3 threads that aren't totally operating
    #with each other the way we want


    
    #print("starting gui thread")
    #gui.start()
    #print("Starting io thread")
    #io.start()




if __name__ == "__main__":
    main()
