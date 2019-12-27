class Trie:
    class Node:
        def __init__(self, is_end=False):
            self.is_end = is_end
            self.children = [None] * 26
            self.word = ''

        @staticmethod
        def _get_idx(ch):
            return ord(ch) - 97

        def insert(self, word, chars) -> None:
            if not chars:
                self.is_end = True
                self.word = word
            else:
                if self.children[self._get_idx(chars[0])]:
                    self.children[self._get_idx(chars[0])].insert(word, chars[1:])
                else:
                    new_node = Trie.Node()
                    self.children[self._get_idx(chars[0])] = new_node
                    new_node.insert(word, chars[1:])

        def search(self, prefix) -> str:
            """
            If the prefix exists in the trie, returns the whole word.
            Otherwise returns an empty string ''.
            """
            if not prefix:
                return self.word
            else:
                if self.children[self._get_idx(prefix[0])]:
                    if self.children[self._get_idx(prefix[0])].is_end:
                        return self.children[self._get_idx(prefix[0])].word
                    else:
                        return self.children[self._get_idx(prefix[0])].search(prefix[1:])
                else:
                    return ''

    def __init__(self):
        self.trie_root = Trie.Node()

    def insert(self, word) -> None:
        self.trie_root.insert(word, word)

    def search(self, prefix) -> str:
        return self.trie_root.search(prefix)

class Solution:

    @staticmethod
    def _helper(trie, word) -> str:
        prefix = trie.search(word)
        if prefix:
            return prefix
        else:
            return word

    def replaceWords(self, dictionary: list, sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)


        words = sentence.split(' ')
        roots = map(lambda w: self._helper(trie, w), words)

        return ' '.join(roots)