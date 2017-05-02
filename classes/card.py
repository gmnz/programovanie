class Card: #vlastna trieda, ktora ma nejake vlastnosti

    def __init__(self, id, x, y, xx, yy, canvas): #tato procedura sa spusti, ked je vytvoreny novy objekt triedy Card 
        self.id = id #priradenie id karte, rovnake karty budu mat rovnake id
        self.back = canvas.create_rectangle(x, y, xx, yy, fill='blue') #vytvorenie zadnej strany karty
    def turnAround(canvas): #funkcia pre otocenie karty, zatial ju to len zmaze, lebo pod obdlznikom nic neni
       canvas.delete(back) 
        
