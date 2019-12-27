class Trie:
    class Node:
        def __init__(self, is_end=False):
            self.is_end = is_end
            self.word = ''
            self.children = [None] * 26
            
        @staticmethod
        def _get_idx(ch):
            return ord(ch) - 97
            
        def insert(self, word, chars) -> None:
            if len(chars) == 1:
                if self.children[self._get_idx(chars[0])]:
                    self.children[self._get_idx(chars[0])].is_end = True
                    self.children[self._get_idx(chars[0])].word = word
                else:
                    new_node = Trie.Node(is_end=True)
                    new_node.word = word
                    self.children[self._get_idx(chars[0])] = new_node
            else:
                if self.children[self._get_idx(chars[0])]:
                    self.children[self._get_idx(chars[0])].insert(word, chars[1:])
                else:
                    new_node = Trie.Node()
                    self.children[self._get_idx(chars[0])] = new_node
                    new_node.insert(word, chars[1:])
                    
        def search(self, ch) -> 'Trie.Node':
            return self.children[self._get_idx(ch)]
            
    def __init__(self):
        self.trie_root = Trie.Node()
        
    def insert(self, word):
        self.trie_root.insert(word, word)
        
    def search(self, word):
        return self.trie_root.search(word)
        
    

class Solution:
    def __init__(self):
        self.ans = []
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
    def _on_board(self, board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])
        
    def _backtrack(self, trie_node, board, row, col):
        if self._on_board(board, row, col) and board[row][col] != '$':
            node = trie_node.search(board[row][col])
            
            if node:
                if node.is_end:
                    self.ans.append(node.word)
                    node.is_end = False
                    node.word = ''
                
                ch_copy = board[row][col]
                board[row][col] = '$'
                for d in self.directions:
                    new_row = row + d[0]
                    new_col = col + d[1]

                    self._backtrack(node, board, new_row, new_col)
                
                # backtrack
                board[row][col] = ch_copy
                
            
        
    def findWords(self, board: list, words: list) -> list:
        if not board:
            return []
        
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self._backtrack(trie, board, i, j)
                
        return self.ans

if __name__ == "__main__":
    solu = Solution()
    print(solu.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],\
        ["oath","pea","eat","rain"]))