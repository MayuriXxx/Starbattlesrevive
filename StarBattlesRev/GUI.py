from tkinter import *
from tkinter import ttk
from functools import partial


class Board:
    def __init__(self, state, stars, islands):
        self.root = Tk()
        self.boardState = state
        self.fields = islands
        self.solution = stars
        self.colors = ["red", "blue", "yellow", "green"]

    def get_data(self, state, islands, stars):
        self.boardState = state

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
                set_value = partial(self.set, cols, rows)
                text = int(self.solution[rows][cols])
                Button(frm, text=text, image=pixel, height=20, width=20,
                       compound="c", command=set_value,
                       bg=self.colors[int(self.fields[rows][cols])])\
                    .grid(column=cols, row=rows)
        self.root.mainloop()


