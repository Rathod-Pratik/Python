from tkinter import *
f=Tk()

f.geometry("500x300")

c=Canvas(f,bg="pink",height="200",width="300")
l=c.create_line(50,100,150,200)

c.pack()
f.mainloop()