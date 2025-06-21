from tkinter import * 
r=Tk()

a=IntVar()
a1=IntVar()
def f():
    print(a.get())
def f1():
    print(a1.get())

c=Checkbutton(r,text="One",variable=a,command=f)
c.pack()
c1=Checkbutton(r,text="Two",variable=a1,command=f1)
c1.pack()

r.mainloop()