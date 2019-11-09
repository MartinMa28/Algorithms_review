from collections import deque

class Solution:
    def _is_valid(self, parens):
        if parens == '':
            return True
        
        stack = []
        for ch in parens:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
        
    
    def removeInvalidParentheses(self, s: str) -> list:
        if self._is_valid(s):
            return [s]
        
        results = []
        
        odd_q = deque([s])
        even_q = deque()
        found_valid = False
        
        while (len(odd_q) > 0 or len(even_q) > 0) and not found_valid:
            if len(odd_q) > 0:
                while len(odd_q) > 0:
                    popped = odd_q.popleft()
                    if self._is_valid(popped):
                        results.append(popped)
                        found_valid = True
                        # get all of possible valid results from this level
                        while len(odd_q) > 0:
                            possible = odd_q.popleft()
                            if self._is_valid(possible):
                                results.append(possible)
                    else:
                        for i in range(len(popped)):
                            if popped[i] == '(' or popped[i] == ')':
                                one_less = popped[:i] + popped[i+1:]
                                if one_less not in even_q:
                                    even_q.append(one_less)
                                
            else:
                while len(even_q) > 0:
                    popped = even_q.popleft()
                    if self._is_valid(popped):
                        results.append(popped)
                        found_valid = True
                        # get all of possible valid results from this level
                        while len(even_q) > 0:
                            possible = even_q.popleft()
                            if self._is_valid(possible):
                                results.append(possible)
                                
                    else:
                        for i in range(len(popped)):
                            if popped[i] == '(' or popped[i] == ')':
                                one_less = popped[:i] + popped[i+1:]
                                if one_less not in odd_q:
                                    odd_q.append(one_less)
        
        return results