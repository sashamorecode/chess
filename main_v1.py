
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter as tk




img_x = 100
img_y = 100
def makeBoard():
    img = (Image.open("h.jpg"))
    img = img.resize((img_x, img_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    for x in range(0, 7):
        for y in range(0, 7):
            emptyLable = Label(frame, image=img, width=img_x, height=img_y)
            emptyLable.grid(row=x, column=y, sticky=tk.NW)


    """
    imgw = (Image.open("white.jpg"))
    imgw = imgw.resize((img_x, img_y), Image.ANTIALIAS)
    imgw = ImageTk.PhotoImage(imgw)

    img = (Image.open("h.jpg"))
    img = img.resize((img_x, img_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    emptyLable = Label(frame, image=img, width=img_x, height=img_y)
    emptyLable.grid(row=1, column=1, sticky=tk.NW)

    for x in range(0,7):
        for y in range(0,7):
            emptyLable = Label(frame, image=img, width=img_x, height=img_y)
            emptyLable.grid(row=x, column=y, sticky=tk.NW)
    """





if __name__ == '__main__':


    root = Tk()
    content = ttk.Frame(root)
    frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=800, height=800)

    content.grid(column=1, row=1)
    frame.grid(column=0, row=0, columnspan=8, rowspan=8)

    #create Board
    img = (Image.open("h.jpg"))
    img = img.resize((img_x, img_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imgw = (Image.open("white.jpg"))
    imgw = imgw.resize((img_x, img_y), Image.ANTIALIAS)
    imgw = ImageTk.PhotoImage(imgw)


    board = [[]]
    for x in range(0, 8):
        for y in range(0, 8):

            if x in [0,1,6,7]:
                fig = Label(frame, image=img, width=img_x, height=img_y)
                board[x][y] = fig
                fig.grid(row=x, column=y, sticky=tk.NW)

            else:
                board[x][y] = fig
                emptyLable = Label(frame, image=imgw, width=img_x, height=img_y)
                emptyLable.grid(row=x, column=y, sticky=tk.NW)

                print(emptyLable.getint())


    """
    img= (Image.open("h.jpg"))
    img = img.resize((img_x, img_y), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    


    lable = Label(frame, image=img, width=img_x, height=img_y)
    lable.grid(row=0, column=0, sticky=tk.NW)
    label1 =  Label(frame, image=img, width=img_x, height=img_y)
    emptyLable = Label(frame,image=imgw, width=img_x, height=img_y)
    emptyLable.grid(row=0, column=1, sticky=tk.NW)
    label1.grid(row=0, column=2, sticky=tk.NW)
    """
    root.mainloop()



def move(label1, label2):
    label1


"""
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")


frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)
"""


class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Horse(Figure):
    def __init__(self):
        img = (Image.open("h.jpg"))
        img = img.resize((img_x, img_y), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        pic = Label(frame, image=img, width=img_x, height=img_y)
