from tkinter import *

# test

win = Tk()

class Setup:
     def __init__(self):
          self.title = "Calculator"
          self.bgColor = "#323232"
          self.geo = "640x480"

          self.setup()
     
     def setup(self):
          self.start()

     def start(self):
          win.title(self.title)
          win.config(bg = self.bgColor)
          win.geometry(self.geo)
          win.maxsize(640, 480)
          win.minsize(640, 480)
          self.run()

     def run(self):
          win.mainloop()
