from tkinter import *
r=Tk()

def f():
    print("a")

s=Spinbox(r,from_=11,to=15,command=f)
s.pack(side=RIGHT,fill='y')

r.mainloop()