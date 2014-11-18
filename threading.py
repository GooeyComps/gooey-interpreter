import Queue
import threading
import tkinter


class GUIThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        top = Tk()
        top.geometry("200x200+100+50")
        top.mainLoop()
        
class IOThread(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            gooey = input("input: ")
            
            
if __name__ == "__main__":
    q = Queue.Queue()