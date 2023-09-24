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
boards=[board1,board2,board3]

board1.cells[0]="O"
s=board1.is_empty_cell(1)
print(s)
board1.display()


for board in boards: board.display()