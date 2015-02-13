from tkinter import *
root = Tk()
root.configure(bg = "red")
b = Button(root, highlightbackground = root.cget('bg'))
b.pack()
print(root.cget('bg'))
root.mainloop()
