from calculations import *
from tkinter import *

class visual_setup:
    def __init__(self, setting_self):
        print("__init__")
        self.Button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "clear", "delete", "+", "-", "*", "/", "enter", "^"]
        self.num_on_butt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.font = ("courier new", 10)
        self.squire = 4
        self.num_made = 0
        self.settings_self = setting_self
        self.entry()

    def input_disp(self, number):
        print(f"input_number_{number}")
        backup = self.disp.get()
        self.disp.delete(0, END)
        self.disp.insert(0, f"{backup}{number}")
        return self.disp

    def entry(self):
        print("entry")
        self.disp = Entry(self.settings_self.win, font=self.font)
        self.disp.grid(row=0, column=0, columnspan=5, ipadx=38)
        self.all_buttons()
        return self.disp

    # al buttons stuff

    # Button settings
    def all_buttons(self):
        print("make_numeric_buttons")

        self.make_nummeric_button(0, 5, 0)
        self.make_nummeric_button(1, 4, 0)
        self.make_nummeric_button(2, 4, 1)
        self.make_nummeric_button(3, 4, 2)
        self.make_nummeric_button(4, 3, 0)
        self.make_nummeric_button(5, 3, 1)
        self.make_nummeric_button(6, 3, 2)
        self.make_nummeric_button(7, 2, 0)
        self.make_nummeric_button(8, 2, 1)
        self.make_nummeric_button(9, 2, 2)
        self.make_nummeric_button(".", 5, 2)
        print("make_other_buttons")
        self.clear_button(1, 2)

        self.opperator_buttons()
        self.enter("=", 5, 4)

    def opperator_buttons(self):
        print("make_operator_buttons")
        self.make_operator(12, "+", 2, 3)
        self.make_operator(13, "-", 3, 3)
        self.make_operator(14, "*", 4, 3)
        self.make_operator(15, "/", 5, 3)
        self.make_operator(16, "^", 1, 1)
        self.make_operator(17, "V", 1, 0)

    # button makers

    def make_nummeric_button(self, text, x, y):
        print(f"butt_made:{text}")
        self.Button[self.num_made] = Button(self.settings_self.win, text=text, font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda :self.input_disp(text))

        self.Button[self.num_made].grid(row=x, column=y)
        self.num_made += 1

    def clear_button(self, x, y):
        print(f"butt_made:clear")
        self.Button[10] = Button(self.settings_self.win, text="clear", font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda: self.clear())

        self.Button[10].grid(row=x, column=y)

        print(f"butt_made:delete")
        self.Button[11] = Button(self.settings_self.win, text="<=", font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda: self.delete())

        self.Button[11].grid(row=x, column=y + 1)

    def make_operator(self, matrix_place, text, x, y):
        print(f"butt_made:{text}")
        self.Button[matrix_place] = Button(self.settings_self.win, text=text, font=self.font,
                                 width=self.squire, padx=self.squire, pady=self.squire, command=lambda: self.input_disp(text))

        self.Button[matrix_place].grid(row=x, column=y)

    def enter(self, text, x, y):
        print(f"enter")
        self.Button[16] = Button(self.settings_self.win, text=text, font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda: calculation(self))

        self.Button[16].grid(row=x, column=y)


    # button reactions
    def clear(self):
        print("clear")
        self.disp.delete(0, END)

    def delete(self):
        print("delete")
        self.disp.delete(len(self.disp.get())-1, len(self.disp.get()))

