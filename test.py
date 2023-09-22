import random

class TicTacToe3D:
    def __init__(self):
        self.board = [[[' ' for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.players = []
        self.current_player = None

    def print_board(self):
        for row in self.board:
            for sub_row in row:
                print(' | '.join(sub_row))
            print("-" * 17)

    def choose_players(self):
        user1 = input("Player 1, please enter your name: ")
        user2 = input("Player 2, please enter your name: ")
        self.players = [user1, user2]
        self.current_player = random.choice(self.players)

    def player_input(self):
        while True:
            try:
                move = int(input(f"{self.current_player}, please enter your move (1-27): ")) - 1
                if 0 <= move < 27:
                    layer, row, col = divmod(move, 9)
                    if self.board[layer][row][col] == ' ':
                        return layer, row, col
                    else:
                        print("Invalid move. That position is already taken.")
                else:
                    print("Invalid input. Please enter a number between 1 and 27.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_win(self, player):
        # Check rows, columns, and diagonals in all dimensions
        for layer in range(3):
            for i in range(3):
                if all(self.board[layer][i][j] == player for j in range(3)) or \
                   all(self.board[layer][j][i] == player for j in range(3)):
                    return True

        # Check 3D diagonals
        if (
            all(self.board[layer][i][i] == player for i in range(3)) or
            all(self.board[layer][i][2 - i] == player for i in range(3))
        ):
            return True

        # Check diagonals between layers
        if all(self.board[i][i][i] == player for i in range(3)) or \
           all(self.board[i][i][2 - i] == player for i in range(3)):
            return True

        # Check diagonals across layers
        if all(self.board[i][j][j] == player for i, j in enumerate(range(2, -1, -1))) or \
           all(self.board[i][j][2 - j] == player for i, j in enumerate(range(2, -1, -1))):
            return True

        return False

    def is_board_full(self):
        for layer in self.board:
            for row in layer:
                if ' ' in row:
                    return False
        return True

    def play(self):
        self.print_board()
        self.choose_players()
        winner = None

        for _ in range(27):  # Maximum possible moves
            layer, row, col = self.player_input()
            self.board[layer][row][col] = 'X' if self.current_player == self.players[0] else 'O'
            self.print_board()

            if self.check_win('X'):
                winner = self.players[0]
                break
            elif self.check_win('O'):
                winner = self.players[1]
                break
            elif self.is_board_full():
                winner = "Tie"
                break

            self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

        if winner:
            print(f"Game over! {winner} wins!" if winner != "Tie" else "It's a tie!")
        else:
            print("The game is a draw.")

if __name__ == "__main__":
    game = TicTacToe3D()
    game.play()