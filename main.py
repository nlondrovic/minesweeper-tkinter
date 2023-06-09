from tkinter import *
from config import *

root = Tk()
from Cell import Cell
root.geometry(f"{ROOT_WIDTH}x{ROOT_HEIGHT}")
root.title("Minesweeper - Nikola Londrovic")
root.resizable = False

top_frame = Frame(root, bg="#cecece", width=TOP_FRAME_WIDTH, height=TOP_FRAME_HEIGHT)
top_frame.place(x=0, y=0)
game_frame = Frame(root, width=GAME_FRAME_WIDTH, height=GAME_FRAME_HEIGHT)
game_frame.place(x=0, y=TOP_FRAME_HEIGHT)

image_smiley = PhotoImage(file="images/smiley.png")
game_btn = Button(root, image=image_smiley, width=CELL_SIZE, height=CELL_SIZE)
game_btn.place(x=TOP_FRAME_WIDTH / 2 - CELL_SIZE / 2, y=2)

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        c = Cell(x, y)
        c.set_cell_button(game_frame)
        c.cell_btn.grid(row=y, column=x)

Cell.randomize_mines()

root.mainloop()
