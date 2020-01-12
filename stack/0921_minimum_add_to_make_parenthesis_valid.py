class Solution:
    
    
    def minAddToMakeValid(self, S: str) -> int:
        """
        ())
        """
        unbalancity = 0
        stack = []
        
        for ch in S:
            if ch == '(':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalancity += 1
        
        return unbalancity + len(stack)