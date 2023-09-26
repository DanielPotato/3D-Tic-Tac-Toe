import random
import os
import sys



class Player: 

    
    def __init__(self):
   
        self.name = None
        self.x_o=None
        self.counter = 0
    def get_name(self):
        return self.name
      
    def set_name(self, x):
        self.name = x
    def get_x_o(self):
        return self.name
      
    def set_x_o(self, x):
        self.x_o = x

    def pick_number(self):
        while True:
            try:
                number = int(input(" enter a number 1-3: "))
                if 1 <= number <= 3:
                    return number
                else:
                    print(" Please choose a number between 1 and 3.")
            except ValueError:
                print(" Please enter a valid number ")

 


class Board :
    def __init__(self,layer=3,row=3,col=3):
        self.layer = layer
        self.row = row
        self.col = col
        self.squares=[[[" " for _ in range(self.col)] for _ in range(self.row)]for _ in range(self.layer)]

    def set_squares(self, layer, row, col, value):
        if (self.is_valid_indices(layer,row,col)
            and (value == "X" or value == "O" or value == " ")):
            
            self.squares[layer-1][row-1][col-1] = value
        else:
            print("Invalid input. Please provide valid layer, row, column, and value.")



    def displayBoard(self):
        #os.system("clear")
        for l in range(self.layer):
            print(f"Layer :{l+1}")
            for r in range(self.row):
                for c in range(self.col):
                    if c != self.col -1 :
                        print(self.squares[l][r][c]+"|",end="")
                    else:
                        print(self.squares[l][r][c])
                if r != self.row - 1:
                    print("-"*6)
                else:
                    print("_"*6)                        

    def displayLayer(self, layer):
        os.system("clear")
        print(f"Layer: {layer}")
        layer-=1
        #print(" 1 2 3")
        for r in range(self.row):
            print(f"{r+1}) ",end="")
            for c in range(self.col):
                if c != self.col -1 :
                    print(self.squares[layer][r][c]+"|",end="")
                else:
                    print(self.squares[layer][r][c])
            if r != self.row - 1:
                print("  "+"-"*7)
            else:
                print("  "+"_"*8)   

    def displayRow(self,layer,row):
        #os.system("clear")
        print("1 2 3")
        layer -=1
        row -=1
        for c in range(self.col):
            if c != self.col -1 :
                print(self.squares[layer][row][c]+"|",end="")
            else:
                print(self.squares[layer][row][c])        

    def is_valid_indices(self, layer, row, col):
        return (
            0 < layer <= self.layer
            and 0 < row <= self.row
            and 0 < col <= self.col
        )

    def is_square_empty(self, layer, row, col):
        if self.is_valid_indices(layer, row, col):
            return self.squares[layer-1][row-1][col-1] == " "
        else:
            #print("Please provide valid Input!")
            return False


    def check_win(self):
        for l in range(self.layer):
        # Check if any row in this layer has the same symbol in all cells

            for r in range(self.row):
                if (
                    self.squares[l][r][0] == self.squares[l][r][1] == self.squares[l][r][2]
                    and self.squares[l][r][0] != " "
                ):
                    return self.squares[l][r][0]
        # Check if any column in this layer has the same symbol in all cells

            for c in range(self.col):
                if (
                    self.squares[l][0][c] == self.squares[l][1][c] == self.squares[l][2][c]
                    and self.squares[l][0][c] != " "
                ):
                    return self.squares[l][0][c]
            #  Check diagonals in this layer
            if (
                self.squares[l][0][0] == self.squares[l][1][1] == self.squares[l][2][2]
                and self.squares[l][0][0] != " "
            ):
                return self.squares[l][0][0]
            if (
                self.squares[l][0][2] == self.squares[l][1][1] == self.squares[l][2][0]
                and self.squares[l][0][2] != " "
            ):
                return self.squares[l][0][2]
####################################################################
    # Check rows and columns across layers
        for r in range(self.row):
            for c in range(self.col):
                if (
                    self.squares[0][r][c] == self.squares[1][r][c] == self.squares[2][r][c]
                    and self.squares[0][r][c] != " "
                ):
                    return self.squares[0][r][c]
    #  Check diagonals across layers
        if (
            self.squares[0][0][0] == self.squares[1][1][1] == self.squares[2][2][2]
            and self.squares[0][0][0] != " "
        ):
            return self.squares[0][0][0]
        if (
            self.squares[0][0][2] == self.squares[1][1][1] == self.squares[2][2][0]
            and self.squares[0][0][2] != " "
        ):
            return self.squares[0][0][2]
    # If no winner yet and there are empty cells, the game is ongoing
        for l in range(self.layer):
            for r in range(self.row):
                for c in range(self.col):
                    if self.squares[l][r][c] == " ":
                        return " "

        return "C"
def prompt_player():
    name=input("Enter your name : ")
    p1=Player()
    p1.set_name(name)
    p1.set_x_o("X")
    return p1
def propmt_players():
    nameX=input("Enter first name : ")
    nameY=input("Enter second name : ")
    names_list = [nameX, nameY]
    first_name = random.choice(names_list)
    names_list.remove(first_name)
    second_name = names_list[0]
    p1= Player()
    p2= Player()
    p1.set_name(first_name)
    p1.set_x_o("X")

    p2.set_name(second_name)
    p2.set_x_o("O")
    return p1, p2



def computer_ai_turn(self):
    flag=0
    for l in range(self.layer):
    # Check if any row in this layer has the same symbol in all cells

        for r in range(self.row):
            if self.squares[l][r][0] == "X" and self.squares[l][r][1] == "X" : 
                board.set_squares(l+1,r+1,3,"O")
                return flag
            elif self.squares[l][r][1] == "X" and self.squares[l][r][2] == "X" :
                board.set_squares(l+1,r+1,1,"O")
                return flag
            elif self.squares[l][r][0] == "X" and self.squares[l][r][2] == "X" :
                board.set_squares(l+1,r+1,2,"O")
                return flag
              

        for c in range(self.col):
            if self.squares[l][0][c] == "X" and self.squares[l][1][c] == "X" : 
                board.set_squares(l+1,3,c+1,"O")
                return flag
            elif self.squares[l][1][c] == "X" and self.squares[l][2][c] == "X" :
                board.set_squares(l+1,1,c+1,"O")
                return flag
            elif self.squares[l][0][c] == "X" and self.squares[l][2][c] == "X" :
                board.set_squares(l+1,2,c+1,"O")
                return flag    
                
                
        if self.squares[l][0][0] == "X" and self.squares[l][1][1] == "X" : 
            board.set_squares(l+1,3,3,"O")
            return flag
        elif self.squares[l][1][1] == "X" and self.squares[l][2][2] == "X" :
            board.set_squares(l+1,1,1,"O")
            return flag
        elif self.squares[l][0][0] == "X" and self.squares[l][2][2] == "X" :
            board.set_squares(l+1,2,2,"O")
            return flag   

        if self.squares[l][0][2] == "X" and self.squares[l][1][1] == "X" : 
            board.set_squares(l+1,3,1,"O")
            return flag
        elif self.squares[l][1][1] == "X" and self.squares[l][2][0] == "X" :
            board.set_squares(l+1,1,3,"O")
            return flag
        elif self.squares[l][0][2] == "X" and self.squares[l][2][0] == "X" :
            board.set_squares(l+1,2,2,"O")
            return flag   

####################################################################
    # Check rows and columns across layers
    for r in range(self.row):
        for c in range(self.col):
            if self.squares[0][r][c] == "X" and self.squares[1][r][c] == "X" : 
                board.set_squares(3,r+1,c+1,"O")
                return flag
            elif self.squares[1][r][c] == "X" and self.squares[2][r][c] == "X" :
                board.set_squares(1,r+1,c+1,"O")
                return flag
            elif self.squares[0][r][c] == "X" and self.squares[2][r][c] == "X" :
                board.set_squares(2,r+1,c+1,"O")
                return flag   
                
                

    #  Check diagonals across layers
    if self.squares[0][0][0] == "X" and self.squares[1][1][1] == "X" : 
        board.set_squares(3,3,3,"O")
        return flag
    elif self.squares[1][1][1] == "X" and self.squares[2][2][2] == "X" :
        board.set_squares(1,1,1,"O")
        return flag
    elif self.squares[0][0][0] == "X" and self.squares[2][2][2] == "X" :
        board.set_squares(2,2,2,"O")
        return flag   
    
    if self.squares[0][0][2] == "X" and self.squares[1][1][1] == "X" : 
        board.set_squares(3,3,1,"O")
        return flag
    elif self.squares[1][1][1] == "X" and self.squares[2][2][0] == "X" :
        board.set_squares(1,1,3,"O")
        return flag
    elif self.squares[0][0][2] == "X" and self.squares[2][2][0] == "X" :
        board.set_squares(2,2,2,"O")
        return flag  

def computer_random_turn(self):
        while True:   
            layer_num=random.randint(1,3)
            row_num=random.randint(1,3)
            col_num=random.randint(1,3)
            #add validate empty    
            if board.is_square_empty(layer_num,row_num,col_num):
                board.set_squares(layer_num,row_num,col_num,"O") 
                return



def player_turn(player):
    isEmpty=False
   

    while not isEmpty:
        board.displayBoard()
        print(f"{player.name} it's your turn ")
        print("choose a Layer",end="")
        layer_num=player.pick_number()
        board.displayLayer(layer_num)

        print("choose a Row",end="")
        row_num=player.pick_number()

        board.displayRow(layer_num,row_num)
        print("choose a Column",end="")
        col_num=player.pick_number()


        isEmpty=board.is_square_empty(layer_num,row_num,col_num)

        if isEmpty :
            board.set_squares(layer_num,row_num,col_num,player.x_o)
            
        else:
            print("square is not empty ")
   

# def play_game():
#     user_choise=input("choose wither you want to play against 1(CP) or 2(human) ")
#     if user_choise == "1":
#         p1=prompt_player()
#         isWinp1=False
#         while not isWinp1 :
#             player_turn(p1)
#             winner=board.check_win()
#             if winner == "X":
#                 print(f"{p1.name} is the winner !!! ") 
#                 p1.counter += 1   
#                 isWinp1=True
#             if not isWinp1 :
                
#                 computer_turn(board)
#                 winner=board.check_win()
#                 if winner == "O":
#                     print("You Lost")
#     else:    
#         p1 , p2 = propmt_players()
#         isWin=False


#         while not isWin :
#             player_turn(p1)
#             winner=board.check_win()
#             if winner == "X":
#                 print(f"{p1.name} is the winner !!! ") 
#                 p1.counter += 1   
#                 isWin=True
#             if not isWin :     
#                 player_turn(p2)
#                 winner=board.check_win()
#                 if winner == "O": 
#                     print(f"{p2.name} is the winner !!! ")   
#                     p2.counter += 1   
    
#                     isWin=True



def play_game():
    user_choice = input("Choose whether you want to play against 1 (CP) or 2 (human): ")
    if user_choice == "1":
        p1 = prompt_player()
        is_win_p1 = False

        while not is_win_p1:
            player_turn(p1)
            winner = board.check_win()
            
            if winner == "X":
                print(f"{p1.name} is the winner !!! ")
                board.displayBoard()
                p1.counter += 1
                is_win_p1 = True
            elif winner == "C":
                print("It's a draw!")
                is_win_p1 = True
            if not is_win_p1:
            
                flag=computer_ai_turn(board)
                if flag == 0:
                    computer_random_turn(board)
                winner = board.check_win()
                if winner == "O":
                    print("You Lost")
                    is_win_p1 = True
    else:
        p1, p2 = propmt_players()
        is_win = False
        while not is_win:
            player_turn(p1)
            winner = board.check_win()
            if winner == "X":
                print(f"{p1.name} is the winner !!! ")
                p1.counter += 1
                is_win = True
            if not is_win:
                player_turn(p2)
                winner = board.check_win()
                if winner == "O":
                    print(f"{p2.name} is the winner !!! ")
                    p2.counter += 1



play_again = "y"

while play_again == "y":


    board=Board()

    play_game()

    play_again = input("Do you want to play again? (y/n)").lower()
    
    while play_again not in ['y', 'n']:
        print("Please enter y/n")
        play_again = input("Do you want to play again? (y/n)").lower()

        del board



        # print("Score :")
        # print(f"{p1.name} : {p1.counter}") 
        # print(f"{p2.name} : {p2.counter} ")




