from tkinter import *
r=Tk()
r.geometry()

l=Listbox(r,height=5,width=20,bg='pink',fg='red',font=("batang",18,"bold"),activestyle=None)
l.insert(1,"Pizza")
l.insert(2,"Burger")
l.insert(3,"Chinse")

l.pack()
l.selection_anchor(1)
l.select_set(ANCHOR,2)

r.mainloop()