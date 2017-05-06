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

global deck #balicek kariet, global aby sme ho mohli volat aj vo funkciach
deck = list()

#Petove vypocty
card_id1 = 0
card_id2 = 2
i = 1
g = 55
p = g
z = 0
def dvadva():
   cisla = [1, 1, 2, 2] #Vytvoril som list so 4 cislami - pre kazdu kartu jedno cislo
   random.shuffle(cisla) #tento "command" zamiesa cisla v liste
   if cisla[0] == 1: #tuto sa vlastne porovnava hodnota
      color1 = "orange"
      id1 = 1
   else:
      color1 = "green"
      id1 = 2
   if cisla[1] == 1:
      color2 = "orange"
      id2 = 1
   else:
      color2 = "green"
      id2 = 2
   if cisla[2] == 1:
      color3 = "orange"
      id3 = 1
   else:
      color3 = "green"
      id3 = 2
   if cisla[3] == 1:
      color4 = "orange"
      id4 = 1
   else:
      color4 = "green"
      id4 = 2
   nn = y / 3
   yy = x / 2.5
   canvas.create_rectangle(yy, nn, yy + 60, nn + 90, fill=color1)
   canvas.create_rectangle(yy + 95, nn, yy + 60 + 95, nn + 90, fill=color2)
   canvas.create_rectangle(yy, nn + 125, yy + 60, nn + 90 + 125, fill=color3)
   canvas.create_rectangle(yy + 95, nn + 125, yy + 60 + 95, nn + 90 + 125, fill=color4)
   canvas.pack()
   c1 = Card(id1, yy, nn, yy + 60, nn + 90, canvas)#vytvorime a nastavime parametre karty
   c2 = Card(id2, yy + 95, nn, yy + 60 + 95, nn + 90, canvas)
   c3 = Card(id3, yy, nn + 125, yy + 60, nn + 90 + 125, canvas)
   c4 = Card(id4, yy + 95, nn + 125, yy + 60 + 95, nn + 90 + 125, canvas)
   canvas.tag_bind(c1.back, '<ButtonPress-1>', onObjectClick) #prepojime funkciu so zadnou stranou karty
   canvas.tag_bind(c2.back, '<ButtonPress-1>', onObjectClick)
   canvas.tag_bind(c3.back, '<ButtonPress-1>', onObjectClick)
   canvas.tag_bind(c4.back, '<ButtonPress-1>', onObjectClick)
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

krat = 1

#funkcia volana po kliknuti na kartu
def onObjectClick(event):
    clicked_card = canvas.delete(event.widget.find_closest(event.x, event.y)) #zistime na chrbat ktorej karty bolo kliknute
    global krat
    global card_id1
    global card_id2
    if krat == 1:
       card_id1 = card.id #premenna card neexistuje, to je trieda
       #existuje premenna clicked_card, ktora vsak neobsahuje id karty
       #na ktoru bolo kliknute, ale chrbat karty, na ktoru bolo kliknute
       #preto ak sa pozries na moj fork, tak zistis,
       #ze ja som to riesil tak, ze som si vsetky vytvorene karty hodil
       #do zoznamu deck (balicek) a ked mi pouzivatel klikol na kartu
       #tak som chrbty kariet v balicku porovnaval s clicked_card
       #ak sa chrbty rovnaju, tak si danu kartu das napr. do card1
       #ked druhy krat klikne, tak spravis to iste a das ju do card2
       #potom porovnas if card1.id == card2.id
       krat = 2
    else:
       card_id2 = card.id
       krat = 1
       if card_id1 == card_id2:
          print("zhoda!")
       else:
          print("Nezhoda!")
   
canvas.pack()
#ciselnik pridavame do okna, moze sa hybat v rozsahu hodnot 0 az 300 a zmena jeho hodnoty vola funkciu myFunc
spin = Spinbox(root, from_ = 0, to = 300, command=myFunc)
#pridanie ciselniku
spin.pack()

root.mainloop()
