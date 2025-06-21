from tkinter import *

t=Tk()

def f():
    print("Ok")
def f1():
    print("Okey")

r=Radiobutton(t,text="1",value=1,command=f)
r.pack()
r1=Radiobutton(t,text="2",value=2,command=f1)
r1.pack()
r.mainloop()