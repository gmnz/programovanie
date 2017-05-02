from tkinter import * #hviezdicka znamena, ze pridaj VSETKO z kniznice tkinter
from tkinter import messagebox #toto treba pre časť menu info - vyskakovacie okno 
import ctypes #kniznice na zistenie rozmerov okna, momentlane nevyuzita

#pridanie vlastnej triedy do programu
from classes.card import Card #importovanie triedy Card

#Petove podokienko
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
#pridanie menu do okna
root.config(menu=menubar)

#Petove vypocty
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

#funkcia volana Spinboxom
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

global deck #balicek kariet, global aby sme ho mohli volat aj vo funkciach

#funkcia volana po kliknuti na kartu
def onObjectClick(event):
    clicked_card = event.widget.find_closest(event.x, event.y)[0] #zistime na chrbat ktorej karty bolo kliknute
    for card in deck: #prejdeme kartami v balicku
        if card.back == clicked_card: #ak chrbat karty v balicku == chrbtu kliknutej karty
            print(card.id) #id karty, ktora bude zmazana
            deck.remove(card) #zmaz kartu z balicku
            canvas.delete(card.back) #zmaz kartu z platna

#priklad pouzitia novovytvorenej triedy Card
deck = list() #z balicku robim zoznam
c1 = Card(0, 50, 50, 100, 100, canvas) #vytvorime a nastavime parametre karty
canvas.tag_bind(c1.back, '<ButtonPress-1>', onObjectClick) #prepojime funkciu so zadnou stranou karty
deck.append(c1) #pridanie karty na koniec balicku
c2 = Card(1, 110, 50, 160, 100, canvas) #vytvorime a nastavime parametre karty
canvas.tag_bind(c2.back, '<ButtonPress-1>', onObjectClick) #prepojime funkciu so zadnou stranou karty
deck.append(c2) #pridanie karty na koniec balicku

#pridanie platna do okna
canvas.pack() 

#ciselnik pridavame do okna, moze sa hybat v rozsahu hodnot 0 az 300 a zmena jeho hodnoty vola funkciu myFunc
spin = Spinbox(root, from_ = 0, to = 300, command=myFunc)
#pridanie ciselniku
spin.pack()

root.mainloop() #cykli okno, teda nechaj ho otvorene
