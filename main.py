from tkinter import * 
#ak sa nemylim, tak ta hviezdicka znamena importuj vsetko z kniznice, cize ten import pod tym uz nie je potrebny
#from tkinter import messagebox
from tkinter import messagebox #toto treba pre časť menu info - vyskakovacie okno 
import ctypes # to este neviem, co je
import random
#own code
from classes.card import Card #importovanie triedy Card

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

#kiniznica specificka pre Windows
#yy = ctypes.windll.user32
#x = yy.GetSystemMetrics(0) 
#y = yy.GetSystemMetrics(1) - 120

#zatial si dam staticku velkost okna
x = 800
y = 600

#vytvorim okno
root = Tk() 

#v okne vytvorim platno, na ktore sa da kreslit ciary, utvary...
canvas = Canvas(root, width = x, height = y)
#este netreba zobrazit to, co je na platne, lebo na nom nic neni
#canvas.pack()

menubar = Menu(root) #vytvorim menu
hra = Menu(menubar, tearoff=0) #podmenu, neviem co je tearoff
hra.add_command(label="Nova hra!", command=novahra) #pridanie polozky do podmenu priradenie funkcie, ktora sa po jeho stlaceni spusti
hra.add_separator() #pridanie oddelovaca
hra.add_command(label="Koniec!", command=novahra) # pridanie dalsej polozky a priradenie funkcie
menubar.add_cascade(label="Hra", menu=hra) #pridanie podmenu na hlavny panel menu a pridanie jeho nazvu "Hra"

#to iste ako vyssie, tak pozri tam
info = Menu(menubar, tearoff=0)
info.add_command(label="O nás!", command=onas)
menubar.add_cascade(label="Info", menu=info)
root.config(menu=menubar)

#Petove vypocty
i = 1
g = 55
p = g

def dvadva():
   cisla = [1, 2, 3, 4]
   random.shuffle(cisla)
   if cisla[0] == 1 or cisla[0] == 2:
      color1 = "orange"
   else:
      color1 = "green"
   if cisla[1] == 1 or cisla[1] == 2:
      color2 = "orange"
   else:
      color2 = "green"
   if cisla[2] == 1 or cisla[2] == 2:
      color3 = "orange"
   else:
      color3 = "green"
   if cisla[3] == 1 or cisla[3] == 2:
      color4 = "orange"
   else:
      color4 = "green"
   nn = y / 3
   yy = x / 2.5
   canvas.create_rectangle(yy, nn, yy + 60, nn + 90, fill=color1)
   canvas.create_rectangle(yy + 95, nn, yy + 60 + 95, nn + 90, fill=color2)
   canvas.create_rectangle(yy, nn + 125, yy + 60, nn + 90 + 125, fill=color3)
   canvas.create_rectangle(yy + 95, nn + 125, yy + 60 + 95, nn + 90 + 125, fill=color4)
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

def onObjectClick(event):
    canvas.delete(event.widget.find_closest(event.x, event.y))

#priklad pouzitia novovytvorenej triedy Card
c1 = Card(0, 800 / 2.5, 600 / 3, 800 / 2.5 + 60, 600 / 3 + 90, canvas) #vytvorime a nastavime parametre karty
canvas.tag_bind(c1.back, '<ButtonPress-1>', onObjectClick) #prepojime funkciu so zadnou stranou karty
canvas.pack() 

#ciselnik pridavame do okna, moze sa hybat v rozsahu hodnot 0 az 300 a zmena jeho hodnoty vola funkciu myFunc
spin = Spinbox(root, from_ = 0, to = 300, command=myFunc)
#pridanie ciselniku
spin.pack()

root.mainloop()
