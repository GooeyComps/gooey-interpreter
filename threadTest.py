import queue
import threading
from tkinter import *


class GUIThread(threading.Thread):
    def __init__(self, queue):
        super(GUIThread, self).__init__()
        self.queue = queue
        top = Tk()
        top.geometry("200x200+100+50")
        #top.mainloop()
    def run(self, queue):
        print("run thread")
        
class IOThread(threading.Thread):
    def __init__(self, queue):
        super(IOThread, self).__init__()
        self.queue = queue
    def run(self, queue):
        while True:
            gooey = input("input: ")
            self.queue.put(gooey)
            #self.queue.task_done()
   
def main():
    q = queue.Queue()
    io = IOThread(q)
    gui = GUIThread(q)
    
    
            
if __name__ == "__main__":
    main()

