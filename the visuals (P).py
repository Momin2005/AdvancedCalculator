from settings import *


def input_disp(number, disp):
    backup = disp.get()
    disp.delete(0, END)
    disp.insert(0, backup, number)
    return disp


def entry():        # if you use this def, then you need to equal it to the variable "disp" like in line 23
    disp = Entry(win, columnspan=1)
    disp.grid(row=0, column=0)
    return disp


def init_numeric_buttons():
    button1 = Button(win, text="1", command=lambda:input_disp(1, disp))
    button1.grid(row=0, column=3)
    return button1


disp = entry()