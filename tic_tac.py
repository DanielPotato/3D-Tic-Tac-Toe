import time 
import threading
import random

class Cell:
    def __init__(self):
        self.value = " "

    def set_value(self, value):
        if value in ["X", "O", " "]:
            self.value = value
        else:
            print("Invalid  value please Enter X/O")

    def get_value(self):
        return self.value
    
    def __str__(self):
        return self.value 
    
    def is_full(self):
        return self.value != " "       

class Row:
    def __init__(self, size=3):
        self.cells = [Cell() for _ in range(size)]

    def set_value(self, index, value):
        if 0 <= index < len(self.cells):
            self.cells[index].set_value(value)
        else:
            print("Invalid  index.")

    def get_cell(self, index):
        if 0 <= index < len(self.cells):
            return self.cells[index].get_value()
        else:
            print("Invalid  index.")
            return None
    def __str__(self):
        ret=""
        for c in range(3):
                    if c != len(self.cells)-1 :
                        ret+=(str(self.cells[c])+"|")
                    else:
                        ret+=(str(self.cells[c]))
        return ret                        
    
    def is_full(self):
        counter=0
        for c in self.cells:
            if c.is_full():
                counter+=1

        return counter == 3   

class Layer(Row):
    def __init__(self, size=3):
        self.rows = [Row(size) for _ in range(size)]

    def set_value(self, row_index, cell_index, value):
        if 0 <= row_index < len(self.rows):
            self.rows[row_index].set_value(cell_index, value)
        else:
            print("Invalid  index.")

    def get_cell(self, row_index, cell_index):
        if 0 <= row_index < len(self.rows):
            return self.rows[row_index].get_cell(cell_index)
        else:
            print("Invalid  index.")
            return None

    def __str__(self):
        ret=""
        for r in range(3):
            ret += f"{str(self.rows[r])}\n"
            if r != 2 :
                ret+=("-"*6+"\n")
            else:
                ret+=("_"*6+"\n")
        return ret  

    def is_full(self):
        counter=0
        for r in self.rows:
            if r.is_full():
                counter+=1
        return counter==3            

class Board(Layer):
    def __init__(self, size=3):
        self.layers = [Layer(size) for _ in range(size)]

    def set_value(self, layer_index, row_index, cell_index, value):
        if 0 <= layer_index < len(self.layers):
            self.layers[layer_index].set_value(row_index, cell_index, value)
        else:
            print("Invalid  index.")

    def get_cell(self, layer_index, row_index, cell_index):
        if 0 <= layer_index < len(self.layers):
            return self.layers[layer_index].get_cell(row_index, cell_index)
        else:
            print("Invalid  index.")
            return None
    def __str__(self):
        ret=""
        for l in range(3):
            ret+=f"Layer :{l+1}\n______\n{str(self.layers[l])}\n"
        return ret    

    def is_full(self):
        counter=0
        for l in self.layers:
            if l.is_full():
                counter+=1
            
        return counter==3  

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def make_move(self):
        pass


class Person(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
        self.timeout_expired = False  # Initialize the timeout flag


    def make_move(self):
        try:
            layer = int(input("Enter layer (1-3): ")) - 1
            row = int(input("Enter row (1-3): ")) - 1
            cell = int(input("Enter cell (1-3): ")) - 1

            if 0 <= layer < 3 and 0 <= row < 3 and 0 <= cell < 3:
                return layer, row, cell
            else:
                print("Invalid input enter numbers between (1-3)")
        except ValueError:
            print("Please enter a number")

            
class Computer(Player):
    def __init__(self, name,symbol):
        super().__init__(name, symbol)

    def make_move(self):
        
            layer_num = random.randint(1, 3)
            row_num = random.randint(1, 3)
            col_num = random.randint(1, 3)


            return layer_num, row_num, col_num


class Game(Board,Person):
    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def get_num_players(self):
        while True:
            try:
                num_players = int(input("Enter players (1 or 2): "))
                if num_players in [1, 2]:
                    return num_players
                else:
                    print("Invalid Please enter 1 or 2.")
            except ValueError:
                print("Invalid  Please enter a valid number")

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def do_move(self, layer_index, row_index, cell_index):
        if self.board.get_cell(layer_index, row_index, cell_index) == " ":
            self.board.set_value(layer_index, row_index, cell_index, self.current_player.get_symbol())
            self.switch_player()
        else:
            print("Invalid move. Please choose an empty cell.")


    def get_players(self):
        num_players = self.get_num_players()

        if num_players == 2:
            player1_name = input("Enter Player 1's name: ")
            player2_name = input("Enter Player 2's name: ")
        else:
            player1_name = input("Enter your name: ")
            player2_name = "Computer"

        players = [player1_name, player2_name]
        random.shuffle(players)
        if player2_name != "Computer":
            self.player1 = Person(players[0], "X")
            self.player2 = Person(players[1], "O")
        else:
            self.player1 = Person(players[0], "X")
            self.player2 = Computer( "Computer","O") 

        self.current_player = self.player1

    def check_win(self):

        # horizontal 
        for layer in range(3):
            for row in range(3):
                if self.board.get_cell(layer, row, 0) == self.board.get_cell(layer, row, 1) == self.board.get_cell(layer, row, 2) and self.board.get_cell(layer, row, 0) != " ":
                    return True

        # vertical 
        for layer in range(3):
            for col in range(3):
                if self.board.get_cell(layer, 0, col) == self.board.get_cell(layer, 1, col) == self.board.get_cell(layer, 2, col) and self.board.get_cell(layer, 0, col) != " ":
                    return True

        # diagonal
        for layer in range(3):
            if self.board.get_cell(layer, 0, 0) == self.board.get_cell(layer, 1, 1) == self.board.get_cell(layer, 2, 2) and self.board.get_cell(layer, 0, 0) != " ":
                return True
            if self.board.get_cell(layer, 2, 0) == self.board.get_cell(layer, 1, 1) == self.board.get_cell(layer, 0, 2) and self.board.get_cell(layer, 2, 0) != " ":
                return True

        #  3D  wins
        if self.board.get_cell(0, 0, 0) == self.board.get_cell(1, 1, 1) == self.board.get_cell(2, 2, 2) and self.board.get_cell(0, 0, 0) != " ":
            return True
        if self.board.get_cell(2, 0, 0) == self.board.get_cell(1, 1, 1) == self.board.get_cell(0, 2, 2) and self.board.get_cell(2, 0, 0) != " ":
            return True

        for row in range(3):
            for col in range(3):
                if self.board.get_cell( 0,row, col) == self.board.get_cell( 1,row, col) == self.board.get_cell( 2,row, col) and self.board.get_cell( 0,row, col) != " ":
                    return True
        return False

def main():
    print("Welcome to 3D Tic-Tac-Toe!")
    while True:
        game = Game()
        game.get_players()

        print(f"{game.player1.get_name()} is X, and {game.player2.get_name()} is O.")
        print("Let's start the game!\n")

        while not game.board.is_full():
            print(game.board)
            print(f"{game.current_player.get_name()}'s turn ({game.current_player.get_symbol()})")
            while True:
                curr_l,curr_r,curr_c=game.current_player.make_move()
                if game.board.get_cell(curr_l,curr_r,curr_c) == " " :
                    game.board.set_value(curr_l,curr_r,curr_c,game.current_player.get_symbol())
                    break
                else:
                    print("wrong input")
            if game.check_win():
                print(game.board)
                print(f"{game.current_player.get_name()} wins!")
                break  
            game.switch_player()
            if game.board.is_full():
                print("It's a tie!")
                break  

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break

main()