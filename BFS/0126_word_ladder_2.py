from collections import deque

class Solution:
    def _make_masks(self, s: str) -> list:
        masks = []
        
        for i in range(len(s)):
            mask = s[:i] + '*' + s[i + 1:]
            masks.append(mask)
            
        return masks
    
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = {}
        
        for w in wordList:
            for m in self._make_masks(w):
                if m not in graph:
                    graph[m] = [w]
                else:
                    graph[m].append(w)
        
        
        odd_q = deque([(beginWord,)])
        even_q = deque()
        res = []
        visited = set()
        found = False
        
        while (len(odd_q) > 0 or len(even_q) > 0) and (not found):
            if len(odd_q) > 0:
                while len(odd_q) > 0:
                    popped = odd_q.popleft()
                    visited.add(popped[-1])
                    if popped[-1] == endWord:
                        found = True
                        res.append(popped[:])
                    
                    if not found:
                        for m in self._make_masks(popped[-1]):
                            if m in graph:
                                for neighbor in graph[m]:
                                    if neighbor not in visited:
                                        even_q.append(popped + (neighbor,))
            else:
                while len(even_q) > 0:
                    popped = even_q.popleft()
                    visited.add(popped[-1])
                    if popped[-1] == endWord:
                        found = True
                        res.append(popped[:])
                        
                    if not found:
                        for m in self._make_masks(popped[-1]):
                            if m in graph:
                                for neighbor in graph[m]:
                                    if (neighbor not in visited):
                                        odd_q.append(popped + (neighbor,))
                                        
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))