from collections import deque

class Solution:
    @staticmethod
    def _get_neighbors(s):
        res = []
        for idx, ch in enumerate(s):
            if ch == '(' or ch == ')':
                res.append(s[:idx] + s[idx + 1:])
        
        return res
    
    @staticmethod
    def _is_valid(s):
        stack = []
        
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        
    
    def removeInvalidParentheses(self, s: str) -> list:
        queue = deque([s])
        found = False
        visited = set()
        res = []
        
        while queue:
            next_level = []
            
            while queue:
                popped = queue.popleft()

                if self._is_valid(popped):
                    res.append(popped)
                    found = True

                if not found:
                    for neighbor in self._get_neighbors(popped):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_level.append(neighbor)
            
            if not found:
                queue = deque(next_level)
                
        return res