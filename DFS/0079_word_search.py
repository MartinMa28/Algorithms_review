class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.cur_word = ''
        self.visited = set()


    def _is_safe(self, row, col) -> bool:
        if row >= 0 and row < len(self.board) \
            and col >= 0 and col < len(self.board[0]) \
            and (row, col) not in self.visited:
            return True
        else:
            return False

    def _dfs(self, row, col) -> bool:
        self.cur_word += self.board[row][col]
        self.visited.add((row, col))
        if self.word[len(self.cur_word) - 1] == self.cur_word[-1]:
            # If the added character is correct, keep 
            # searching other characters or the word is complete.
            if self.word == self.cur_word:
                return True
            else:
                for d in self.directions:
                    if self._is_safe(row + d[0], col + d[1]) \
                        and self._dfs(row + d[0], col + d[1]):
                        return True

        # No matter this character is not correct or this character
        # doesn't lead to the complete word, backtrack over here.
        self.cur_word = self.cur_word[:-1]
        self.visited.discard((row, col))

        return False
            
    def exist(self, board: list, word: list) -> bool:
        self.board = board
        self.word = word

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self._dfs(i, j):
                    return True

        return False