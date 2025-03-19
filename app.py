from tkinter import *
from random import randint

root = Tk()
root.title("Rulla tärning.")

textBox = Label(root, text="")
textBox.pack()

def show():
    roll = randint(1, 6)
    textBox.config(text=roll)





show_button = Button(root, text="Visa saker", width=50, command=show)
show_button.pack()
button = Button(root, text="Quit program", width=500, command=root.destroy)
button.pack()

root.mainloop()
