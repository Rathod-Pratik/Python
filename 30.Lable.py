from tkinter import *
lables=Tk()

v=StringVar();

lb=Label(lables, textvariable=v)
v.set("Rathod")
lb.pack(side=LEFT)
lables.mainloop()