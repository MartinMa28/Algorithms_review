from collections import deque, defaultdict

class Solution:
    @staticmethod
    def _make_masks(s: str) -> list:
        masks = []
        
        for i in range(len(s)):
            mask = s[:i] + '*' + s[i + 1:]
            masks.append(mask)
            
        return masks
    
    
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        
        for word in wordList:
            for mask in self._make_masks(word):
                graph[mask].append(word)
                
        visited = set()
        queue = deque([(beginWord, [beginWord])])
        found = False
        res = []
        
        while queue:
            next_level = []
            while queue:
                popped, cur_path = queue.popleft()
                visited.add(popped)
                if popped == endWord:
                    if not found:
                        found = True
                    
                    res.append(cur_path)
                
                for mask in self._make_masks(popped):
                    for neighbor in graph[mask]:
                        if neighbor not in visited and not found:
                            next_level.append((neighbor, cur_path + [neighbor]))
            
            if not found:
                queue = deque(next_level)
            
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))