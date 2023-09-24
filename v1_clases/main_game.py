import random
import os
from player import Player
from board import Board


def is_square_empty(boards: object, layer: object, square: object, player: object):
    while boards[layer].cells[square] != " ":
        print("square is not empty, please select another square")
        layer = player.select_layer()
        square = player.select_square()


def check_win(boards):
    #TODO check win_combinations span on multiple boards
    win_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]  # Diagonals
    ]
    # check win_combinations in every single board
    for layer in range(3):
        for combination in win_combinations:
            if boards[layer].cells[combination[0]-1] == boards[layer].cells[combination[1]-1] == boards[layer].cells[combination[2]-1] == 'X':
                return True
    return False


# input("enter your name")
player1 = Player()
player1.set_name(input("enter your name"))
p1_name = player1.get_name()
print(p1_name)

player2 = Player()
player2.set_name(input("enter your name"))
p2_name = player2.get_name()
print(p2_name)

is_win = False
boards = []
for i in range(0, 3):
    board = Board()
    board.display()
    boards.append(board)

while not is_win:
    print("player1 please enter your move: ")
    layer = player1.select_layer()
    square = player1.select_square()
    # check if square is empty
    is_square_empty(boards, layer, square, player1)
    boards[layer].cells[square] = "X"

    for board in boards:
        board.display()

    is_win = check_win(boards)

    print("player2 please enter your move: ")
    layer = player2.select_layer()
    square = player2.select_square()
    # check if square is empty
    is_square_empty(boards, layer, square, player2)
    boards[layer].cells[square] = "O"

    for board in boards:
        board.display()

    is_win = check_win(boards)
