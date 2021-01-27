from settings import *

class visual_setup:
    def __init__(self):
        self.font = '("new courier", 20)'
        self.squire = 5
        self.entry()

    def input_disp(self, number, disp):
        backup = disp.get()
        disp.delete(0, END)
        disp.insert(0, backup, number)
        return disp

    def entry(self):
        disp = Entry(win, columnspan=1)
        disp.grid(row=0, column=0)
        return disp

    def init_numeric_buttons(self):
        button1 = Button(win, text="1", font=self.font, width=self.squire, padx=self.squire, pady=self.squire,
                         command=lambda :input_disp(1, disp))
        button1.grid(row=0, column=3)

