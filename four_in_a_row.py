const_empty = " "
turns = ["X", "O"]

class board:
    x = 8
    y = 6
    grid = [[]]
    turn = turns[0]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = [[const_empty for i in range(x)] for i in range(y)]

    def print_board(self):
        for i in range(len(self.grid)):
            print(self.grid[i])
        
        print("")
        print([str(i) for i in range(self.x)])
        print("Turn: " + self.turn)
    
    def set_board(self, x, y, char):
        self.grid[y][x] = char
    
    def check_win(self):
        b = self.grid
        def check_horizontal():
            for i in range(self.y):
                for j in range(self.x - 3):
                    if b[i][j] == b[i][j + 1] == b[i][j + 2] == b[i][j + 3]:
                        if b[i][j] != const_empty:
                            return True
        def check_vertical():
            for i in range(self.y - 3):
                for j in range(self.x):
                    if b[i][j] == b[i + 1][j] == b[i + 2][j] == b[i + 3][j]:
                        if b[i][j] != const_empty:
                            return True
        def check_diagonal():
            def check_ld_ru():
                for i in range(self.y - 3):
                    for j in range(self.x - 3):
                        if b[i][j] == b[i + 1][j + 1] == b[i + 2][j + 2] == b[i + 3][j + 3]:
                            if b[i][j] != const_empty:
                                return True
            def check_lu_rd():
                for i in range(self.y - 3):
                    for j in range(self.x - 3):
                        if b[i][j + 3] == b[i + 1][j + 2] == b[i + 2][j + 1] == b[i + 3][j]:
                            if b[i][j + 3] != const_empty:
                                return True
            return check_ld_ru() or check_lu_rd()
        
        return check_horizontal() or check_vertical() or check_diagonal()
        
    def insert_token(self, column, char):
        b = self.grid
        for i in range(self.y):
            if b[self.y - i - 1][column] == const_empty:
                self.set_board(column, self.y - i - 1, char)
                return self.y - i - 1 >= 0
        
                
    
    def change_turns(self):
        if self.turn == turns[0]:
            self.turn = turns[1]
        else: 
            self.turn = turns[0]
    
    def start_turn(self):
        self.print_board()
        in_column = int(input("Column: "))
        print("\n\n")
        if self.insert_token(in_column, self.turn):
            if self.check_win():
                self.print_board()
                print("")
                return self.turn + " Wins!"
            self.change_turns()
        else:
            print("There is no space left in the column!")
        return self.start_turn()

game_board = board(8, 6)
print(game_board.start_turn())

