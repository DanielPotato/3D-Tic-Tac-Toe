import os

os.system("clear")

class Board:
    layer_number = 0
    
    def __init__(self):

        self.cells=[" ", " ", " "," ", " ", " "," ", " ", " "]
        Board.layer_number+=1
    def display(self):
        print(f"Layer  {self.layer_number}")
        print("###########")
        print(f"{self.cells[0]} | {self.cells[1]} | {self.cells[2]}")
        print("----------")
        print(f"{self.cells[3]} | {self.cells[4]} | {self.cells[5]}")
        print("----------")
        print(f"{self.cells[6]} | {self.cells[7]} | {self.cells[8]}")
        print("##########")



    def Prompt_move(self):
        '''
        this function returns tow variables 
        first variable will be layer number 
        second variable will be square numbe (we return square-1 )
        '''

        valid = False
        while valid == False:
            layer = input("Choose layer number 1-3: ")
            if layer.isdigit() and 1 <= int(layer) <= 3:
                valid = True
            else:
                print("Invalid input")
        valid = False
        while valid == False:
            square = input("Choose Square number 1-9: ")
            if square.isdigit() and 1 <= int(square) <= 9:
                valid = True
            else:
                print("Invalid input")

        return int(layer) , (int(square)-1) 

board = Board()
layer , square = board.Prompt_move()
print(layer,square)

##TODO: todo: check 




board.display()


