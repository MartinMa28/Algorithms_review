class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        violations = 0
        
        if S == '':
            return 0
        
        for idx, ch in enumerate(S):
            if ch == '(':
                stack.append(idx)
            elif ch == ')':
                if len(stack) == 0:
                    violations += 1
                else:
                    stack.pop()
        
        if len(stack) > 0:
            violations += len(stack)
        
        return violations