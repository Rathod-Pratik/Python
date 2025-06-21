from tkinter import *
r=Tk()

s=Scrollbar(r)

s.pack(side=RIGHT,fill='y')
l=Listbox(r,yscrollcommand=s.set)
for i in range(30):
    l.insert(END,i)
l.pack()
s.config(command=l.yview)
r.mainloop()