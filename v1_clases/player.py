class Player: 
    def __init(self,name):
        self.name = name

    def get_name(self):
        return self._name
      
    def set_name(self, x):
        self._name = x


    def select_layer(self):

        valid = False
        while valid == False:
            layer = input("Choose layer number 1-3: ")
            if layer.isdigit() and 1 <= int(layer) <= 3:
                valid = True
            else:
                print("Invalid input")
        valid = False

        return int(layer)-1
    
    
    
    def select_square(self):
        '''
        this function returns tow variables 
        first variable will be layer number 
        second variable will be square numbe (we return square-1 )
        '''
        valid=False
        while valid == False:
            square = input("Choose Square number 1-9: ")
            if square.isdigit() and 1 <= int(square) <= 9:
                valid = True
            else:
                print("Invalid input")

        return  int(square)-1 

       

# player1=Player()
# player1.set_name("player1") 

# p1_name=player1.get_name()
# print(p1_name  )

# print(player1._name)      