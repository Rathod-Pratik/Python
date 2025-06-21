from tkinter import *
r=Tk()

t=Text(r,fg="green",wrap="word",width=10,height=10,bd=10,font=("batang",19,"bold"))

t.insert("1.0","Ok \n")
t.insert("2.0","Ok1")

t.config(state="disabled")

t.pack()
r.mainloop()