import random
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

# players=(p1.get_players)
# c=randome.chose()
board=Board()
board.display()
board1=Board()
board1.display()
board2=Board()
board2.display()