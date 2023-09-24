class Board :
    def __init__(self,layer=3,row=3,col=3):
        self.layer = layer
        self.row = row
        self.col = col
        self.squares=[[[" " for _ in range(self.col)] for _ in range(self.row)]for _ in range(self.layer)]

    def display(self):
        for l in range(self.layer):
            print(f"Layer :{l+1}")
            for r in range(self.row):
                for c in range(self.col):
                    if c != self.col -1 :
                        print(self.squares[l][r][c]+"|",end="")
                    else:
                        print(self.squares[l][r][c])
                if r != self.row - 1:
                    print("-------")
                else:
                    print("_________")                        


board=Board()
board.display()