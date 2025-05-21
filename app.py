from tkinter import *
from random import randint

root = Tk()
root.title("Rulla tärningen")

textBox = Label(root, text="Random Number Generator!")
textBox.place(x=100)



def show():
    roll = randint(0, 101)
    textBox.config(text=roll, width=60, background="#003560", fg="#000000")


show_button = Button(root, text="Positive Number!", width=60, height=20, command=show, background="#34A2FE")
show_button.grid(row=0, column=0)

def show():
    roll = randint(-100, 0)
    textBox.config(text=roll, width=60, background="#003560", fg="#34A2FE")

show_button = Button(root, text="Negative Number!", width=60, height=20, command=show, background="#34A2FE")
show_button.grid(row=0, column=1)



button = Button(root, text="Quit program", width=60, command=root.destroy, background="#003560", fg="#34A2FE")
button.place(x=240, y=396)

root.mainloop()