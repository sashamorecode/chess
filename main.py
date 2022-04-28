
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps

import tkinter as tk
img_x = 100
img_y = 100


buff = [9,9]







def move(xy1):




    global buff
    print(xy1)
    print("x: ", board[xy1[0]][xy1[1]].x, "y: ", board[xy1[0]][xy1[1]].y)
    if(buff != [9,9] and buff != xy1):


        buffFig = board[buff[0]][buff[1]]
        if(isinstance(buffFig, Figure)):
            if(buffFig.check_move_possible(xy1[0], xy1[1])):
                buffFig.x = xy1[0]
                buffFig.y = xy1[1]
                board[xy1[0]][xy1[1]] = buffFig
                board[buff[0]][buff[1]] = EmptyFig(buff[0], buff[1])





        buff = [9,9]



        show(board)

    elif(buff == xy1):
        buff = [9,9]
    elif(isinstance(board[xy1[0]][xy1[1]],Figure)):
        buff = xy1
    else:
        buff = [9,9]

    for line in board:
        print(line)

class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y






class EmptyFig():
    def __init__(self,x,y):
        #self.pic = Label(frame, image=img_white, width=img_x, height=img_y)
        self.x = x
        self.y = y
        self.color = "Empty"
        a = lambda: move([self.x, self.y])
        self.pic = tk.Button(frame, image=img_white, width = img_x, height = img_y, command = a)

    def __repr__(self):
        return "empty"
class Rook(Figure):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

        # self.pic = Label(frame, image=img_horse, width=img_x, height=img_y)
        a = lambda: move([self.x, self.y])

        if (self.color == "black"):
            img = img_horse_black
        else:
            img = img_horse_white

        self.pic = tk.Button(frame, image=img, width=img_x, height=img_y, command=a)

    def check_move_possible(self, target_x, target_y):

        if (target_x < 0 or target_x > 7 or target_y < 0 or target_y > 7):
            return False
        target_fig = board[target_x][target_y]
        if(target_x == self.x and target_y != self.y):
            for y in range(self.y + 1, target_y):
                if(isinstance(board[self.x][y], Figure)):
                    return False
            if(not isinstance(target_fig, Figure)):
                return True
            elif(self.color == target_fig.color):
                return False

            board[target_x][target_y] = EmptyFig(target_x,target_y)
            return True

        if (target_x != self.x and target_y == self.y):
            for x in range(self.x + 1, target_x):
                if (isinstance(board[x][self.y], Figure)):
                    return False
            if (not isinstance(target_fig, Figure)):
                return True
            elif (self.color == target_fig.color):
                return False

            board[target_x][target_y] = EmptyFig(target_x, target_y)
            return True

        return False
class Horse(Figure):
    def __init__(self,x,y, color):
        self.x = x
        self.y = y
        self.color = color

        #self.pic = Label(frame, image=img_horse, width=img_x, height=img_y)
        a = lambda: move([self.x,self.y])

        if (self.color == "black"):
            img = img_horse_black
        else:
            img = img_horse_white

        self.pic = tk.Button(frame, image=img, width=img_x, height=img_y, command = a)
    def check_move_possible(self, target_x, target_y):
        return True
        if(abs(self.x - target_x) == 1):
            return True
        return False

    def __repr__(self):
        return "HORSE"

class Pawn(Figure):
    def __init__(self, x, y, color):
        # self.pic = Label(frame, image=img_white, width=img_x, height=img_y)
        self.color = color
        self.x = x
        self.y = y
        self.firstMove = True
        a = lambda: move([self.x, self.y])
        if (self.color == "black"):
            img = img_pawn_black
        else:
            img = img_pawn_white


        self.pic = tk.Button(frame, image=img, width=img_x, height=img_y, command=a)

    def check_move_possible(self, target_x, target_y):
        if(target_x < 0 or target_x > 7 or target_y < 0 or target_y > 7):
            return False



        if(target_y == self.y):

            if (target_x == self.x - 1 and self.color == "white"):
                if (isinstance(board[target_x][target_y], Figure)):
                    return False
                return True

            if(target_x == self.x + 1 and self.color == "black"):
                if (isinstance(board[target_x][target_y], Figure)):
                    return False
                return True

        if(self.firstMove):
            if (target_y == self.y):

                if (target_x == self.x - 2 and self.color == "white"):
                    if (isinstance(board[target_x][target_y], Figure)):
                        return False
                    return True

                if (target_x == self.x + 2 and self.color == "black"):
                    if (isinstance(board[target_x][target_y], Figure)):
                        return False
                    return True

        if(self.color == "white"):
            if(self.y -1 == target_y and self.x-1 == target_x and isinstance(board[target_x][target_y], Figure)):
                return True
        if (self.color == "black"):
            if (self.x + 1 == target_x and self.y + 1 == target_y and isinstance(board[target_x][target_y], Figure)):
                return True
        return False

def show(board):

    i =0
    j =0

    for line in board:
        i +=1
        j = 0
        for fig in line:
            j +=1

            fig.pic.grid(row=i, column=j)

if __name__ == '__main__':

    root = Tk()
    #content = ttk.Frame(root)
    frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=800, height=800)
    #button_frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=800, height=800)
    #content.grid(column=1, row=1)
    frame.grid(column=0, row=0, columnspan=8, rowspan=8)
    #button_frame.grid(column=0, row=0, columnspan=8, rowspan=8)


    # image loading
    img_horse_white = (Image.open("horse_w.jpg"))
    img_horse_white = img_horse_white.resize((img_x, img_y), Image.ANTIALIAS)
    img_horse_black = ImageOps.invert(img_horse_white)
    img_horse_white = ImageTk.PhotoImage(img_horse_white)
    img_horse_black = ImageTk.PhotoImage(img_horse_black)


    img_white = (Image.open("white.jpg"))
    img_white = img_white.resize((img_x, img_y), Image.ANTIALIAS)
    img_white = ImageTk.PhotoImage(img_white)

    img_pawn_white = (Image.open("pawn_w.jpg"))
    img_pawn_white = img_pawn_white.resize((img_x, img_y), Image.ANTIALIAS)
    img_pawn_black = ImageOps.invert(img_pawn_white)
    img_pawn_white = ImageTk.PhotoImage(img_pawn_white)
    img_pawn_black = ImageTk.PhotoImage(img_pawn_black)



    #board = [[None] * 8]*8
    board = []

    for x in range(0, 8):
        line = []
        for y in range(0, 8):
            if x in [6]:
                fig = Horse(x,y, "white")
            elif x in [1]:
                fig = Horse(x,y, "black")
            elif x in [7]:
                fig = Horse(x,y, "white")
            elif x in [0]:
                fig = Horse(x,y,"black")


            else:

                fig = EmptyFig(x,y)

            line.append(fig)

        board.append(line)


    show(board)

    root.mainloop()
