import os

os.system("clear")

class Board:
    #layer_number = 0
    
    def __init__(self):

        self.cells=[" ", " ", " "," ", " ", " "," ", " ", " "]
        #Board.layer_number+=1
    def display(self):

        #print(f"Layer  {self.layer_number}")
        print("###########")
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("----------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("----------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")
        print("##########")








##TODO: create a new function that checks for a win condition , and a function that checks move cordinates is empty 




