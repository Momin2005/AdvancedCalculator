from parameters import *
from tkinter import *
from visuals import *


class calculation:
    def __init__(self, vis_self):
        print(vis_self.disp.get())
        answert = self.calculate(vis_self.disp.get())
        vis_self.disp.delete(0, END)
        vis_self.disp.insert(0, answert)



    def split1(self, inpuT, placeOpp):
        output = ""
        for i in range(0, placeOpp):
            output += str(inpuT[i])

        return output

    def split2(self, inpuT, placeOpp):
        output = ""
        for i in range(int(placeOpp) + 1, len(inpuT)):
            output += str(inpuT[i])

        return output

    def calculate(self, inpuT):
        calc = False
        output = 0
        opperators = ["*", "/", "-", "+"]
        for opp in range(0, len(opperators)):
            for place in range(0, len(str(inpuT))):

                if str(inpuT[place]) == opperators[opp]:
                    calc = True

                    split_1 = float(self.calculate(self.split1(inpuT, place)))
                    split_2 = float(self.calculate(self.split2(inpuT, place)))
                    print(f"split1 {split_1} split2 {split_2}")

                    if opperators[opp] == "*":

                        output = float(split_1) * float(split_2)
                        print(f"calculate(*) place({place})")

                    elif opperators[opp] == "/":

                        output = float(split_1) / float(split_2)
                        print(f"calculate(/) place({place})")

                    elif opperators[opp] == "-":

                        output = float(split_1) - float(split_2)
                        print(f"calculate(-) place({place})")

                    elif opperators[opp] == "+":

                        output = float(split_1) + float(split_2)
                        print(f"calculate(+) place({place})")

        if not calc:
            output = inpuT

        print(f"return {output}")
        return output

