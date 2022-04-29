from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
import tkinter as tk
from copy import deepcopy
# globals
img_x = 100
img_y = 100
board = []
curr_figure = None
buff = [9, 9]

turn = "white"
# global end

"""switchs the turn"""




def switch_turn():
    global turn
    if (turn == "white"):
        turn = "black"
    else:
        turn = "white"

        """takes a board and a color as input and return True if that color is in check in that board"""
def in_check(color, tempBoard):

    x,y = find_king(color, tempBoard)
    return is_field_attacked(color, tempBoard, x,y)

def is_field_attacked(color, tempBoard, x,y):
    if color == "white":
        oponant_color = "black"
    else:
        oponant_color = "white"

    for line in tempBoard:
        for fig in line:
            if isinstance(fig, Figure):
                if fig.color == oponant_color:
                    if(fig.check_move_possible(x,y, tempBoard)):
                        return True

    return False


def find_king(color, tmp_board):
    for line in tmp_board:
        for fig in line:
            if isinstance(fig, King) and fig.color == color:
                return fig.x, fig.y

def printBoard(board):
    for line in board:
        print(line)

def move(xy1):
    global turn
    global buff
    global board

    board_temp = copy_of_board(board)
    if (buff != [9, 9] and buff != xy1):  # check if buff is not empty and not equal to new input

        buffFig = board_temp[buff[0]][buff[1]]  # retrive object from buffer position
        if (isinstance(buffFig, Figure)):  # check that object that is to me moved is a Figure
            if (buffFig.check_move_possible(xy1[0], xy1[1], board_temp)):  # check that the move is possible using the pieces internal check move possible function
                # set buff figs internal cordinates to the new position it is being moved to

                buffFig.x = xy1[0]
                buffFig.y = xy1[1]

                board_temp[xy1[0]][xy1[1]] = buffFig  # write buffFig over newFig in global board array
                board_temp[buff[0]][buff[1]] = EmptyFig(buff[0],
                                                   buff[1])  # create new emptyFig and place where buff fig used to be
                  # refresh moved item
                board_temp[xy1[0]][xy1[1]].refresh()


                if not in_check(turn,board_temp):
                    # Figur wird gezogen:
                    curr_figure = buffFig
                    board = board_temp
                    switch_turn()
                    show(board[buff[0]][buff[1]])
                    show(board[xy1[0]][xy1[1]])
                    buff = [9, 9]  # reset buffer
                    printBoard(board)
                else:
                    print(turn, " is in check after this move, so it is not possible")
                    buff = [9,9]
        buff = [9,9]






    elif(buff == xy1):  # reset buffer if click same objet twice
        buff = [9, 9]
    elif (isinstance(board[xy1[0]][xy1[1]], Figure)):
        if (board[xy1[0]][xy1[1]].color == turn):  # write new input into buffer if click on own color
            buff = xy1
        else:
            buff = [9, 9]  # reset buffer if click on oponant first
    else:
        buff = [9, 9]  # safty catch



def copy_of_board(b):
    return decompress_board(compress_board(b))

def compress_board(b):
    compressed_b = []
    for line in b:
        l = []
        for fig in line:
            l.append(fig.compress())
        compressed_b.append(l)
    return compressed_b


def decompress_board(b_compressed):
    decompresed_b = []
    for line in b_compressed:
        l = []
        for compressed_fig in line:
            l.append(decompress(compressed_fig))
        decompresed_b.append(l)
    return decompresed_b


def decompress(compressed_fig):
    fig_class = compressed_fig[0]
    if fig_class == EmptyFig:
        return EmptyFig(compressed_fig[1], compressed_fig[2])
    return fig_class(compressed_fig[1],compressed_fig[2], compressed_fig[3])





class Figure:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.refresh()

    def refresh(self):
        a = lambda: move([self.x, self.y])

        if (self.color == "black"):
            img = self.img_black
        else:
            img = self.img_white

        self.pic = tk.Button(frame, image=img, width=img_x, height=img_y, command=a)

    def check_move_possible(self, target_x, target_y, board):
        return False


    def compress(self):
        return [deepcopy(type(self)), deepcopy(self.x), deepcopy(self.y),deepcopy(self.color)]



class EmptyFig():
    def __init__(self, x, y):
        # self.pic = Label(frame, image=img_white, width=img_x, height=img_y)
        self.x = x
        self.y = y
        self.color = "Empty"
        self.refresh()

    def __int__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = "Empty"
        self.refresh()

    def refresh(self):
        a = lambda: move([self.x, self.y])
        self.pic = tk.Button(frame, image=img_white, width=img_x, height=img_y, command=a)

    def compress(self):
        return [type(self), self.x, self.y, self.color]

    def __repr__(self):
        return "empty "


class Queen(Figure):
    def __init__(self, x, y, color):
        self.img_black = img_queen_black
        self.img_white = img_queen_white

        super(Queen, self).__init__(x, y, color)

    def __repr__(self):
        return "Queen "

    def check_move_possible(self, target_x, target_y, board):
        if (target_x < 0 or target_x > 7 or target_y < 0 or target_y > 7):
            return False
        target_fig = board[target_x][target_y]
        if (target_x == self.x and target_y != self.y):
            if (self.y - target_y > 0):
                incr = -1
            else:
                incr = 1
            for y in range(self.y + incr, target_y, incr):
                if (isinstance(board[self.x][y], Figure)):
                    return False
            if (not isinstance(target_fig, Figure)):
                return True
            elif (self.color == target_fig.color):
                return False

            board[target_x][target_y] = EmptyFig(target_x, target_y)
            return True
        if (target_x != self.x and target_y == self.y):
            if (self.x - target_x > 0):
                incr = -1
            else:
                incr = 1
            for x in range(self.x + incr, target_x, incr):
                if (isinstance(board[x][self.y], Figure)):
                    return False
            if (not isinstance(target_fig, Figure)):
                return True
            elif (self.color == target_fig.color):
                return False

            board[target_x][target_y] = EmptyFig(target_x, target_y)
            return True
        if (self.color == board[target_x][target_y].color):
            return False
        if (abs(self.x - target_x) == abs(self.y - target_y)):

            if (self.x > target_x):
                if (self.y > target_y):
                    toX = range(self.x - 1, target_x, -1)
                    toY = range(self.y - 1, target_y, -1)

                if (self.y < target_y):
                    toX = range(self.x - 1, target_x, -1)
                    toY = range(self.y + 1, target_y, 1)
            if (self.x < target_x):
                if (self.y > target_y):
                    toX = range(self.x + 1, target_x, 1)
                    toY = range(self.y - 1, target_y, -1)

                if (self.y < target_y):
                    toX = range(self.x + 1, target_x, 1)
                    toY = range(self.y + 1, target_y, 1)

            for xy in range(0, abs(self.x - target_x) - 1):
                print(xy)
                print(toX[xy], toY[xy])
                if (isinstance(board[toX[xy]][toY[xy]], Figure)):
                    return False
            return True
        return False


class King(Figure):
    def __init__(self, x, y, color):
        self.img_black = img_king_black
        self.img_white = img_king_white
        super(King, self).__init__(x, y, color)

    def __repr__(self):
        return " King "

    def check_move_possible(self, target_x, target_y, board):

        return (abs(self.x-target_x)<=1 and abs(self.y-target_y)<=1 and not (self.x == target_x and self.y ==target_y) and self.color != board[target_x][target_y].color)


class Bishop(Figure):
    def __init__(self, x, y, color):
        self.img_black = img_bishop_black
        self.img_white = img_bishop_white
        super(Bishop, self).__init__(x, y, color)

        # self.pic = Label(frame, image=img_horse, width=img_x, height=img_y)

    def __repr__(self):
        return "Bishop"

    def check_move_possible(self, target_x, target_y, board):

        if (self.color == board[target_x][target_y].color):
            return False
        if (abs(self.x - target_x) == abs(self.y - target_y)):

            if (self.x > target_x):
                if (self.y > target_y):
                    toX = range(self.x - 1, target_x, -1)
                    toY = range(self.y - 1, target_y, -1)

                if (self.y < target_y):
                    toX = range(self.x - 1, target_x, -1)
                    toY = range(self.y + 1, target_y, 1)
            if (self.x < target_x):
                if (self.y > target_y):
                    toX = range(self.x + 1, target_x, 1)
                    toY = range(self.y - 1, target_y, -1)

                if (self.y < target_y):
                    toX = range(self.x + 1, target_x, 1)
                    toY = range(self.y + 1, target_y, 1)

            for xy in range(0, abs(self.x - target_x) - 1):
                print(xy)
                print(toX[xy], toY[xy])
                if (isinstance(board[toX[xy]][toY[xy]], Figure)):
                    return False
            return True


class Rook(Figure):
    def __init__(self, x, y, color):
        self.img_white = img_rook_white
        self.img_black = img_rook_black
        super(Rook, self).__init__(x, y, color)

    def __repr__(self):
        return " Rook "

    def check_move_possible(self, target_x, target_y, board):

        if (target_x < 0 or target_x > 7 or target_y < 0 or target_y > 7):
            return False
        target_fig = board[target_x][target_y]
        if (target_x == self.x and target_y != self.y):
            if (self.y - target_y > 0):
                incr = -1
            else:
                incr = 1
            for y in range(self.y + incr, target_y, incr):
                if (isinstance(board[self.x][y], Figure)):
                    return False
            if (not isinstance(target_fig, Figure)):
                return True
            elif (self.color == target_fig.color):
                return False

            board[target_x][target_y] = EmptyFig(target_x, target_y)
            return True

        if (target_x != self.x and target_y == self.y):
            if (self.x - target_x > 0):
                incr = -1
            else:
                incr = 1
            for x in range(self.x + incr, target_x, incr):
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
    def __init__(self, x, y, color):
        self.img_black = img_horse_black
        self.img_white = img_horse_white
        super(Horse, self).__init__(x, y, color)

    def __repr__(self):
        return "Horse"

    def check_move_possible(self, target_x, target_y, board):

        if ((abs(self.x - target_x) == 1 and abs(self.y - target_y) == 2) or (
                abs(self.x - target_x) == 2 and abs(self.y - target_y) == 1)):
            if (self.color != board[target_x][target_y].color):
                return True
            return False
        return False

    def __repr__(self):
        return "HORSE"


class Pawn(Figure):
    def __init__(self, x, y, color):
        # self.pic = Label(frame, image=img_white, width=img_x, height=img_y)
        self.img_white = img_pawn_white
        self.img_black = img_pawn_black
        self.firstMove = True
        super(Pawn, self).__init__(x, y, color)

    def __repr__(self):
        return " Pawn "

    #Prueft ob Bauer zu Dame wird:
    def refresh(self):
        if(self.color=="white" and self.x==0):
            fig = Queen(self.x, self.y, "white")
            board[self.x][self.y] = fig
            show(fig)
        elif(self.color=="black" and self.x==7):
            fig = Queen(self.x, self.y, "black")
            board[self.x][self.y] = fig
            show(fig)
        else:
            super(Pawn, self).refresh()


    def check_move_possible(self, target_x, target_y, board):

        if (board[target_x][target_y].color == self.color):
            return False

        if (target_x < 0 or target_x > 7 or target_y < 0 or target_y > 7):
            return False
        if (target_y == self.y):

            if (target_x == self.x - 1 and self.color == "white"):
                if (isinstance(board[target_x][target_y], Figure)):
                    return False
                return True

            if (target_x == self.x + 1 and self.color == "black"):
                if (isinstance(board[target_x][target_y], Figure)):
                    return False
                return True

        if ((self.color=="white" and self.x == 6) or (self.color=="black" and self.x == 1)):

            if (target_y == self.y):

                if (target_x == self.x - 2 and self.color == "white" and not isinstance(board[self.x - 1][self.y],
                                                                                        Figure)):
                    if (isinstance(board[target_x][target_y], Figure)):
                        return False
                    return True

                if (target_x == self.x + 2 and self.color == "black" and not isinstance(board[self.x + 1][self.y],
                                                                                        Figure)):
                    if (isinstance(board[target_x][target_y], Figure)):
                        return False
                    return True

        if (self.color == "white"):
            if (((self.y + 1 == target_y and self.x - 1 == target_x) or (
                    self.y - 1 == target_y and self.x - 1 == target_x)) and isinstance(board[target_x][target_y],
                                                                                       Figure)):
                return True
        if (self.color == "black"):
            if (((self.y - 1 == target_y and self.x + 1 == target_x) or (
                    self.y + 1 == target_y and self.x + 1 == target_x)) and isinstance(board[target_x][target_y],
                                                                                       Figure)):
                return True
        #Check en-passent:
        if(isinstance(curr_figure, Pawn)):
            #fuer weiss:
            if(self.color=="white" and self.x==3 and curr_figure.x==3 and abs(self.y-curr_figure.y)==1 and target_x==2 and target_y==curr_figure.y):
                return True
            if(self.color=="black" and self.x==6 and curr_figure.x==6 and abs(self.y-curr_figure.y)==1 and target_x==5 and target_y==curr_figure.y):
                return True
        return False


def show(fig):
    #i = 0
    fig.pic.grid(row=fig.x +1, column=fig.y +1)


def showAll(board):
    i =0
    for line in board:
        i += 1
        j = 0
        for fig in line:
            j += 1
            # fig.refresh()
            fig.pic.grid(row=i, column=j)

def loadImg(img):
    img_horse_white = (Image.open(img))
    img_horse_white = img_horse_white.resize((img_x, img_y), Image.ANTIALIAS)
    img_horse_black = ImageOps.invert(img_horse_white)
    img_horse_white = ImageTk.PhotoImage(img_horse_white)
    img_horse_black = ImageTk.PhotoImage(img_horse_black)
    return img_horse_white, img_horse_black


if __name__ == '__main__':

    root = Tk()
    # content = ttk.Frame(root)
    frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=800, height=800)
    # button_frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=800, height=800)
    # content.grid(column=1, row=1)
    frame.grid(column=0, row=0, columnspan=8, rowspan=8)
    # button_frame.grid(column=0, row=0, columnspan=8, rowspan=8)

    # image loading
    img_horse_white, img_horse_black = loadImg("horse_w.jpg")

    img_white = (Image.open("white.jpg"))
    img_white = img_white.resize((img_x, img_y), Image.ANTIALIAS)
    img_white = ImageTk.PhotoImage(img_white)

    img_pawn_white, img_pawn_black = loadImg("pawn_w.jpg")

    img_rook_white, img_rook_black = loadImg("rook_w.jpg")
    img_bishop_white = (Image.open("bishop_w.jpg"))

    img_bishop_white, img_bishop_black = loadImg("bishop_w.jpg")

    img_queen_white, img_queen_black = loadImg("queen_w.jpg")
    img_king_white, img_king_black = loadImg("king_w.jpg")
    # board = [[None] * 8]*8

    for x in range(0, 8):
        line = []
        for y in range(0, 8):
            if x in [6]:
                fig = Pawn(x, y, "white")
            elif x in [1]:
                fig = Pawn(x, y, "black")
            elif x in [7]:
                if y in [1, 6]:
                    fig = Horse(x, y, "white")
                elif y in [2, 5]:
                    fig = Bishop(x, y, "white")
                elif y in [3]:
                    fig = Queen(x, y, "white")
                elif y == 4:
                    fig = King(x, y, "white")
                else:
                    fig = Rook(x, y, "white")
            elif x in [0]:
                if y in [1, 6]:
                    fig = Horse(x, y, "black")
                elif y in [2, 5]:
                    fig = Bishop(x, y, "black")
                elif y in [3]:
                    fig = Queen(x, y, "black")
                elif y == 4:
                    fig = King(x, y, "black")
                else:

                    fig = Rook(x, y, "black")


            else:

                fig = EmptyFig(x, y)

            line.append(fig)

        board.append(line)


    showAll(board)

    root.mainloop()
