class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.p1 = set()
        self.p2 = set()
        self.n = n
    
    def _check_winner(self, player, row, col):
        # check the row
        for i in range(self.n):
            if (row, i) not in player:
                break
            
            if i == self.n - 1:
                return True
            
        # check the column
        for i in range(self.n):
            if (i, col) not in player:
                break
            
            if i == self.n - 1:
                return True
        
        # check the diagonals
        for i in range(self.n):
            if (i, i) not in player:
                break
            
            if i == self.n - 1:
                return True
        
        for i in range(self.n):
            if (self.n - 1 - i, i) not in player:
                break
                
            if i == self.n - 1:
                return True
        
        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.p1.add((row, col))
            if self._check_winner(self.p1, row, col):
                return 1
        else:
            self.p2.add((row, col))
            if self._check_winner(self.p2, row, col):
                return 2
        
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)