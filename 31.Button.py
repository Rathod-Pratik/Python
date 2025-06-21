from tkinter import *

r=Tk()
r.geometry("300x300")
def f():
    print("Ok")

b= Button(r,text="Ok",bg='red',fg="white",command=f)
b.pack(side=RIGHT);
b= Button(r,text="Ok1",bg='green',fg="white",height=3,width=3)
b.pack(side=LEFT)
r.mainloop()