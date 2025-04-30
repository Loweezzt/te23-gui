from tkinter import *
from random import randint

root = Tk()
root.title("Rulla tärningen")

textBox = Label(root, text="")
textBox.pack()

def show():
    roll = randint(1, 100)
    textBox.config(text=roll)

show_button = Button(root, text="RNG", width=60, height=20, command=show)
show_button.pack()
button = Button(root, text="Quit program", width=20, command=root.destroy)
button.pack()
root.mainloop()
