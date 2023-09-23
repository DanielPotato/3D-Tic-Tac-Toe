import random
import os

def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0

    def get_name(self):
        return self.name

    def set_name(self, x):
        self.name = x

    def record_win(self):
        self.wins += 1

    def record_loss(self):
        self.losses += 1

    def get_score(self):
        return f"{self.name}: Wins - {self.wins}, Losses - {self.losses}"

class Board:
    def __init__(self):
        self.layers = [[" " for _ in range(9)] for _ in range(3)]
        self.current_layer = 0

    def display(self):
        for layer_number, layer in enumerate(self.layers, start=1):
            print(f"Layer {layer_number}")
            print("")
            print(f"{layer[0]} | {layer[1]} | {layer[2]}")
            print("----------")
            print(f"{layer[3]} | {layer[4]} | {layer[5]}")
            print("----------")
            print(f"{layer[6]} | {layer[7]} | {layer[8]}")
            print("")

    def is_empty(self, layer, square):
        return self.layers[layer][square] == " "

    def make_move(self, layer, square, symbol):
        if self.is_empty(layer, square):
            self.layers[layer][square] = symbol
            return True
        else:
            return False

    def check_win(self, layer, symbol):
        # Check rows, columns, and diagonals in the given layer
        for i in range(3):
            if all(self.layers[layer][i * 3 + j] == symbol for j in range(3)) or \
               all(self.layers[layer][j * 3 + i] == symbol for j in range(3)):
                return True
        # Check diagonals
        if (self.layers[layer][0] == self.layers[layer][4] == self.layers[layer][8] == symbol) or \
           (self.layers[layer][2] == self.layers[layer][4] == self.layers[layer][6] == symbol):
            return True
        return False

def prompt_move(board, current_player):
    while True:
        try:
            layer = int(input(f"{current_player.get_name()}, choose a layer number (1-3): ")) - 1
            square = int(input(f"{current_player.get_name()}, choose a square number (1-9): ")) - 1

            if 0 <= layer < 3 and 0 <= square < 9 and board.is_empty(layer, square):
                return layer, square
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers.")

def choose_starting_player(player1, player2):
    return random.choice([player1, player2])

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            return True
        elif choice == 'no':
            return False
        else:
            print("Invalid input. Enter 'yes' or 'no'.")

# Main game logic
player1 = Player(input("Player 1, enter your name: "))
player2 = Player(input("Player 2, enter your name: "))

while True:
    board = Board()
    clear_console()
    board.display()

    # Choose the starting player randomly for each game
    current_player = choose_starting_player(player1, player2)

    while True:
        layer, square = prompt_move(board, current_player)
        symbol = "X" if current_player == player1 else "O"

        if board.make_move(layer, square, symbol):
            clear_console()
            board.display()

            if board.check_win(layer, symbol):
                print(f"Congratulations, {current_player.get_name()}! You win!")
                current_player.record_win()
                if current_player == player1:
                    player2.record_loss()
                else:
                    player1.record_loss()
                break

            # Switch to the other player
            current_player = player1 if current_player == player2 else player2
        else:
            print("Invalid move. Try again.")

    print(player1.get_score())
    print(player2.get_score())

    if not play_again():
        break