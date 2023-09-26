class Cell:
    def __init__(self):
        self.value = " "

    def set_value(self, value):
        if value in ["X", "O", " "]:
            self.value = value
        else:
            print("Invalid input. Please provide a valid value.")

    def get_value(self):
        return self.value
    
    def __str__(self):
        return self.value        

class Row:
    def __init__(self, size=3):
        self.cells = [Cell() for _ in range(size)]

    def set_value(self, index, value):
        if 0 <= index < len(self.cells):
            self.cells[index].set_value(value)
        else:
            print("Invalid index. Please provide a valid index.")

    def get_cell(self, index):
        if 0 <= index < len(self.cells):
            return self.cells[index].get_value()
        else:
            print("Invalid index. Please provide a valid index.")
            return None
    def __str__(self):
        ret=""
        for c in range(self.cells):
                    if c != len(self.cells)-1 :
                        ret+=(str(self.cells[c])+"|")
                    else:
                        ret+=(str(self.cells[c]))
        return ret                        

class Layer(Row):
    def __init__(self, size=3):
        self.rows = [Row(size) for _ in range(size)]

    def set_value(self, row_index, cell_index, value):
        if 0 <= row_index < len(self.rows):
            self.rows[row_index].set_value(cell_index, value)
        else:
            print("Invalid row index. Please provide a valid index.")

    def get_cell(self, row_index, cell_index):
        if 0 <= row_index < len(self.rows):
            return self.rows[row_index].get_cell(cell_index)
        else:
            print("Invalid row index. Please provide a valid index.")
            return None

    def __str__(self):
        ret=""
        for r in len(self.rows):
            ret += str(self.rows[r])+"\n"
            if r != self.row - 1:
                ret+=("-"*6+"\n")
            else:
                ret+=("_"*6+"\n")
        return ret           
class Board(Layer):
    def __init__(self, size=3):
        self.layers = [Layer(size) for _ in range(size)]

    def set_value(self, layer_index, row_index, cell_index, value):
        if 0 <= layer_index < len(self.layers):
            self.layers[layer_index].set_value(row_index, cell_index, value)
        else:
            print("Invalid layer index. Please provide a valid index.")

    def get_cell(self, layer_index, row_index, cell_index):
        if 0 <= layer_index < len(self.layers):
            return self.layers[layer_index].get_cell(row_index, cell_index)
        else:
            print("Invalid layer index. Please provide a valid index.")
            return None
    def __str__(self):
        ret=""
        for l in len(self.layers):
            ret+=f"Layer :{l+1}\n{str(self.layers[l])}\n"
        return ret    