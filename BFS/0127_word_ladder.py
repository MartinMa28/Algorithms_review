from collections import deque

class Solution:
    
    def _make_masks(self, word):
        masks = []
        for idx, ch in enumerate(word):
            masks.append(word[:idx] + '*' + word[idx + 1:])
            
        return masks
        
    def _build_graph(self, word_list):
        graph = {}
        
        for word in word_list:
            masks = self._make_masks(word)
            for m in masks:
                if m in graph:
                    graph[m].append(word)
                else:
                    graph[m] = [word]
                    
        return graph
    
    def ladderLength(self, beginWord: str, endWord: str, wordList:list) -> int:
        graph = self._build_graph(wordList)
        
        queue = deque([(beginWord, 1)])
        visited = set()
        
        while len(queue) > 0:
            pop_word, pop_len = queue.popleft()
            visited.add(pop_word)
            if pop_word == endWord:
                return pop_len
            
            masks = self._make_masks(pop_word)
            
            for m in masks:
                if m in graph:
                    for w in graph[m]:
                        if w not in visited:
                            queue.append((w, pop_len + 1))
                        
        return 0