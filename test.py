from tkinter import *
from tkinter import messagebox
import ctypes
def novahra():
   filewin = Toplevel(root)
   button = Button(filewin, text="2x2", height= 3, width = 20, command=dvadva)
   button1 = Button(filewin, text="4x4", height= 3, width= 20)
   button2 = Button(filewin, text="6x6", height= 3, width= 20)
   button.pack()
   button1.pack()
   button2.pack()
def onas():
   messagebox.showinfo( "O nas!", "Lorem Ipsum...")
#yy = ctypes.windll.user32
#x = yy.GetSystemMetrics(0) 
#y = yy.GetSystemMetrics(1) - 120
x = 800
y = 600
root = Tk()
canvas = Canvas(root, width = x, height = y)
canvas.pack()
menubar = Menu(root)
hra = Menu(menubar, tearoff=0)
hra.add_command(label="Nova hra!", command=novahra)
hra.add_separator()
hra.add_command(label="Koniec!", command=novahra)
menubar.add_cascade(label="Hra", menu=hra)

info = Menu(menubar, tearoff=0)
info.add_command(label="O nás!", command=onas)
menubar.add_cascade(label="Info", menu=info)
root.config(menu=menubar)

i = 1
g = 55
p = g
def dvadva():
   """nn = y / 2 + y
   mm = x / 2 + x"""
   nn = y / 3
   yy = x / 2.5
   canvas.create_rectangle(yy, nn, yy + 60, nn + 90, fill='blue')
   canvas.create_rectangle(yy + 95, nn, yy + 60 + 95, nn + 90, fill='blue')
   canvas.create_rectangle(yy, nn + 125, yy + 60, nn + 90 + 125, fill='blue')
   canvas.create_rectangle(yy + 95, nn + 125, yy + 60 + 95, nn + 90 + 125, fill='blue')
   canvas.pack()
def myFunc():
    print(spin.get())
    a = int(spin.get())
    g = p * 2
    if 1 <= a:
        d = a * 55 - g
        b = d + 50
    else:
        b = d + 50
        d = 0
    
    canvas.create_rectangle(d, 1, b, 80, fill='blue')
    canvas.pack()

spin = Spinbox(root, from_ = 0, to = 300, command=myFunc)
spin.pack()


root.mainloop()
