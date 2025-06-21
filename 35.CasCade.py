from tkinter import *
r=Tk()

r.geometry("200x300")

mb=Menu(r)
file=Menu(r)

mb.add_cascade(label='file',menu=file)
file.add_command(label="Ok")
file.add_command(label="Ok1")
r.config(menu=mb)

r.mainloop()