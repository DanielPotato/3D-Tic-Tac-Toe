class s:    
    def coomputer_turn(self):
        for l in range(self.layer):
        # Check if any row in this layer has the same symbol in all cells

            for r in range(self.row):
                if self.squares[l][r][0] == "X" and self.squares[l][r][1] == "X" : 
                    board.set_squares(l,r,3,"O")
                    return
                elif self.squares[l][r][1] == "X" and self.squares[l][r][2] == "X" :
                    board.set_squares(l,r,1,"O")
                    return
                elif self.squares[l][r][0] == "X" and self.squares[l][r][2] == "X" :
                    board.set_squares(l,r,2,"O")
                    return
              

            for c in range(self.col):
                if self.squares[l][0][c] == "X" and self.squares[l][1][c] == "X" : 
                    board.set_squares(l,3,c,"O")
                    return
                elif self.squares[l][1][c] == "X" and self.squares[l][2][c] == "X" :
                    board.set_squares(l,1,c,"O")
                    return
                elif self.squares[l][0][c] == "X" and self.squares[l][2][c] == "X" :
                    board.set_squares(l,2,c,"O")
                    return    
                
                
            if self.squares[l][0][0] == "X" and self.squares[l][1][1] == "X" : 
                board.set_squares(l,3,3,"O")
                return
            elif self.squares[l][1][1] == "X" and self.squares[l][2][2] == "X" :
                board.set_squares(l,1,1,"O")
                return
            elif self.squares[l][0][0] == "X" and self.squares[l][2][2] == "X" :
                board.set_squares(l,2,2,"O")
                return   

            if self.squares[l][0][2] == "X" and self.squares[l][1][1] == "X" : 
                board.set_squares(l,3,1,"O")
                return
            elif self.squares[l][1][1] == "X" and self.squares[l][2][0] == "X" :
                board.set_squares(l,1,3,"O")
                return
            elif self.squares[l][0][2] == "X" and self.squares[l][2][0] == "X" :
                board.set_squares(l,2,2,"O")
                return   

####################################################################
    # Check rows and columns across layers
        for r in range(self.row):
            for c in range(self.col):
                if self.squares[0][r][c] == "X" and self.squares[1][r][c] == "X" : 
                    board.set_squares(3,r,c,"O")
                    return
                elif self.squares[1][r][c] == "X" and self.squares[2][r][c] == "X" :
                    board.set_squares(1,r,c,"O")
                    return
                elif self.squares[0][r][c] == "X" and self.squares[2][r][c] == "X" :
                    board.set_squares(2,r,c,"O")
                    return   
                
                

    #  Check diagonals across layers
        if self.squares[0][0][0] == "X" and self.squares[1][1][1] == "X" : 
            board.set_squares(3,3,3,"O")
            return
        elif self.squares[1][1][1] == "X" and self.squares[2][2][2] == "X" :
            board.set_squares(1,1,1,"O")
            return
        elif self.squares[0][0][0] == "X" and self.squares[2][2][2] == "X" :
            board.set_squares(2,2,2,"O")
            return   
        
        if self.squares[0][0][2] == "X" and self.squares[1][1][1] == "X" : 
            board.set_squares(3,3,1,"O")
            return
        elif self.squares[1][1][1] == "X" and self.squares[2][2][0] == "X" :
            board.set_squares(1,1,3,"O")
            return
        elif self.squares[0][0][2] == "X" and self.squares[2][2][0] == "X" :
            board.set_squares(2,2,2,"O")
            return  
        
         
        layer_num=random.randint(1,3)
        row_num=random.randint(1,3)
        col_num=random.randint(1,3)
        board.set_squares(layer_num,row_num,col_num,"O")    