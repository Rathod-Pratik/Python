from tkinter import *
r=Tk()

s=Scrollbar(r,orient=HORIZONTAL)
s.pack(side="bottom",fill=X)

t=Listbox(r,xscrollcommand=s.set,width=20)
for i in range(30):
    t.insert(END,f"Item Number {i} from this List of file it is Horizontal scroll Bar")

t.pack(side=RIGHT,fill=BOTH)

s.config(command=t.xview)

r.mainloop()