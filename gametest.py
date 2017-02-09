from Tkinter import *
import math
import random

root = Tk()


class Hex:
    """Returns a hexagon generator for hexagons of the specified size."""
    def __init__(self, num, terrain):

        self.roll_num = num
        self.terrain = terrain

        if terrain == 'field':
            self.color = '#ffcc66' 
        elif terrain == 'forest':
            self.color = '#009933'
        elif terrain == 'pasture':
            self.color = '#ccff66'
        elif terrain == 'mountains':
            self.color = '#808080'
        elif terrain == 'hills':
            self.color = '#cc6600'
        elif terrain == 'desert':
            self.color = '#ffffcc'
    def setCoords(self, coords):
        self.coords = coords
        
    

      
def generate_hex(edge_length, offset):
    """Generator for coordinates in a hexagon."""
    coords = []
    x, y = offset
    coords.append([x,y])
    for angle in range(0, 360, 60):
        x += round(math.cos(math.radians(angle)) * edge_length,1)
        y += round(math.sin(math.radians(angle)) * edge_length,1)
        coords.append([x,y])
        
    coords.append([offset])
    return coords

def drawboard(canvas, tiles):
    length = 50
    orig_x = 200
    orig_y = 200
    xspace = 75
    yspace = 45
    vspace = 88
    x = orig_x
    y = orig_y
    i = 0
    for h in tiles:
        coords = generate_hex(length,(x,y))
        color = 'red'
        #name = h.roll_num
        canvas.create_polygon(coords, fill = h.color,outline='black',stipple='gray75',activeoutline='red',activewidth=3)

        i += 1
        if i < 3 or (i > 3 and i <7) or (i>7 and i< 12) or (i>12 and i<16) or (i>16 and i<20):
            x += 0
            y += vspace
        elif i == 3:
            x = orig_x + xspace
            y = orig_y -yspace
        elif i == 7:
            x = orig_x + 2*xspace
            y = orig_y - 2*yspace
        elif i == 12:
            x = orig_x + 3*xspace
            y = orig_y -yspace
        elif i == 16:
            x = orig_x + 4*xspace
            y = orig_y

def makenewboard():
    random.seed()
    board = []
    for i in range(19):
        terr = ['field','forest','pasture','mountains','hills','desert']
        terrain = random.choice(terr)
        tile = Hex(i,terrain)
        board.append(tile)

    return board

def randomboard(canvas):
    canvas.delete("all")
    drawboard(canvas,makenewboard())
    return 



w = Canvas(root, width=800, height=800)
menubar = Menu(root)
menubar.add_command(label="new board", command=lambda: randomboard(w))
menubar.add_command(label="quit",command=lambda: root.destroy())
root.config(menu=menubar)
w.pack()


def click(event):
    if w.find_withtag(CURRENT):
        ids = w.find_withtag(CURRENT)
        w.itemconfig(CURRENT, width = 10)
        w.update_idletasks()
        w.after(200)
        w.itemconfig(CURRENT,width = 1)
        fill = w.itemcget(ids, "fill")
    #    if fill = '#ffcc66':
    #        terrain = 'field'
    #    elif fill = 
    #  self.stipple = 'gray25'
    #elif terrain == 'forest':
    #  self.color = '#009933'
    #  self.stipple = 'gray50'
    #elif terrain == 'pasture':
    #  self.color = '#ccff66'
    #  self.stipple = 'gray25'
    #elif terrain == 'mountains':
    #  self.color = '#808080'
    #  self.stipple = 'gray75'
    #elif terrain == 'hills':
    #  self.color = '#cc6600'
    #  self.stipple = 'gray25'
    #elif terrain == 'desert':
    #  self.color = '#ffffcc'
    #  self.stipple = 'gray12'

w.bind("<Button-1>", click)



mainloop()

