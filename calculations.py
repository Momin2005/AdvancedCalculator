import math
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

    def split2(self, inpuT, placeOpp, lenopp):
        output = ""
        for i in range(int(placeOpp) + 1 + lenopp, len(inpuT)):
            output += str(inpuT[i])

        return output

    def calculate(self, inpuT):
        calc = False
        output = 0
        opperators = ["s", "^", "V", "*", "/", "-", "+"]
        for opp in range(0, len(opperators)):
            for place in range(0, len(str(inpuT))):

                if str(inpuT[place]) == opperators[opp]:
                    calc = True

                    split_1 = str(self.calculate(self.split1(inpuT, place)))
                    split_2 = str(self.calculate(self.split2(inpuT, place, 0)))
                    split_gon = str(self.calculate(self.split2(inpuT, place, 2)))
                    print(f"split1 {split_1} split2 {split_2} splitgon {split_gon}")

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

                    elif opperators[opp] == "^":
                        output = float(split_1) ** float(split_2)
                        print(f"calculate(power) place({place})")

                    elif opperators[opp] == "V":
                        output = math.sqrt(float(split_2))
                        print(f"calculate(V) place({place})")

                    elif opperators[opp] == "s":
                        output = math.sin(float(split_gon))
                        print(f"calculate(sin) place({place})")

        if not calc:
            output = inpuT

        # print(f"return {output}")
        return output

