from tkinter import *
import configure
import new
from unit import Cell


root = Tk()
root.config(bg="black")
root.geometry(f"{configure.WIDTH}x{configure.HEIGHT}")
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(root, bg="#5D6D7E",
                  width=configure.WIDTH, 
                  height=new.height_prct(25))

top_frame.place(x=0,y=0)


game_title = Label(top_frame, bg="#5D6D7E", fg="white", text="Minesweeper Game",
                   font=('', 48))

game_title.place(x=new.width_prct(30), y=0)


# board
center_frame = Frame(root, bg="white", width=new.width_prct(75), height=new.height_prct(75))
center_frame.place(relx=0.5, rely=0.5, anchor=CENTER)



for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x, y)
        c.cell_btn_object = c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)



# Create the label object
Cell.cell_count_label_object = Label(top_frame, text=f"Cells Left: {Cell.cell_count}")

# Place the label in the top frame
Cell.cell_count_label_object.place(x=new.width_prct(42), y=new.height_prct(15))



Cell.randomize_mines()

root.mainloop()