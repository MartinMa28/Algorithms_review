class Trie:
    class Node:
        def __init__(self, is_end=False):
            self.is_end = is_end
            self.children = [None] * 26
            
        def insert(self, word):
            if len(word) == 1:
                if self.children[ord(word[0]) - 97]:
                    self.children[ord(word[0]) - 97].is_end = True
                else:
                    self.children[ord(word[0]) - 97] = Trie.Node(True)
            else:
                if self.children[ord(word[0]) - 97]:
                    self.children[ord(word[0]) - 97].insert(word[1:])
                else:
                    new_node = Trie.Node()
                    self.children[ord(word[0]) - 97] = new_node
                    new_node.insert(word[1:])
                    
        def search(self, word, starts_with=False):
            if not word:
                if not starts_with:
                    return self.is_end
                else:
                    return True
            else:
                if self.children[ord(word[0]) - 97]:
                    return self.children[ord(word[0]) - 97].search(word[1:], starts_with)
                else:
                    return False         
        
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = Trie.Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie_root.insert(word)
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.trie_root.search(word)
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.trie_root.search(prefix, starts_with=True)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)