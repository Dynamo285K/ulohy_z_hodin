import tkinter as tk
from datetime import datetime

win = tk.Tk()
canvas = tk.Canvas(win, width=800, height=800,bg='white')
canvas.pack()

class Line:
    def __init__(self,point:tuple,dx,dy, color, canvas):
        self.coords = point
        self.dx = dx
        self.dy = dy
        self.color = color
        self.canvas = canvas
        self.id = canvas.create_rectangle(point[0],point[1],point[0]+dx,point[1]+dy, fill =color, outline='')

    def on(self):
        self.canvas.itemconfig(self.id, fill=self.color)



    def off(self):
        self.canvas.itemconfig(self.id, fill='white')



class Segment:
    def __init__(self,point:tuple,dx,dy,small:int,big:int,color:str,canvas):
        self.parts = []
        self.coords = point
        self.color = color
        sx = point[0]
        sy = point[1]
        self.parts.append(Line((sx+small, sy), big, small, color, canvas))
        self.parts.append(Line((sx + small+big, sy+small), small, big, color, canvas))
        self.parts.append(Line((sx + small, sy+big+small), big, small, color, canvas))
        self.parts.append(Line((sx, sy + small), small, big, color, canvas))
        self.parts.append(Line((sx + small + big, sy + big+small+small), small, big, color, canvas))
        self.parts.append(Line((sx + small, sy+big+big+small+small), big, small, color, canvas))
        self.parts.append(Line((sx , sy + big + small + small), small, big, color, canvas))

    def reset(self):
        for part in self.parts:
            part.off()

    def error(self):
        for part in self.parts:
            part.on()

    def display(self,number:int):
        if number == 0:
            self.error()
            self.parts[2].off()
        elif number == 1:
            self.reset()
            self.parts[1].on()
            self.parts[4].on()
        elif number == 2:
            self.error()
            self.parts[3].off()
            self.parts[4].off()
        elif number == 3:
            self.error()
            self.parts[3].off()
            self.parts[6].off()
        elif number == 4:
            self.error()
            self.parts[0].off()
            self.parts[5].off()
            self.parts[6].off()
        elif number == 5:
            self.error()
            self.parts[1].off()
            self.parts[6].off()
        elif number == 6:
            self.error()
            self.parts[1].off()
        elif number == 7:
            self.reset()
            self.parts[0].on()
            self.parts[1].on()
            self.parts[4].on()
        elif number == 8:
            self.error()
        elif number == 9:
            self.error()
            self.parts[6].off()

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
splitted = current_time.split(':')
print(splitted)
listik = []
for i in splitted:
    listik.append(int(i))
print(listik)



class Hodziny:#konstruktor 6 segmentov
              #metoda on - zobrat systemovy cas, rozbit ho na cislice(hodiny na dve), prva cislica - hodin do 1ho seg...6tu do 6
    pass







skuska = Segment((100,100),20,100, 20,100,'turquoise', canvas)
skuska.display(1)




win.mainloop()
