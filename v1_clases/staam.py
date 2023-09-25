class Board:

    def check_win(self):
        for l in range(self.layer):

            for r in range(self.row):
                if (
                    self.squares[l][r][0] == self.squares[l][r][1] == self.squares[l][r][2]
                    and self.squares[l][r][0] != " "
                ):
                    return self.squares[l][r][0]

            for c in range(self.col):
                if (
                    self.squares[l][0][c] == self.squares[l][1][c] == self.squares[l][2][c]
                    and self.squares[l][0][c] != " "
                ):
                    return self.squares[l][0][c]

            if (
                self.squares[l][0][0] == self.squares[l][1][1] == self.squares[l][2][2]
                and self.squares[l][0][0] != " "
            ):
                return self.squares[l][0][0]
            if (
                self.squares[l][0][2] == self.squares[l][1][1] == self.squares[l][2][0]
                and self.squares[l][0][2] != " "
            ):
                return self.squares[l][0][2]
####################################################################
        for r in range(self.row):
            for c in range(self.col):
                if (
                    self.squares[0][r][c] == self.squares[1][r][c] == self.squares[2][r][c]
                    and self.squares[0][r][c] != " "
                ):
                    return self.squares[0][r][c]

        #v
        if (
            self.squares[0][0][0] == self.squares[1][1][1] == self.squares[2][2][2]
            and self.squares[0][0][0] != " "
        ):
            return self.squares[0][0][0]
        
        
        if (
            self.squares[0][0][2] == self.squares[1][1][1] == self.squares[2][2][0]
            and self.squares[0][0][2] != " "
        ):
            return self.squares[0][0][2]

        for l in range(self.layer):
            for r in range(self.row):
                for c in range(self.col):
                    if self.squares[l][r][c] == " ":
                        return " "

        return "C"
