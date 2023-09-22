import random as rd
def create_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("")


def display_board(board):
    create_board(board)
    create_board(board)
    create_board(board)


def choose_player():
    user1 = input("Player 1, please enter your name: ")
    user2 = input("Player 2, please enter your name: ")
    players = [user1, user2]
    first_player = rd.choice(players)
    if first_player == user1:
        second_player = user2
    else:
        second_player = user1
    return first_player, second_player

def playerInput():
    inp = int(input(f"{first_player} Please enter the board"))



board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


display_board(board)
choose_player()