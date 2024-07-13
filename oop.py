class Board:
    def __init__(self):
        self.board :list = [i for i in range(0,9)]

    def print_board(self):
        for group in zip(*[iter(self.board)] * 3):
            print(*group)

    def win_check(self):
        if self.board[0] == self.board[4] == self.board[8]:
                return True
        
        if self.board[2] == self.board[4] == self.board[6]:
                return True

        for i in range(0,3):
            if self.board[i] == self.board[i+3] == self.board[i+6]:
                return True
            
        for i in range(0,9,3):
            if self.board[i] == self.board[i+1] == self.board[i+2]:
                return True
            
    
class Player:
    def __init__(self, letter):
        self.index :int = None
        self.letter: str = letter

    def __str__(self):
        return f"{self.index}"
    
    def update_board(self,player,game):
        game.board[player.index] = self.letter
    
    def get_data(self):
        self.index :int = int(input(f"{'pls assign the index for :',self.letter}"))

    