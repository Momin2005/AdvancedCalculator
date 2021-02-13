from calculations import *
from tkinter import *

class visual_setup:
    def __init__(self, setting_self):
        print("__init__")
        self.Button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "clear", "delete", "+", "-", "*", "/", "enter"]
        self.num_on_butt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.font = ("new courier", 10)
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
        self.disp.grid(row=0, column=0, columnspan=4)
        self.all_buttons()
        return self.disp

    # al buttons stuff

    # Button settings
    def all_buttons(self):
        print("make_numeric_buttons")

        self.make_nummeric_button(0, 4, 0)
        self.make_nummeric_button(1, 3, 0)
        self.make_nummeric_button(2, 3, 1)
        self.make_nummeric_button(3, 3, 2)
        self.make_nummeric_button(4, 2, 0)
        self.make_nummeric_button(5, 2, 1)
        self.make_nummeric_button(6, 2, 2)
        self.make_nummeric_button(7, 1, 0)
        self.make_nummeric_button(8, 1, 1)
        self.make_nummeric_button(9, 1, 2)
        print("make_other_buttons")
        self.clear_button()

        self.opperator_buttons()
        self.enter("=", 5, 5)

    def opperator_buttons(self):
        print("make_operator_buttons")
        self.make_operator(12, "+", 1, 5)
        self.make_operator(13, "-", 2, 5)
        self.make_operator(14, "*", 3, 5)
        self.make_operator(15, "/", 4, 5)



    # button makers
    def make_nummeric_button(self, text, x, y):
        print(f"butt_made:{text}")
        self.Button[self.num_made] = Button(self.settings_self.win, text=text, font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda :self.input_disp(text))

        self.Button[self.num_made].grid(row=x, column=y)
        self.num_made += 1

    def clear_button(self):
        print(f"butt_made:clear")
        self.Button[10] = Button(self.settings_self.win, text="clear", font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda: self.clear())

        self.Button[10].grid(row=4, column=1)

        print(f"butt_made:delete")
        self.Button[11] = Button(self.settings_self.win, text="<=", font=self.font,
            width=self.squire, padx=self.squire, pady=self.squire, command=lambda: self.delete())

        self.Button[11].grid(row=4, column=2)

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




