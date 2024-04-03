from tkinter import *
import random
import new, configure
import ctypes
import sys

class Cell:
    all =[]
    cell_count = configure.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y ,is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_opened = False 
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        Cell.all.append(self)




    def create_btn_object(self, location):
        btn = Button(location,
                    width=12,
                    height=4,)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions) 

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.sorrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
                    self.show_cell()

                    if Cell.cell_count == configure.MINES_COUNT:
                      ctypes.WinDLL.user32.MessageBoxW(0, "Congratulations! Tou won", "Game Over", 0)  
                      self.cell_btn_object.unbind("<Button-1>")
                      self.cell_btn_object.unbind("<Button-3>")


    def show_mine(self):
        self.cell_btn_object.configure(bg="red" )
        ctypes.windll.user32.messageBoxW(0, "You clickedon a mine", "Play Again", 0)
        sys.exit()


    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y ),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def sorrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.sorrounded_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left{Cell.cell_count}")
            self.cell_btn_object.configure(bg="white")
            self.is_opened = True

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="white")
            self.is_mine_candidate = False


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, configure.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return (f"Cell{self.x}, {self.y}")
