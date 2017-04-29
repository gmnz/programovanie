class Card:
    def __init__(self, id, x, y, xx, yy, canvas):
        self.id = id
        canvas.create_rectangle(x, y, xx, yy, fill='blue')
