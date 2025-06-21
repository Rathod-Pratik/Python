from tkinter import *
r=Tk()
r.geometry("200x300")

def f():
    print(e.get())

e=Entry(r,width=50,bg="red")
e.pack()
b=Button(r,text='submit',command=f)
b.pack()

r.mainloop()