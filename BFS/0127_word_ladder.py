from collections import deque

class Solution:
    
    def _make_masks(self, word):
        for i in range(len(word)):
            mask = word[:i] + '*' + word[i + 1:]
            yield mask

    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        # build an adjacent list
        graph = {}
        
        for word in wordList:
            for mask in self._make_masks(word):
                if mask not in graph:
                    graph[mask] = [word]
                else:
                    graph[mask].append(word)
                    
        queue = deque()
        visited = set()
        visited.add(beginWord)
        queue.append((beginWord, 1))
        
        while len(queue) > 0:
            popped, trans = queue.popleft()
            
            if popped == endWord:
                return trans
            
            for mask in self._make_masks(popped):
                if mask in graph:
                    for neighbor in graph[mask]:
                        if neighbor not in visited:
                            queue.append((neighbor, trans + 1))
                            visited.add(neighbor)
                        
        return 0