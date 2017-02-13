from Tkinter import *
import math
import random

root = Tk()


class Hex:
    """Returns a hexagon generator for hexagons of the specified size."""
    def __init__(self, num, terrain, name):

        self.roll_num = num
        self.terrain = terrain
        self.name = name

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

    canvas.delete(all)
    length = 50
    orig_x = 250
    orig_y = 200
    xspace = length*1.5+.5
    yspace = length*0.866+.5
    vspace = yspace*2+1
    x = orig_x
    y = orig_y
    i = 0

    canvas.create_polygon([425,30,685,180,685,480,425,630,165,480,165,180], fill = 'cyan',stipple = 'gray50', width = 0)
    for h in tiles:
        coords = generate_hex(length,(x,y))
        color = 'red'
        canvas.create_polygon(coords,fill = 'white', width = 0)
        canvas.create_polygon(coords, tag=h.name ,fill = h.color,outline=h.color,stipple='gray75',activeoutline='red',activewidth=3)
        if h.name != 'desert':
            textcolor = 'black'
            if h.roll_num == 6 or h.roll_num == 8:
                textcolor = 'red'
            canvas.create_oval(x+10,y+29,x+40,y+59,fill = 'white', outline = 'white')
            canvas.create_text(x+25,y+44,text = str(h.roll_num),fill = textcolor)
        if h.name == 'desert':
            canvas.create_oval(x+12,y+31,x+38,y+57,fill = 'grey', stipple = 'gray75', outline = 'gray')

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

def conflicts(board):
    #for 0 neighbors =                      i+1 i+3 i+4
    #for 1 neighbors =                  i-1 i+1 i+3 i+4
    #for 2 neighbors =                  i-1     i+3 i+4
    #for 3 neighbors =              i-3     i+1     i+4 i+5
    #for 4 neighbors =          i-4 i-3 i-1 i+1     i+4 i+5
    #for 5 neighbors =          i-4 i-3 i-1 i+1     i+4 i+5
    #for 6 neighbors =          i-4     i-1         i+4 i+5
    #for 7 neighbors =          i-4         i+1         i+5
    #for 8 neighbors =      i-5 i-4     i-1 i+1     i+4 i+5
    #for 9 neighbors =      i-5 i-4     i-1 i+1     i+4 i+5
    #for 10 neighbors =     i-5 i-4     i-1 i+1     i+4 i+5
    #for 11 neighbors =     i-5         i-1         i+4
    #for 12 neighbors =     i-5 i-4         i+1     i+4
    #for 13 neighbors =     i-5 i-4     i-1 i+1 i+3 i+4
    #for 14 neighbors =     i-5 i-4     i-1 i+1 i+3 i+4
    #for 15 neighbors =     i-5 i-4     i-1     i+3
    #for 16 neighbors =         i-4 i-3     i+1
    #for 17 neighbors =         i-4 i-3 i-1 i+1
    #for 18 neighbors =         i-4 i-3 i-1     

    reds = []
    conflict = 0
    for i in range(len(board)):
        if board[i].roll_num == 6 or board[i].roll_num == 8:
            reds.append(i)
    
    for i in range (len(reds)):
        if reds[i]+1 in reds or reds[i]+3 in reds or reds[i]+4 in reds or reds[i]+5 in reds:
            conflict +=1
    
    return conflict


def makenewboard():
    ''' 
           __
        __/  \__
     __/  \_7/  \__
    /  \_3/  \12/  \
    \_0/  \_8/  \16/
    /  \_4/  \13/  \
    \_1/  \_9/  \17/
    /  \_5/  \14/  \
    \_2/  \10/  \18/
       \_6/  \15/ 
          \11/ 
    '''


    random.seed()
    board = []
    nums = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
    random.shuffle(nums)
    i = 0
    for j in range(4):
        terrain = 'field'
        name = 'field'+str(j)
        tile = Hex(nums[i],terrain,name)
        board.append(tile)

        terrain = 'pasture'
        name = 'pasture'+str(j)
        tile = Hex(nums[i+1],terrain,name)
        board.append(tile)

        terrain = 'forest'
        name = 'forest'+str(j)
        tile = Hex(nums[i+2],terrain,name)
        board.append(tile)
        i += 3

    for k in range(3):
        terrain = 'mountains'
        name = 'mountains'+str(k)
        tile = Hex(nums[i],terrain,name)
        board.append(tile)

        terrain = 'hills'
        name = 'hills'+str(k)
        tile = Hex(nums[i+1],terrain,name)
        board.append(tile)
        i+=2
     
    terrain = 'desert'
    name = 'desert'
    tile = Hex(7,terrain,name)
    board.append(tile)
    random.shuffle(board)

    while (conflicts(board)):
        random.shuffle(board)

    return board


def shuffleboard(board):
    while (conflicts(board)):
        random.shuffle(board)


w = Canvas(root, width=800, height=800)
menubar = Menu(root)
hexlist = makenewboard()
menubar.add_command(label="shuffle board",command = lambda: shuffleboard(hexlist))
menubar.add_command(label="draw board", command=lambda: drawboard(w,hexlist))
menubar.add_command(label="quit",command=lambda: root.destroy())
root.config(menu=menubar)
w.pack()


def click(event):
    if w.find_withtag(CURRENT):
        ids = w.find_withtag(CURRENT)
        w.itemconfig(CURRENT, width = 4)
        w.update_idletasks()
        w.after(200)
        w.itemconfig(CURRENT,width = 1)
        tags = w.itemcget(ids,'tag')
        name = tags.split(' ')[0]
        currhex = filter(lambda x: x.name == name, hexlist)
        if len(currhex) > 0:
            print(currhex[0].name)
            print(currhex[0].roll_num)


w.bind("<Button-1>", click)



mainloop()

