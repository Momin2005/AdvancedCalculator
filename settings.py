from tkinter import *
from visuals import *

class Setup:
     def __init__(self):
          self.title = "Calculator"
          self.bgColor = "#323232"      # can you set in this comment witch color this is.
          self.geo = "640x480"
          self.win = Tk()

          self.setup()
     
     def setup(self):
          self.start()


     def start(self):
          self.win.title(self.title)
          self.win.config(bg = self.bgColor)
          self.win.geometry(self.geo)
          self.win.maxsize(640, 480)
          self.win.minsize(640, 480)
          visual_setup(self)
          self.run()

     def run(self):
          self.win.mainloop()
