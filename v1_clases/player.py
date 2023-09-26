import time 
import sys
class Player: 

    
    def __init__(self):
        self.name = None
        self.x_o=None
        self.counter = 0
    def get_name(self):
        return self.name
      
    def set_name(self, x):
        self.name = x
    def get_x_o(self):
        return self.name
      
    def set_x_o(self, x):
        self.x_o = x

    def pick_number(self):
        while True:
            try:
                number = int(input(" enter a number 1-3: "))
                if 1 <= number <= 3:
                    return number 
                else:
                    print(" Please choose a number between 1 and 3.")
            except ValueError:
                print(" Please enter a valid number ")

 

