from tkinter import *
from tkinter import ttk
from functools import partial


class Board:
    def __init__(self, X):
        self.root = Tk()
        self.boardState = X

    def get_data(self, stars):
        self.boardState = stars

    def update(self):
        pass

    def set(self, column, row):
        temp = self.boardState
        print(self.boardState)
        temp[row, column] = (temp[row, column] + 1) % 3
        print(temp)
        return temp

    def show(self):
        frm = ttk.Frame(self.root, padding=10)
        frm.grid()
        pixel = PhotoImage(width=1, height=1)
        for rows in range(len(self.boardState)):
            for cols in range(len(self.boardState[rows])):
                setValue = partial(self.set, cols, rows)
                Button(frm, text="", image=pixel, height=20, width=20, compound="c", command=setValue).grid(column=cols, row=rows)
        self.root.mainloop()


