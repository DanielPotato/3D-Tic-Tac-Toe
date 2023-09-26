import random
import os
from player import Player
from board import Board


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


def prompt_player():
    name=input("Enter your name : ")
    p1=Player()
    p1.set_name(name)
    p1.set_x_o("X")
    return p1


# def coomputer_turn(self):
    
#     for l in range(self.layer):
#     # Check if any row in this layer has the same symbol in all cells

#         for r in range(self.row):
#             if self.squares[l][r][0] == "X" and self.squares[l][r][1] == "X" : 
#                 board.set_squares(l+1,r+1,3,"O")
#                 return
#             elif self.squares[l][r][1] == "X" and self.squares[l][r][2] == "X" :
#                 board.set_squares(l,r,0,"O")
#                 return
#             elif self.squares[l][r][0] == "X" and self.squares[l][r][2] == "X" :
#                 board.set_squares(l,r,1,"O")
#                 return
              

#         for c in range(self.col):
#             if self.squares[l][0][c] == "X" and self.squares[l][1][c] == "X" : 
#                 board.set_squares(l,2,c,"O")
#                 return
#             elif self.squares[l][1][c] == "X" and self.squares[l][2][c] == "X" :
#                 board.set_squares(l,0,c,"O")
#                 return
#             elif self.squares[l][0][c] == "X" and self.squares[l][2][c] == "X" :
#                 board.set_squares(l,1,c,"O")
#                 return    
                
                
#         if self.squares[l][0][0] == "X" and self.squares[l][1][1] == "X" : 
#             board.set_squares(l,2,2,"O")
#             return
#         elif self.squares[l][1][1] == "X" and self.squares[l][2][2] == "X" :
#             board.set_squares(l,0,0,"O")
#             return
#         elif self.squares[l][0][0] == "X" and self.squares[l][2][2] == "X" :
#             board.set_squares(l,1,1,"O")
#             return   

#         if self.squares[l][0][2] == "X" and self.squares[l][1][1] == "X" : 
#             board.set_squares(l,2,0,"O")
#             return
#         elif self.squares[l][1][1] == "X" and self.squares[l][2][0] == "X" :
#             board.set_squares(l,0,2,"O")
#             return
#         elif self.squares[l][0][2] == "X" and self.squares[l][2][0] == "X" :
#             board.set_squares(l,1,1,"O")
#             return   

# ####################################################################
#     # Check rows and columns across layers
#     for r in range(self.row):
#         for c in range(self.col):
#             if self.squares[0][r][c] == "X" and self.squares[1][r][c] == "X" : 
#                 board.set_squares(2,r,c,"O")
#                 return
#             elif self.squares[1][r][c] == "X" and self.squares[2][r][c] == "X" :
#                 board.set_squares(0,r,c,"O")
#                 return
#             elif self.squares[0][r][c] == "X" and self.squares[2][r][c] == "X" :
#                 board.set_squares(1,r,c,"O")
#                 return   
                
                

#     #  Check diagonals across layers
#     if self.squares[0][0][0] == "X" and self.squares[1][1][1] == "X" : 
#         board.set_squares(2,2,2,"O")
#         return
#     elif self.squares[1][1][1] == "X" and self.squares[2][2][2] == "X" :
#         board.set_squares(0,0,0,"O")
#         return
#     elif self.squares[0][0][0] == "X" and self.squares[2][2][2] == "X" :
#         board.set_squares(1,1,1,"O")
#         return   
    
#     if self.squares[0][0][2] == "X" and self.squares[1][1][1] == "X" : 
#         board.set_squares(2,2,0,"O")
#         return
#     elif self.squares[1][1][1] == "X" and self.squares[2][2][0] == "X" :
#         board.set_squares(0,0,2,"O")
#         return
#     elif self.squares[0][0][2] == "X" and self.squares[2][2][0] == "X" :
#         board.set_squares(1,1,1,"O")
#         return  
        
         
#     layer_num=random.randint(1,3)
#     row_num=random.randint(1,3)
#     col_num=random.randint(1,3)
#     board.set_squares(layer_num,row_num,col_num,"O") 




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
   
            

def play_game():

    isWin=False
    while not isWin :
        player_turn(p1)
        winner=board.check_win()
        if winner == "X":
            print(f"{p1.name} is the winner !!! ") 
            p1.counter += 1   
            isWin=True
        if not isWin :     
            player_turn(p2)
            winner=board.check_win()
            if winner == "O": 
                print(f"{p2.name} is the winner !!! ")   
                p2.counter += 1   
 
                isWin=True



#user_choise=input("choose wither you want to play against 1(CP) or 2(human) ")
play_again="y"
while play_again == "y":    
    #if user_choise == "1":

        board=Board()
    #     p1=prompt_player()
    #     isWinp1=False
    #     while not isWinp1 :
    #         player_turn(p1)
    #         winner=board.check_win()
    #         if winner == "X":
    #             print(f"{p1.name} is the winner !!! ") 
    #             p1.counter += 1   
    #             isWinp1=True
    #         if not isWinp1 :
                
    #             coomputer_turn(board)
    #             winner=board.check_win()
    #             if winner == "O":
    #                 print("You Lost")

    # else:    
        p1 , p2 = propmt_players()
        play_game()
        
        
    
    
    
        play_again = input("Do you want to play again? (y/n)").lower()
    

        print("Score :")
        print(f"{p1.name} : {p1.counter}") 
        print(f"{p2.name} : {p2.counter} ")








