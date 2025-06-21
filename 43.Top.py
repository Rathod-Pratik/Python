from tkinter import *
r=Tk()
def f():
    top=Toplevel(r)
    t=Text(top,bd=10)
    t.pack()

b=Button(r,text="open",command=f)
b.pack()
r.mainloop()