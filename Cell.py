from tkinter import Button, PhotoImage
from config import *
import random


class Cell:
    all = []
    img0 = PhotoImage(file="images/num0.png")
    img1 = PhotoImage(file="images/num1.png")
    img2 = PhotoImage(file="images/num2.png")
    img3 = PhotoImage(file="images/num3.png")
    img4 = PhotoImage(file="images/num4.png")
    img5 = PhotoImage(file="images/num5.png")
    img6 = PhotoImage(file="images/num6.png")
    img7 = PhotoImage(file="images/num7.png")
    img8 = PhotoImage(file="images/num8.png")
    imgflag = PhotoImage(file="images/flag.png")
    imgmine = PhotoImage(file="images/mine.png")
    bg_images = [img0, img1, img2, img3, img4, img5, img6, img7, img8]

    def __init__(self, x, y):
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.cell_btn = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    @property
    def neighbor_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def neighbor_mine_count(self):
        counter = 0
        for cell in self.neighbor_cells:
            if cell.mine:
                counter += 1

        return counter

    def set_cell_button(self, location):
        btn = Button(location, image=self.img0)
        self.cell_btn = btn

        btn.bind("<Button-1>", self.btn_left_click)
        btn.bind("<Button-3>", self.btn_right_click)

    def btn_left_click(self, event):
        global STARTED
        global OVER

        if self.revealed:
            return

        if self.flagged:
            return

        if OVER:
            return

        if not STARTED:
            STARTED = True
            if self.mine:
                self.mine = False

        if self.mine:
            self.show_mines()
        else:
            self.reveal_cell()

    def reveal_cell(self):
        if self.revealed:
            return

        self.revealed = True
        self.cell_btn.configure(
            image=self.bg_images[self.neighbor_mine_count],
            bg="#ececec",
            text=self.neighbor_mine_count)

        if (self.neighbor_mine_count == 0):
            self.flood_fill()

    def show_mines(self):
        global OVER
        OVER = True

        for cell in Cell.all:
            if cell.mine:
                cell.cell_btn.configure(image=self.imgmine, bg="#ececec")
                cell.revealed = True

    def btn_right_click(self, event):
        global OVER

        if OVER:
            return

        if self.revealed:
            return

        if self.flagged:
            self.cell_btn.configure(image=self.img0)
            self.flagged = False
        else:
            self.cell_btn.configure(image=self.imgflag)
            self.flagged = True

    def flood_fill(self):
        for cell in self.neighbor_cells:
            cell.reveal_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def randomize_mines():
        mine_cells = random.sample(Cell.all, MINE_COUNT)

        for mine_cell in mine_cells:
            mine_cell.mine = True
