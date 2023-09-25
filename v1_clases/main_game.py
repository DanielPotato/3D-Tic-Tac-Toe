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


p1 , p2 = propmt_players()


board=Board()


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
   
            



isWin=False

while not isWin :
    player_turn(p1)
    winner=board.check_win()
    if winner == "X":
         print(f"{p1.name} is the winner !!! ")    
         isWin=True
    if not isWin :     
        player_turn(p2)
        winner=board.check_win()
        if winner == "O": 
            print(f"{p2.name} is the winner !!! ")    
            isWin=True


#board.displayBoard()

