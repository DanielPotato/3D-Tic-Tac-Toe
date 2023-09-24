import os

class Board :
    def __init__(self,layer=3,row=3,col=3):
        self.layer = layer
        self.row = row
        self.col = col
        self.squares=[[[" " for _ in range(self.col)] for _ in range(self.row)]for _ in range(self.layer)]

    def set_squares(self, layer, row, col, value):
        if (self.is_valid_indices(layer,row,col)
            and (value == "X" or value == "O" or value == " ")):
            
            self.squares[layer-1][row-1][col-1] = value
        else:
            print("Invalid input. Please provide valid layer, row, column, and value.")



    def displayBoard(self):
        os.system("clear")
        for l in range(self.layer):
            print(f"Layer :{l+1}")
            for r in range(self.row):
                for c in range(self.col):
                    if c != self.col -1 :
                        print(self.squares[l][r][c]+"|",end="")
                    else:
                        print(self.squares[l][r][c])
                if r != self.row - 1:
                    print("-"*6)
                else:
                    print("_"*6)                        

    def displayLayer(self, layer):
        os.system("clear")
        print(f"Layer: {layer}")
        layer-=1
        #print(" 1 2 3")
        for r in range(self.row):
            print(f"{r+1}",end="")
            for c in range(self.col):
                if c != self.col -1 :
                    print(self.squares[layer][r][c]+"|",end="")
                else:
                    print(self.squares[layer][r][c])
            if r != self.row - 1:
                print("-"*8)
            else:
                print("_"*8)   

    def displayRow(self,layer,row):
        os.system("clear")
        print("1 2 3")
        layer -=1
        row -=1
        for c in range(self.col):
            if c != self.col -1 :
                print(self.squares[layer][row][c]+"|",end="")
            else:
                print(self.squares[layer][row][c])        

    def is_valid_indices(self, layer, row, col):
        return (
            0 < layer <= self.layer
            and 0 < row <= self.row
            and 0 < col <= self.col
        )

    def is_square_empty(self, layer, row, col):
        if self.is_valid_indices(layer, row, col):
            return self.squares[layer-1][row-1][col-1] == " "
        else:
            print("Please provide valid Input!")
            return False

board = Board()

board.displayBoard()
result = board.is_square_empty(1, 1, 1)

print(result)
board.set_squares(1,1,1,"X")
board.set_squares(1,1,2,"X")
board.set_squares(1,1,3,"X")
board.displayBoard()
board.displayLayer(1)

result = board.is_square_empty(1, 1, 1)
board.displayRow(1, 1)
print(result)