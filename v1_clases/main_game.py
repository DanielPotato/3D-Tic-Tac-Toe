import random
import os
from player import Player
from board import Board

#input("enter your name")

player1=Player()
player1.set_name(input("enter your name")) 
p1_name=player1.get_name()
print(p1_name  )

player2=Player()
player2.set_name(input("enter your name")) 
p2_name=player2.get_name()
print(p2_name  )


board1=Board()
board2=Board()
board3=Board()
board1.display()
board2.display()
board3.display()


layer=player1.select_layer()
square = player1.select_square()
cells_list=[board1.cells,board2.cells,board3.cells]

cells_list[layer][square]="O"

os.system("clear")



board1.display()

board2.display()

board3.display()
