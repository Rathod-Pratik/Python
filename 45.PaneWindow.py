from tkinter import *
r=Tk()

p=PanedWindow(orient="horizontal")

b=Button(p,text="Hi")
b.pack()

b1=Button(p,text="hi")
b1.pack()

p.pack()
p.add(b)
p.add(b1)

r.mainloop()