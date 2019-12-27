class Trie:
    class Node:
        def __init__(self, is_end=False):
            self.is_end = is_end
            self.children = [None] * 26
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = Trie.Node()
    
    def _insert(self, node: 'Trie.Node', word):
        if len(word) == 1:
            if node.children[ord(word[0]) - 97]:
                node.children[ord(word[0]) - 97].is_end = True
            else:
                node.children[ord(word[0]) - 97] = Trie.Node(True)
        else:
            if node.children[ord(word[0]) - 97]:
                self._insert(node.children[ord(word[0]) - 97], word[1:])
            else:
                new_node = Trie.Node()
                node.children[ord(word[0]) - 97] = new_node
                self._insert(new_node, word[1:])
            

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not self.trie_root.children[ord(word[0]) - 97]:
            if len(word) == 1:
                new_node = Trie.Node(True)
                self.trie_root.children[ord(word[0]) - 97] = new_node
            else:
                new_node = Trie.Node()
                self.trie_root.children[ord(word[0]) - 97] = new_node
                self._insert(new_node, word[1:])
        else:
            if len(word) == 1:
                self.trie_root.children[ord(word[0]) - 97].is_end = True
            else:
                self._insert(self.trie_root.children[ord(word[0]) - 97], word[1:])
        
    def _search(self, root: 'Trie.Node', word):
        if not word:
            return root.is_end
        else:
            if root.children[ord(word[0]) - 97]:
                return self._search(root.children[ord(word[0]) - 97], word[1:])
            else:
                return False
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if self.trie_root.children[ord(word[0]) - 97]:
            return self._search(self.trie_root.children[ord(word[0]) - 97], word[1:])
        else:
            return False
        
    def _starts_with(self, root: 'Trie.Node', prefix):
        if not prefix:
            return True
        else:
            if root.children[ord(prefix[0]) - 97]:
                return self._starts_with(root.children[ord(prefix[0]) - 97], prefix[1:])
            else:
                return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if self.trie_root.children[ord(prefix[0]) - ord('a')]:
            return self._starts_with(self.trie_root.children[ord(prefix[0]) - 97], prefix[1:])
        else:
            return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)